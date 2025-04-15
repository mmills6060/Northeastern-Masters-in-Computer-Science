import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from zipfile import ZipFile
import glob
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import gc  # For garbage collection
import re  # For regex pattern matching
import itertools  # For islice


def discover_available_timeframes():
    """
    Dynamically discover all available timeframes in the dataset directory
    
    Returns:
    --------
    list of str: Available timeframes in the format 'YYYY-qN'
    """
    # Base directory for datasets
    base_dir = "dataset"
    
    # If base_dir doesn't exist, try a few alternatives
    if not os.path.exists(base_dir):
        alternatives = [
            os.path.join(os.getcwd(), "dataset"),
            os.path.join(os.getcwd(), "CS_6140", "project", "dataset"),
            os.path.join(os.getcwd(), "CS_6140", "dataset")
        ]
        for alt in alternatives:
            if os.path.exists(alt):
                base_dir = alt
                break
    
    # If still doesn't exist
    if not os.path.exists(base_dir):
        print(f"Warning: Could not find dataset directory")
        return ['2019-q1', '2020-q1', '2021-q1']  # Return default timeframes
    
    print(f"Looking for timeframes in: {base_dir}")
    
    # List all subdirectories matching the pattern 'YYYY-qN'
    timeframe_pattern = re.compile(r'\d{4}-q[1-4]')
    timeframes = []
    
    # List all directories in the base_dir
    try:
        subdirs = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
        for subdir in subdirs:
            if timeframe_pattern.match(subdir):
                # Check if there are any parquet files in this directory
                parquet_files = glob.glob(os.path.join(base_dir, subdir, "*.parquet"))
                if parquet_files:
                    timeframes.append(subdir)
                    print(f"Found data for timeframe: {subdir}")
    except Exception as e:
        print(f"Error discovering timeframes: {e}")
    
    # Sort timeframes chronologically
    timeframes.sort()
    
    # If no timeframes found, return defaults
    if not timeframes:
        print("No timeframes found, using defaults")
        return ['2019-q1', '2020-q1', '2021-q1']
    
    print(f"Found {len(timeframes)} timeframes: {timeframes}")
    return timeframes


def load_dataset(timeframes=None, max_timeframes=4, sample_size=200000):
    """
    Load the Ookla Internet Speed dataset from local files
    
    Parameters:
    -----------
    timeframes : list of str, optional
        List of timeframes to load (e.g., ['2019-q1', '2019-q2']).
        If None, auto-discovers available timeframes.
    max_timeframes : int, optional
        Maximum number of timeframes to load to avoid memory issues.
        Default is 4 (one year's worth of data).
    sample_size : int, optional
        Number of rows to sample from each timeframe to avoid memory issues.
        Set to None to load all data (warning: may cause memory errors).
    
    Returns:
    --------
    pandas.DataFrame or None
    """
    if timeframes is None:
        # Auto-discover available timeframes
        timeframes = discover_available_timeframes()
    
    # Limit number of timeframes if needed
    if len(timeframes) > max_timeframes:
        print(f"WARNING: Found {len(timeframes)} timeframes but limiting to {max_timeframes} to avoid memory issues.")
        print(f"Using timeframes: {timeframes[:max_timeframes]}")
        print(f"To process more timeframes, modify the max_timeframes parameter or process in batches.")
        timeframes = timeframes[:max_timeframes]
    
    print(f"Loading data for timeframes: {timeframes}")
    
    all_dataframes = []
    
    for timeframe in timeframes:
        # Extract year from timeframe (e.g., '2019' from '2019-q1')
        year = timeframe.split('-')[0]
        
        # Extract quarter from timeframe (e.g., '1' from '2019-q1')
        quarter = timeframe.split('-q')[1]
        
        # Calculate the month based on the quarter
        month = (int(quarter) - 1) * 3 + 1  # q1->1, q2->4, q3->7, q4->10
        
        # Construct the file path for each timeframe
        file_path = f"dataset/{timeframe}/{year}-{month:02d}-01_performance_fixed_tiles.parquet"
        
        print(f"Attempting to load dataset from: {file_path}")
        
        # Handle absolute path as well (in case the relative path doesn't work)
        if not os.path.exists(file_path):
            # Try searching in a few different places
            possible_paths = [
                file_path,
                os.path.join(os.getcwd(), file_path),
                os.path.join(os.getcwd(), "CS_6140", "project", file_path),
                os.path.join(os.getcwd(), "CS_6140", file_path),
            ]
            
            # Find the first path that exists
            for path in possible_paths:
                if os.path.exists(path):
                    file_path = path
                    break
        
        try:
            # Check if the file exists
            if not os.path.exists(file_path):
                print(f"Warning: File not found at {file_path}")
                # Try to find any parquet file in the timeframe directory
                parent_dir = os.path.dirname(file_path)
                if os.path.exists(parent_dir):
                    parquet_files = glob.glob(os.path.join(parent_dir, "*.parquet"))
                    if parquet_files:
                        file_path = parquet_files[0]
                        print(f"Found alternative file: {file_path}")
                    else:
                        print(f"No parquet files found in {parent_dir}")
                        print(f"Skipping timeframe {timeframe}")
                        continue
                else:
                    print(f"Skipping timeframe {timeframe}")
                    continue
            
            # Load the file based on its extension
            if file_path.endswith('.csv'):
                if sample_size:
                    # First get total rows to calculate sampling fraction
                    total_rows = sum(1 for _ in open(file_path, 'r'))
                    sample_fraction = min(1.0, sample_size / total_rows)
                    df = pd.read_csv(file_path, skiprows=lambda i: i > 0 and np.random.random() > sample_fraction)
                else:
                    df = pd.read_csv(file_path)
            elif file_path.endswith('.parquet'):
                try:
                    # Try with pyarrow engine first
                    if sample_size:
                        # For parquet, we need to load and then sample
                        # Use memory-efficient approach by selecting only needed columns
                        # First, get the schema to know what columns are available
                        schema = pd.read_parquet(file_path, engine='pyarrow', columns=None).head(0)
                        required_cols = schema.columns.tolist()
                        
                        # Read the parquet file with specific columns and sample rows
                        df = pd.read_parquet(file_path, engine='pyarrow', columns=required_cols)
                        # Sample after loading to reduce memory usage
                        df = df.sample(n=min(sample_size, len(df)), random_state=42)
                    else:
                        df = pd.read_parquet(file_path, engine='pyarrow')
                except Exception as e:
                    print(f"Error with pyarrow: {e}")
                    try:
                        # Try with fastparquet engine
                        if sample_size:
                            # For fastparquet, we also load and then sample
                            df = pd.read_parquet(file_path, engine='fastparquet')
                            df = df.sample(n=min(sample_size, len(df)), random_state=42)
                        else:
                            df = pd.read_parquet(file_path, engine='fastparquet')
                    except Exception as e2:
                        print(f"Error with fastparquet: {e2}")
                        print(f"Skipping timeframe {timeframe}")
                        continue
            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                if sample_size:
                    # For Excel, load and then sample
                    df = pd.read_excel(file_path)
                    df = df.sample(n=min(sample_size, len(df)), random_state=42)
                else:
                    df = pd.read_excel(file_path)
            else:
                print(f"Unsupported file format: {file_path}")
                continue
            
            # Add a column to identify the timeframe
            df['timeframe'] = timeframe
            
            print(f"Loaded {timeframe} data successfully! Shape before sampling: {df.shape}")
            
            # Force garbage collection
            gc.collect()
            
            all_dataframes.append(df)
            
        except Exception as e:
            print(f"Error loading dataset for {timeframe}: {e}")
            print(f"Skipping timeframe {timeframe}")
    
    if not all_dataframes:
        print("No dataframes were loaded successfully.")
        return None
    
    # Combine all dataframes
    print("\nCombining all dataframes...")
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    print(f"Combined dataset shape: {combined_df.shape}")
    
    # Free memory
    del all_dataframes
    gc.collect()
    
    return combined_df


def analyze_correlation_over_time(df, latency_col='avg_lat_ms', output_dir='output'):
    """
    Analyze how correlations between factors and latency change over time across timeframes
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Combined dataset with all timeframes
    latency_col : str
        Name of the column containing latency data
    output_dir : str
        Directory to save output files
    
    Returns:
    --------
    dict: Dictionary with correlation data by timeframe
    """
    if 'timeframe' not in df.columns:
        print("No timeframe information available for correlation over time analysis")
        return None
    
    print("\n\n========== ANALYZING CORRELATION CHANGES OVER TIME ==========")
    
    # Make sure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Get unique timeframes and sort them
    timeframes = sorted(df['timeframe'].unique())
    print(f"Analyzing correlation changes across {len(timeframes)} timeframes: {timeframes}")
    
    # Dictionary to store correlation results for each timeframe
    correlation_by_timeframe = {}
    
    # Identify all numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    numeric_columns = [col for col in numeric_columns if col not in [latency_col, 'timeframe']]
    
    # Create DataFrames to store correlation values and p-values over time
    correlation_data = pd.DataFrame(index=timeframes, columns=numeric_columns, dtype=float)
    
    # Calculate correlations for each timeframe
    for timeframe in timeframes:
        # Filter data for this timeframe
        timeframe_df = df[df['timeframe'] == timeframe]
        
        # Skip if too few samples
        if len(timeframe_df) < 1000:
            print(f"Skipping {timeframe} - insufficient data ({len(timeframe_df)} samples)")
            continue
            
        print(f"\nAnalyzing correlations for timeframe {timeframe} ({len(timeframe_df)} samples):")
        
        # Calculate correlations for all numeric columns
        correlations = {}
        for col in numeric_columns:
            if col != latency_col and not pd.isna(timeframe_df[col]).all():
                corr = timeframe_df[[latency_col, col]].corr().iloc[0, 1]
                if not pd.isna(corr):
                    correlations[col] = float(corr)  # Convert to float explicitly
                    # Store correlation in the correlation_data DataFrame
                    correlation_data.loc[timeframe, col] = float(corr)  # Convert to float
                else:
                    # Fill NaN values with 0 directly
                    correlation_data.loc[timeframe, col] = 0.0
        
        # Sort correlations by absolute value
        sorted_correlations = sorted(correlations.items(), key=lambda x: abs(x[1]), reverse=True)
        
        # Print top correlations for this timeframe
        print(f"Top correlations with {latency_col} in {timeframe}:")
        for factor, corr in sorted_correlations[:5]:  # Top 5 correlations
            print(f"  - {factor}: {corr:.4f}")
        
        # Store the results
        correlation_by_timeframe[timeframe] = sorted_correlations
    
    # Make sure all values are numeric
    correlation_data = correlation_data.astype(float)
    
    # Now plot the heatmap
    try:
        # Convert the DataFrame to long format for plotting, ensuring data types
        correlation_long = correlation_data.reset_index().melt(
            id_vars=['index'], 
            value_vars=numeric_columns,
            var_name='Factor', 
            value_name='Correlation'
        )
        correlation_long.rename(columns={'index': 'Timeframe'}, inplace=True)
        correlation_long['Correlation'] = correlation_long['Correlation'].astype(float)
        
        # Create a pivot table with explicitly numeric values
        correlation_pivot = correlation_long.pivot_table(
            index='Factor', 
            columns='Timeframe', 
            values='Correlation',
            aggfunc='first'  # Just take the first value in case of duplicates
        ).astype(float)
        
        # Plot correlation heatmap over time
        plt.figure(figsize=(14, 10))
        sns.heatmap(correlation_pivot, annot=True, cmap='coolwarm', fmt=".2f", center=0)
        plt.title(f'Correlations with {latency_col} Across Timeframes')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'correlation_heatmap_over_time.png'))
        plt.close()
        print(f"Saved correlation heatmap over time to {output_dir}/correlation_heatmap_over_time.png")
    
        # Plot correlation line chart for top factors
        # Get top 5 factors with highest average absolute correlation
        mean_abs_corr = correlation_data.abs().mean().sort_values(ascending=False)
        top_factors = mean_abs_corr.index[:5].tolist()
        
        plt.figure(figsize=(14, 8))
        for factor in top_factors:
            plt.plot(timeframes, correlation_data[factor], marker='o', linewidth=2, label=factor)
        
        plt.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
        plt.grid(True, alpha=0.3)
        plt.xlabel('Timeframe')
        plt.ylabel(f'Correlation with {latency_col}')
        plt.title(f'Changes in Top Correlations with {latency_col} Over Time')
        plt.xticks(rotation=45)
        plt.legend(title='Factors')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'correlation_trends_over_time.png'))
        plt.close()
        print(f"Saved correlation trends over time to {output_dir}/correlation_trends_over_time.png")
    
        # Calculate correlation stability (standard deviation across timeframes)
        correlation_stability = correlation_data.std().sort_values(ascending=True)
        
        print("\nStability of correlations across timeframes (lower std = more stable):")
        stability_items = list(correlation_stability.items())
        for factor, std in stability_items[:10]:  # Top 10 most stable
            print(f"  - {factor}: {std:.4f}")
        
        # Plot correlation stability
        plt.figure(figsize=(12, 8))
        # Use only the top 10 most stable factors
        stability_df = pd.DataFrame({
            'Factor': correlation_stability.index[:10],
            'Stability': correlation_stability.values[:10]
        })
        sns.barplot(x='Stability', y='Factor', data=stability_df)
        plt.title('Stability of Correlations Across Timeframes')
        plt.xlabel('Standard Deviation (Lower = More Stable)')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'correlation_stability.png'))
        plt.close()
        print(f"Saved correlation stability plot to {output_dir}/correlation_stability.png")
    
    except Exception as e:
        print(f"Error during visualization: {e}")
        print("Skipping visualization but continuing with analysis")
    
    print("\nCorrelation over time analysis complete!")
    return correlation_by_timeframe


def analyze_latency_factors(df):
    """
    Analyze factors affecting network latency in the Ookla dataset
    """
    if df is None:
        return None
    
    # Create output directory
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)
    
    # Display basic information about the dataset
    print("\nDataset Information:")
    print(f"Number of records: {len(df)}")
    print(f"Columns: {df.columns.tolist()}")
    
    # Check if dataset is too large (more than 500,000 rows)
    if len(df) > 500000:
        print(f"Dataset is large ({len(df)} rows). Sampling data for analysis...")
        # Take a random sample to reduce memory usage
        df_sample = df.sample(n=500000, random_state=42)
        print(f"Using sample of 500,000 rows for analysis.")
    else:
        df_sample = df
    
    # Check if latency data is available
    if 'avg_lat_ms' not in df_sample.columns and 'latency' not in df_sample.columns:
        latency_col = None
        # Try to find a column related to latency
        for col in df_sample.columns:
            if 'lat' in col.lower() or 'rtt' in col.lower() or 'ping' in col.lower():
                latency_col = col
                print(f"Found potential latency column: {col}")
                break
        
        if latency_col is None:
            print("No latency data found in the dataset. Using avg_d_kbps as a proxy for performance.")
            # If no latency column, we can use download speed as our target variable
            if 'avg_d_kbps' in df_sample.columns:
                df_sample['latency_proxy'] = 1000 / df_sample['avg_d_kbps']  # Inverse of download speed as a proxy
                latency_col = 'latency_proxy'
                print("Created proxy latency measure based on download speed.")
            else:
                print("Cannot analyze latency: no suitable columns found")
                return df
    else:
        latency_col = 'avg_lat_ms' if 'avg_lat_ms' in df_sample.columns else 'latency'
    
    print(f"\nAnalyzing factors affecting {latency_col}...")
    
    # 1. Basic statistics for latency
    print(f"\n{latency_col} Statistics:")
    latency_stats = df_sample[latency_col].describe()
    print(latency_stats)
    
    # 2. Distribution of latency
    plt.figure(figsize=(10, 6))
    sns.histplot(df_sample[latency_col].dropna(), kde=True)
    plt.title(f'Distribution of {latency_col}')
    plt.xlabel(latency_col)
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(output_dir, 'latency_distribution.png'))
    plt.close()
    print(f"Saved latency distribution plot to {output_dir}/latency_distribution.png")
    
    # Check if we have timeframe data for temporal analysis
    if 'timeframe' in df_sample.columns:
        # Analyze latency trends over time
        plt.figure(figsize=(12, 8))
        time_trends = df_sample.groupby('timeframe')[latency_col].agg(['mean', 'median', 'std']).reset_index()
        time_trends = time_trends.sort_values('timeframe')
        
        # Plot mean latency by timeframe
        plt.subplot(2, 1, 1)
        sns.barplot(x='timeframe', y='mean', data=time_trends)
        plt.title(f'Mean {latency_col} by Timeframe')
        plt.xticks(rotation=45)
        
        # Plot median latency by timeframe
        plt.subplot(2, 1, 2)
        sns.barplot(x='timeframe', y='median', data=time_trends)
        plt.title(f'Median {latency_col} by Timeframe')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'latency_over_time.png'))
        plt.close()
        print(f"Saved latency trends over time to {output_dir}/latency_over_time.png")
        
        # Add timeframe as a potential factor
        print("\nLatency statistics by timeframe:")
        print(time_trends)
    
    # 3. Find potential factors that could affect latency
    potential_factors = []
    
    # Network speed factors
    speed_factors = [col for col in df_sample.columns if 'kbps' in col.lower() or 'mbps' in col.lower() or 'speed' in col.lower()]
    potential_factors.extend(speed_factors)
    
    # Network type/technology factors
    network_factors = [col for col in df_sample.columns if 'network' in col.lower() or 'tech' in col.lower() or 'type' in col.lower()]
    potential_factors.extend(network_factors)
    
    # Geographic factors - looking for lat/long or location columns
    geo_factors = [col for col in df_sample.columns if 'lat' in col.lower() or 'lon' in col.lower() or 'location' in col.lower() or 'geo' in col.lower()]
    geo_factors = [col for col in geo_factors if col != latency_col]  # Remove latency column from geo factors
    potential_factors.extend(geo_factors)
    
    # Time-related factors
    time_factors = [col for col in df_sample.columns if 'time' in col.lower() or 'date' in col.lower() or 'hour' in col.lower() or 'day' in col.lower() or 'timeframe' in col.lower()]
    potential_factors.extend(time_factors)
    
    # Get unique factors (remove duplicates)
    potential_factors = list(set(potential_factors))
    
    print("\nPotential factors that may affect latency:")
    for factor in potential_factors:
        print(f"- {factor}")
    
    # 4. Correlation analysis
    numeric_columns = df_sample.select_dtypes(include=['number']).columns.tolist()
    if len(numeric_columns) > 1:
        # Calculate correlations
        correlation_with_latency = []
        for col in numeric_columns:
            if col != latency_col and not pd.isna(df_sample[col]).all():
                corr = df_sample[[latency_col, col]].corr().iloc[0, 1]
                if not pd.isna(corr):
                    correlation_with_latency.append((col, corr))
        
        # Sort by absolute correlation
        correlation_with_latency.sort(key=lambda x: abs(x[1]), reverse=True)
        
        print("\nCorrelation of factors with latency:")
        for factor, corr in correlation_with_latency[:10]:  # Top 10 correlations
            print(f"{factor}: {corr:.4f}")
        
        # Create correlation heatmap
        top_correlated = [factor for factor, _ in correlation_with_latency[:min(8, len(correlation_with_latency))]]
        if latency_col not in top_correlated:
            top_correlated.append(latency_col)
        
        if len(top_correlated) > 1:
            plt.figure(figsize=(12, 10))
            correlation_matrix = df_sample[top_correlated].corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
            plt.title('Correlation between Latency and Other Factors')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, 'latency_correlation_heatmap.png'))
            plt.close()
            print(f"Saved correlation heatmap to {output_dir}/latency_correlation_heatmap.png")
    
    # 5. Visualize relationship between latency and top correlated factors
    if 'correlation_with_latency' in locals() and len(correlation_with_latency) > 0:
        # Pick top 3 correlated factors
        top_factors = [factor for factor, _ in correlation_with_latency[:min(3, len(correlation_with_latency))]]
        
        for factor in top_factors:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=factor, y=latency_col, data=df_sample, alpha=0.5)
            plt.title(f'Relationship between {latency_col} and {factor}')
            plt.xlabel(factor)
            plt.ylabel(latency_col)
            plt.savefig(os.path.join(output_dir, f'latency_vs_{factor}.png'))
            plt.close()
            print(f"Saved scatter plot to {output_dir}/latency_vs_{factor}.png")
    
    # 6. Build a simple predictive model for latency
    try:
        print("\nBuilding predictive model for latency...")
        # Prepare features
        if 'correlation_with_latency' in locals() and len(correlation_with_latency) > 0:
            # Use top correlated numeric features
            # Limit to top 5 features to reduce complexity for RandomForest
            features = [factor for factor, _ in correlation_with_latency[:min(5, len(correlation_with_latency))]]
            print(f"Using top {len(features)} features for modeling: {features}")
            
            # Add timeframe as a categorical feature if available
            if 'timeframe' in df_sample.columns and 'timeframe' not in features:
                # Create dummy variables for timeframe
                timeframe_dummies = pd.get_dummies(df_sample['timeframe'], prefix='timeframe')
                df_sample_with_dummies = pd.concat([df_sample[features + [latency_col]], timeframe_dummies], axis=1)
                # Update features list to include the dummy variables
                features.extend(timeframe_dummies.columns.tolist())
                print(f"Added timeframe dummy variables as features")
                X = df_sample_with_dummies[features].copy()
            else:
                X = df_sample[features].copy()
            
            y = df_sample[latency_col].copy()
            
            # Handle NaN values
            X = X.fillna(X.mean())
            y = y.fillna(y.mean())
            
            # Further reduce dataset size for modeling if needed
            if len(X) > 100000:
                print(f"Further sampling data for modeling to 100,000 rows...")
                X_sampled, _, y_sampled, _ = train_test_split(X, y, train_size=100000, random_state=42)
                X, y = X_sampled, y_sampled
                print(f"Using {len(X)} samples for modeling")
                # Force garbage collection to free memory
                gc.collect()
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Standardize features
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            
            # Train models
            # Linear Regression
            print("Training Linear Regression model...")
            lr_model = LinearRegression()
            lr_model.fit(X_train_scaled, y_train)
            lr_pred = lr_model.predict(X_test_scaled)
            lr_mse = mean_squared_error(y_test, lr_pred)
            lr_r2 = r2_score(y_test, lr_pred)
            
            print(f"Linear Regression Results:")
            print(f"  - MSE: {lr_mse:.4f}")
            print(f"  - R² Score: {lr_r2:.4f}")
            
            # Free memory before Random Forest
            del X_train_scaled, X_test_scaled
            gc.collect()
            
            # Random Forest with memory optimization
            print("Training Random Forest model with reduced parameters...")
            # Use fewer estimators and limit max_depth to reduce memory usage
            rf_model = RandomForestRegressor(
                n_estimators=50,  # Reduced from 100
                max_depth=10,     # Limit depth to reduce memory
                min_samples_split=10,
                max_features='sqrt',  # Use sqrt of features to reduce complexity
                n_jobs=2,         # Limit parallelism to reduce memory
                random_state=42
            )
            
            try:
                rf_model.fit(X_train, y_train)
                rf_pred = rf_model.predict(X_test)
                rf_mse = mean_squared_error(y_test, rf_pred)
                rf_r2 = r2_score(y_test, rf_pred)
                
                print(f"Random Forest Results:")
                print(f"  - MSE: {rf_mse:.4f}")
                print(f"  - R² Score: {rf_r2:.4f}")
                
                # Feature importance (Random Forest)
                feature_importance = pd.DataFrame({
                    'Feature': X.columns.tolist(),  # Use column names from X
                    'Importance': rf_model.feature_importances_
                }).sort_values('Importance', ascending=False)
                
                print("\nFeature Importance (Random Forest):")
                for idx, row in feature_importance.iterrows():
                    print(f"  - {row['Feature']}: {row['Importance']:.4f}")
                
                # Visualize feature importance
                plt.figure(figsize=(12, 8))
                sns.barplot(x='Importance', y='Feature', data=feature_importance)
                plt.title('Feature Importance for Predicting Latency')
                plt.tight_layout()
                plt.savefig(os.path.join(output_dir, 'latency_feature_importance.png'))
                plt.close()
                print(f"Saved feature importance plot to {output_dir}/latency_feature_importance.png")
            except MemoryError:
                print("Memory error when training Random Forest model.")
                print("Skipping Random Forest model due to memory constraints.")
                print("Linear Regression results are still available.")
                
    except Exception as e:
        print(f"Error building predictive model: {e}")
    
    print("\nLatency analysis complete!")
    return df


def main():
    # Load the dataset with auto-discovery of timeframes, loading all available 
    # timeframes and sampling 100,000 rows from each to avoid memory issues
    # Increase max_timeframes to analyze more timeframes
    df = load_dataset(max_timeframes=12, sample_size=100000)

    # Analyze factors affecting latency
    if df is not None:
        # Regular analysis
        df = analyze_latency_factors(df)
        
        # Add correlation over time analysis
        correlation_by_timeframe = analyze_correlation_over_time(df)
        
        print("\nData loading and all analyses complete!")

    return df


if __name__ == "__main__":
    df = main()
