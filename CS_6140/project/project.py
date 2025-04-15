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


def load_dataset():
    """
    Load the Ookla Internet Speed dataset from a local file
    """
    # Use a relative path starting from the current directory
    file_path = "dataset/2019-q1/2019-01-01_performance_fixed_tiles.parquet"

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

    print(f"Attempting to load dataset from: {file_path}")

    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            print(
                "Please ensure the Ookla dataset is downloaded and provide the correct path.")
            print(
                "The expected structure is: dataset/2019-q1/2019-01-01_performance_fixed_tiles.parquet")
            return None

        # If it's a zip file, extract it first
        if file_path.endswith('.zip'):
            print("Extracting zip file...")
            extract_dir = os.path.join(os.path.dirname(file_path), 'extracted')
            os.makedirs(extract_dir, exist_ok=True)

            with ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)

            print(f"Files extracted to: {extract_dir}")

            # Find all potential data files in the extracted directory
            csv_files = glob.glob(os.path.join(
                extract_dir, '**', '*.csv'), recursive=True)
            parquet_files = glob.glob(os.path.join(
                extract_dir, '**', '*.parquet'), recursive=True)
            excel_files = glob.glob(os.path.join(extract_dir, '**', '*.xlsx'), recursive=True) + \
                glob.glob(os.path.join(
                    extract_dir, '**', '*.xls'), recursive=True)

            # Prioritize files to load
            data_files = csv_files + parquet_files + excel_files

            if not data_files:
                print("No data files found in the extracted directory.")
                shp_files = glob.glob(os.path.join(
                    extract_dir, '**', '*.shp'), recursive=True)
                if shp_files:
                    print(f"Found {
                          len(shp_files)} shapefile(s). To load these, install geopandas and use:")
                    print("import geopandas as gpd")
                    print(f"gdf = gpd.read_file('{shp_files[0]}')")
                return None

            file_path = data_files[0]
            print(f"Loading data from: {file_path}")

        # Load the file based on its extension
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.parquet'):
            try:
                # Try with pyarrow engine first
                df = pd.read_parquet(file_path, engine='pyarrow')
            except Exception as e:
                print(f"Error with pyarrow: {e}")
                try:
                    # Try with fastparquet engine
                    df = pd.read_parquet(file_path, engine='fastparquet')
                except Exception as e2:
                    print(f"Error with fastparquet: {e2}")
                    print(
                        "\nTo read parquet files, you need to install the required packages:")
                    print("pip install pyarrow fastparquet")
                    return None
        elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
            df = pd.read_excel(file_path)
        else:
            print(f"Unsupported file format: {file_path}")
            return None

        print("\nDataset loaded successfully!")
        print(f"Shape: {df.shape}")
        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")
        print("\nTry installing necessary dependencies:")
        print("pip install pandas pyarrow fastparquet matplotlib seaborn scikit-learn")
        return None


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
    time_factors = [col for col in df_sample.columns if 'time' in col.lower() or 'date' in col.lower() or 'hour' in col.lower() or 'day' in col.lower()]
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
                    'Feature': features,
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
    # Load the dataset
    df = load_dataset()

    # Analyze factors affecting latency
    if df is not None:
        df = analyze_latency_factors(df)
        print("\nData loading and analysis complete!")

    return df


if __name__ == "__main__":
    df = main()
