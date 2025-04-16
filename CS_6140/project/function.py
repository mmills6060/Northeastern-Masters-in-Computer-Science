# %% [markdown]
# # Network Latency Analysis
# This notebook analyzes factors affecting network latency in the dataset.

# %% [markdown]
# ## Import Libraries

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# %% [markdown]
# ## Define Helper Functions

# %%
def prepare_dataset(df):
    """Prepare dataset for latency analysis by sampling if necessary."""
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
        
    return df_sample

# %%
def identify_latency_column(df_sample):
    """Identify the column representing latency or create a proxy."""
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
                return df_sample, None
    else:
        latency_col = 'avg_lat_ms' if 'avg_lat_ms' in df_sample.columns else 'latency'
    
    print(f"\nAnalyzing factors affecting {latency_col}...")
    return df_sample, latency_col

# %%
def analyze_basic_statistics(df_sample, latency_col):
    """Analyze and display basic statistics for latency."""
    if latency_col is None:
        return
        
    print(f"\n{latency_col} Statistics:")
    latency_stats = df_sample[latency_col].describe()
    print(latency_stats)

    # Distribution of latency
    plt.figure(figsize=(10, 6))
    sns.histplot(df_sample[latency_col].dropna(), kde=True)
    plt.title(f'Distribution of {latency_col}')
    plt.xlabel(latency_col)
    plt.ylabel('Frequency')
    plt.show()

# %%
def analyze_temporal_trends(df_sample, latency_col):
    """Analyze latency trends over time if timeframe data is available."""
    if latency_col is None or 'timeframe' not in df_sample.columns:
        return
    
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
    plt.show()

    # Add timeframe as a potential factor
    print("\nLatency statistics by timeframe:")
    print(time_trends)
    
    return time_trends

# %%
def identify_potential_factors(df_sample, latency_col):
    """Identify potential factors that could affect latency."""
    if latency_col is None:
        return []
        
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
        
    return potential_factors

# %%
def perform_correlation_analysis(df_sample, latency_col):
    """Perform correlation analysis between latency and other numeric factors."""
    if latency_col is None:
        return None
        
    numeric_columns = df_sample.select_dtypes(include=['number']).columns.tolist()
    if len(numeric_columns) <= 1:
        return None
        
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
        plt.show()
        
    return correlation_with_latency

# %%
def visualize_top_correlations(df_sample, latency_col, correlation_with_latency):
    """Visualize relationship between latency and top correlated factors."""
    if latency_col is None or correlation_with_latency is None or len(correlation_with_latency) == 0:
        return
        
    # Pick top 3 correlated factors
    top_factors = [factor for factor, _ in correlation_with_latency[:min(3, len(correlation_with_latency))]]

    for factor in top_factors:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=factor, y=latency_col, data=df_sample, alpha=0.5)
        plt.title(f'Relationship between {latency_col} and {factor}')
        plt.xlabel(factor)
        plt.ylabel(latency_col)
        plt.show()

# %%
def train_linear_regression(X_train, X_test, y_train, y_test):
    """Train and evaluate a linear regression model."""
    # Standardize features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("Training Linear Regression model...")
    lr_model = LinearRegression()
    lr_model.fit(X_train_scaled, y_train)
    lr_pred = lr_model.predict(X_test_scaled)
    lr_mse = mean_squared_error(y_test, lr_pred)
    lr_r2 = r2_score(y_test, lr_pred)

    print(f"Linear Regression Results:")
    print(f"  - MSE: {lr_mse:.4f}")
    print(f"  - R² Score: {lr_r2:.4f}")
    
    # Free memory
    del X_train_scaled, X_test_scaled
    gc.collect()
    
    return {
        'mse': lr_mse,
        'r2': lr_r2
    }

# %%
def train_random_forest(X_train, X_test, y_train, y_test, feature_names):
    """Train and evaluate a random forest model."""
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

    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_mse = mean_squared_error(y_test, rf_pred)
    rf_r2 = r2_score(y_test, rf_pred)

    print(f"Random Forest Results:")
    print(f"  - MSE: {rf_mse:.4f}")
    print(f"  - R² Score: {rf_r2:.4f}")

    # Feature importance (Random Forest)
    feature_importance = pd.DataFrame({
        'Feature': feature_names,
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
    plt.show()
    
    return feature_importance

# %%
def build_predictive_model(df_sample, latency_col, correlation_with_latency):
    """Build predictive models for latency based on correlated factors."""
    if latency_col is None or correlation_with_latency is None or len(correlation_with_latency) == 0:
        return
        
    try:
        print("\nBuilding predictive model for latency...")
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

        # Train and evaluate linear regression model
        linear_regression_results = train_linear_regression(X_train, X_test, y_train, y_test)
        
        # Train and evaluate random forest model
        feature_importance = train_random_forest(X_train, X_test, y_train, y_test, X.columns.tolist())
        
        return feature_importance
        
    except Exception as e:
        print(f"Error building predictive model: {e}")
        return None

# %% [markdown]
# ## Load Data
# This section assumes you have already loaded your data into a DataFrame called `df`

# %% [markdown]
# ## Analysis Pipeline

# %% [markdown]
# ### 1. Prepare Dataset

# %%
# Prepare dataset for analysis
df_sample = prepare_dataset(df)

# %% [markdown]
# ### 2. Identify Latency Column

# %%
# Identify latency column
df_sample, latency_col = identify_latency_column(df_sample)

# %% [markdown]
# ### 3. Analyze Basic Statistics

# %%
# Check if latency analysis can proceed
if latency_col is None:
    print("Cannot proceed with latency analysis: no suitable latency column found")
else:
    # Analyze basic statistics
    analyze_basic_statistics(df_sample, latency_col)

# %% [markdown]
# ### 4. Analyze Temporal Trends

# %%
# Analyze temporal trends if latency column exists
if latency_col is not None:
    time_trends = analyze_temporal_trends(df_sample, latency_col)

# %% [markdown]
# ### 5. Identify Potential Factors

# %%
# Identify potential factors if latency column exists
if latency_col is not None:
    potential_factors = identify_potential_factors(df_sample, latency_col)

# %% [markdown]
# ### 6. Perform Correlation Analysis

# %%
# Perform correlation analysis if latency column exists
if latency_col is not None:
    correlation_with_latency = perform_correlation_analysis(df_sample, latency_col)

# %% [markdown]
# ### 7. Visualize Top Correlations

# %%
# Visualize top correlations if latency column exists and correlations were found
if latency_col is not None and 'correlation_with_latency' in locals() and correlation_with_latency is not None:
    visualize_top_correlations(df_sample, latency_col, correlation_with_latency)

# %% [markdown]
# ### 8. Build Predictive Models

# %%
# Build predictive models if latency column exists and correlations were found
if latency_col is not None and 'correlation_with_latency' in locals() and correlation_with_latency is not None:
    feature_importance = build_predictive_model(df_sample, latency_col, correlation_with_latency)

# %% [markdown]
# ## Conclusion

# %%
if latency_col is not None:
    print("\nLatency analysis complete!")
else:
    print("\nLatency analysis could not be performed due to missing latency data.")