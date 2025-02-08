# Step 1: Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso

# Suppress warnings
warnings.filterwarnings('ignore')

def load_boston_housing_data():
    """Load Boston Housing dataset from CMU website."""
    url = "https://lib.stat.cmu.edu/datasets/boston"
    response = requests.get(url)
    
    # Find the start of the data
    data_start = None
    lines = response.text.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('0.00632'):
            data_start = i
            break
    
    if data_start is None:
        raise ValueError("Could not find the start of the data")
    
    # Extract the actual data (first 506 rows)
    data_lines = []
    current_line = ""
    
    for line in lines[data_start:]:
        if not line.strip():  # Skip empty lines
            continue
        current_line += " " + line.strip()
        if len(current_line.split()) >= 14:  # Each row should have 14 values
            data_lines.append(current_line.strip())
            current_line = ""
        if len(data_lines) >= 506:  # We have all the data
            break
    
    # Convert to DataFrame
    data = [row.split() for row in data_lines]
    df = pd.DataFrame(data, dtype=float, columns=[
        'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
        'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV'
    ])
    
    return df

def main():
    # Step 2: Load your data
    print("Loading Boston Housing dataset from CMU...")
    df = load_boston_housing_data()

    # Data Preprocessing
    print("\n1. Data Preprocessing")
    print("Original data shape:", df.shape)
    print("\nFeature descriptions:")
    print("CRIM    - per capita crime rate by town")
    print("ZN      - proportion of residential land zoned for lots over 25,000 sq.ft")
    print("INDUS   - proportion of non-retail business acres per town")
    print("CHAS    - Charles River dummy variable (1 if tract bounds river; 0 otherwise)")
    print("NOX     - nitric oxides concentration (parts per 10 million)")
    print("RM      - average number of rooms per dwelling")
    print("AGE     - proportion of owner-occupied units built prior to 1940")
    print("DIS     - weighted distances to five Boston employment centers")
    print("RAD     - index of accessibility to radial highways")
    print("TAX     - full-value property-tax rate per $10,000")
    print("PTRATIO - pupil-teacher ratio by town")
    print("B       - 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town")
    print("LSTAT   - % lower status of the population")
    print("MEDV    - Median value of owner-occupied homes in $1000's")
    
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # Split features and target
    X = df.drop('MEDV', axis=1)  # Features
    y = df['MEDV']  # Target variable
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("\nTraining set shape:", X_train_scaled.shape)
    print("Test set shape:", X_test_scaled.shape)
    
    # Print summary statistics of the processed data
    print("\nSummary statistics of processed features:")
    print(pd.DataFrame(X_train_scaled, columns=X.columns).describe())
    
    # 2. Implement and evaluate OLS Regression
    print("\n2. OLS Regression Results")
    # Our implementation
    ols = OLSRegression()
    ols.fit(X_train_scaled, y_train)
    y_pred_ols = ols.predict(X_test_scaled)
    
    # Scikit-learn implementation for comparison
    sk_ols = LinearRegression()
    sk_ols.fit(X_train_scaled, y_train)
    y_pred_sk_ols = sk_ols.predict(X_test_scaled)
    
    print("\nOur Implementation:")
    print("MSE:", mean_squared_error(y_test, y_pred_ols))
    print("R2 Score:", r2_score(y_test, y_pred_ols))
    print("\nScikit-learn Implementation:")
    print("MSE:", mean_squared_error(y_test, y_pred_sk_ols))
    print("R2 Score:", r2_score(y_test, y_pred_sk_ols))
    
    # 3. Implement and evaluate Ridge Regression
    print("\n3. Ridge Regression Results")
    lambda_values = [0.5, 1.0, 1.5, 2.0]
    
    for lambda_param in lambda_values:
        print(f"\nLambda = {lambda_param}")
        
        # Our implementation
        ridge = RidgeRegression(lambda_param=lambda_param)
        ridge.fit(X_train_scaled, y_train)
        y_pred_ridge = ridge.predict(X_test_scaled)
        
        # Scikit-learn implementation
        sk_ridge = Ridge(alpha=lambda_param)
        sk_ridge.fit(X_train_scaled, y_train)
        y_pred_sk_ridge = sk_ridge.predict(X_test_scaled)
        
        print("Our Implementation:")
        print("MSE:", mean_squared_error(y_test, y_pred_ridge))
        print("R2 Score:", r2_score(y_test, y_pred_ridge))
        print("\nScikit-learn Implementation:")
        print("MSE:", mean_squared_error(y_test, y_pred_sk_ridge))
        print("R2 Score:", r2_score(y_test, y_pred_sk_ridge))
    
    # 4. Implement and evaluate Lasso Regression
    print("\n4. Lasso Regression Results")
    
    for lambda_param in lambda_values:
        print(f"\nLambda = {lambda_param}")
        
        # Our implementation
        lasso = LassoRegression(lambda_param=lambda_param)
        lasso.fit(X_train_scaled, y_train)
        y_pred_lasso = lasso.predict(X_test_scaled)
        
        # Scikit-learn implementation
        sk_lasso = Lasso(alpha=lambda_param)
        sk_lasso.fit(X_train_scaled, y_train)
        y_pred_sk_lasso = sk_lasso.predict(X_test_scaled)
        
        print("Our Implementation:")
        print("MSE:", mean_squared_error(y_test, y_pred_lasso))
        print("R2 Score:", r2_score(y_test, y_pred_lasso))
        print("\nScikit-learn Implementation:")
        print("MSE:", mean_squared_error(y_test, y_pred_sk_lasso))
        print("R2 Score:", r2_score(y_test, y_pred_sk_lasso))
    
    # 5. Visualization and Analysis
    plt.figure(figsize=(15, 5))
    
    # Plot actual vs predicted values for OLS
    plt.subplot(131)
    plt.scatter(y_test, y_pred_ols, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('OLS Regression')
    
    # Plot actual vs predicted values for Ridge (λ=1.0)
    ridge = RidgeRegression(lambda_param=1.0)
    ridge.fit(X_train_scaled, y_train)
    y_pred_ridge = ridge.predict(X_test_scaled)
    
    plt.subplot(132)
    plt.scatter(y_test, y_pred_ridge, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Ridge Regression (λ=1.0)')
    
    # Plot actual vs predicted values for Lasso (λ=1.0)
    lasso = LassoRegression(lambda_param=1.0)
    lasso.fit(X_train_scaled, y_train)
    y_pred_lasso = lasso.predict(X_test_scaled)
    
    plt.subplot(133)
    plt.scatter(y_test, y_pred_lasso, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Lasso Regression (λ=1.0)')
    
    plt.tight_layout()
    plt.show()
    
    # Plot feature coefficients comparison
    feature_names = X.columns
    coefficients_df = pd.DataFrame({
        'Feature': feature_names,
        'OLS': ols.coefficients,
        'Ridge': ridge.coefficients,
        'Lasso': lasso.coefficients
    })
    
    plt.figure(figsize=(12, 6))
    coefficients_df.plot(x='Feature', y=['OLS', 'Ridge', 'Lasso'], kind='bar')
    plt.title('Feature Coefficients Comparison')
    plt.xlabel('Features')
    plt.ylabel('Coefficient Value')
    plt.xticks(rotation=45)
    plt.legend(title='Model')
    plt.tight_layout()
    plt.show()

class OLSRegression:
    def __init__(self):
        self.coefficients = None
        self.intercept = None
    
    def fit(self, X, y):
        # Add column of ones for intercept
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        # Calculate coefficients using normal equation: θ = (X^T X)^(-1) X^T y
        theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
        self.intercept = theta[0]
        self.coefficients = theta[1:]
        return self
    
    def predict(self, X):
        return np.dot(X, self.coefficients) + self.intercept

class RidgeRegression:
    def __init__(self, lambda_param=1.0):
        self.lambda_param = lambda_param
        self.coefficients = None
        self.intercept = None
    
    def fit(self, X, y):
        # Add column of ones for intercept
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        # Calculate coefficients using Ridge formula: θ = (X^T X + λI)^(-1) X^T y
        identity = np.eye(X_b.shape[1])
        identity[0, 0] = 0  # Don't regularize the intercept
        theta = np.linalg.inv(X_b.T.dot(X_b) + self.lambda_param * identity).dot(X_b.T).dot(y)
        self.intercept = theta[0]
        self.coefficients = theta[1:]
        return self
    
    def predict(self, X):
        return np.dot(X, self.coefficients) + self.intercept

class LassoRegression:
    def __init__(self, lambda_param=1.0, learning_rate=0.01, n_iterations=1000, tol=1e-4):
        self.lambda_param = lambda_param
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.tol = tol
        self.coefficients = None
        self.intercept = None
    
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.coefficients = np.zeros(n_features)
        self.intercept = 0
        
        for _ in range(self.n_iterations):
            # Store previous coefficients for convergence check
            prev_coefficients = np.copy(self.coefficients)
            prev_intercept = self.intercept
            
            # Update intercept
            y_pred = self.predict(X)
            self.intercept -= self.learning_rate * np.mean(y_pred - y)
            
            # Update coefficients
            for j in range(n_features):
                # Calculate gradient for feature j
                gradient = np.mean((y_pred - y) * X[:, j])
                # Add L1 regularization term
                if self.coefficients[j] > 0:
                    gradient += self.lambda_param
                elif self.coefficients[j] < 0:
                    gradient -= self.lambda_param
                self.coefficients[j] -= self.learning_rate * gradient
            
            # Check for convergence
            if np.sum(np.abs(prev_coefficients - self.coefficients)) < self.tol and \
               np.abs(prev_intercept - self.intercept) < self.tol:
                break
        
        return self
    
    def predict(self, X):
        return np.dot(X, self.coefficients) + self.intercept

if __name__ == "__main__":
    main()