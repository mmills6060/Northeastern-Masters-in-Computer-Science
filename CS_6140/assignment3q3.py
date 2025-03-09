import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_circles
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
import time
from typing import Tuple, List
import pandas as pd

class SVM:
    def __init__(self, kernel='linear', C=1.0, max_iter=100, tol=1e-3):
        """
        Initialize SVM with kernel and hyperparameters
        
        Args:
            kernel (str): The kernel type ('linear', 'poly', 'rbf', 'sigmoid')
            C (float): Regularization parameter
            max_iter (int): Maximum number of iterations
            tol (float): Tolerance for stopping criterion
        """
        self.kernel = kernel
        self.C = C
        self.max_iter = max_iter
        self.tol = tol
        self.alphas = None
        self.support_vectors = None
        self.support_vector_labels = None
        self.b = 0
        self.K = None  # Cache for kernel matrix
        
    def _kernel_function(self, x1, x2):
        """Compute kernel function between x1 and x2"""
        if self.kernel == 'linear':
            return np.dot(x1, x2.T)
        elif self.kernel == 'poly':
            degree = 2  # Reduced from 3 to 2 for faster computation
            return (np.dot(x1, x2.T) + 1) ** degree
        elif self.kernel == 'rbf':
            gamma = 1.0  # Increased from 0.1 for better separation
            if len(x1.shape) == 1:
                x1 = x1.reshape(1, -1)
            if len(x2.shape) == 1:
                x2 = x2.reshape(1, -1)
            return np.exp(-gamma * np.sum((x1[:, np.newaxis] - x2) ** 2, axis=2))
        elif self.kernel == 'sigmoid':
            gamma = 0.1
            coef0 = 1.0  # Changed from 0.0 for better performance
            return np.tanh(gamma * np.dot(x1, x2.T) + coef0)
            
    def _compute_error(self, i, X, y):
        """Compute error for index i"""
        if self.K is None:
            output_i = self._decision_function(X[i], X, y)
        else:
            output_i = np.sum(self.alphas * y * self.K[i]) + self.b
        return output_i - y[i]
            
    def fit(self, X, y, max_time=30):
        """
        Train the SVM classifier using Sequential Minimal Optimization (SMO)
        
        Args:
            X (np.ndarray): Training features
            y (np.ndarray): Training labels (-1 or 1)
            max_time (int): Maximum training time in seconds
        """
        start_time = time.time()
        n_samples = X.shape[0]
        
        # Initialize alphas and b
        self.alphas = np.zeros(n_samples)
        self.b = 0
        
        # Compute and cache kernel matrix
        self.K = self._kernel_function(X, X)
        
        # SMO optimization
        iter_counter = 0
        max_passes = 5  # Reduced from 10 to 5
        passes = 0
        
        while passes < max_passes and iter_counter < self.max_iter:
            if time.time() - start_time > max_time:
                print(f"Training stopped after {max_time} seconds")
                break
                
            alpha_pairs_changed = 0
            
            # Randomly shuffle indices for better convergence
            indices = np.random.permutation(n_samples)
            
            for i in indices:
                # Calculate error
                Ei = self._compute_error(i, X, y)
                
                # Check KKT conditions with stricter tolerance
                if ((y[i] * Ei < -self.tol and self.alphas[i] < self.C) or
                    (y[i] * Ei > self.tol and self.alphas[i] > 0)):
                    
                    # Choose second alpha heuristically
                    if Ei > 0:
                        j = np.argmin([self._compute_error(k, X, y) for k in range(n_samples)])
                    else:
                        j = np.argmax([self._compute_error(k, X, y) for k in range(n_samples)])
                    
                    # Calculate error for j
                    Ej = self._compute_error(j, X, y)
                    
                    # Save old alphas
                    alpha_i_old = self.alphas[i].copy()
                    alpha_j_old = self.alphas[j].copy()
                    
                    # Compute bounds L and H
                    if y[i] != y[j]:
                        L = max(0, self.alphas[j] - self.alphas[i])
                        H = min(self.C, self.C + self.alphas[j] - self.alphas[i])
                    else:
                        L = max(0, self.alphas[i] + self.alphas[j] - self.C)
                        H = min(self.C, self.alphas[i] + self.alphas[j])
                    
                    if abs(L - H) < 1e-4:
                        continue
                    
                    # Compute eta
                    eta = 2.0 * self.K[i,j] - self.K[i,i] - self.K[j,j]
                    if eta >= 0:
                        continue
                    
                    # Update alpha j
                    self.alphas[j] -= y[j] * (Ei - Ej) / eta
                    self.alphas[j] = min(H, max(L, self.alphas[j]))
                    
                    if abs(self.alphas[j] - alpha_j_old) < 1e-5:
                        continue
                    
                    # Update alpha i
                    self.alphas[i] += y[i] * y[j] * (alpha_j_old - self.alphas[j])
                    
                    # Compute b
                    b1 = self.b - Ei - y[i] * (self.alphas[i] - alpha_i_old) * self.K[i,i] - \
                         y[j] * (self.alphas[j] - alpha_j_old) * self.K[i,j]
                    b2 = self.b - Ej - y[i] * (self.alphas[i] - alpha_i_old) * self.K[i,j] - \
                         y[j] * (self.alphas[j] - alpha_j_old) * self.K[j,j]
                    
                    if 0 < self.alphas[i] < self.C:
                        self.b = b1
                    elif 0 < self.alphas[j] < self.C:
                        self.b = b2
                    else:
                        self.b = (b1 + b2) / 2
                    
                    alpha_pairs_changed += 1
            
            if alpha_pairs_changed == 0:
                passes += 1
            else:
                passes = 0
                
            iter_counter += 1
            if iter_counter % 10 == 0:
                print(f"Iteration {iter_counter}, passes without change: {passes}")
        
        # Save support vectors
        support_vector_indices = self.alphas > 1e-5
        self.support_vectors = X[support_vector_indices]
        self.support_vector_labels = y[support_vector_indices]
        self.alphas = self.alphas[support_vector_indices]
        
        # Clear kernel cache
        self.K = None
        
        training_time = time.time() - start_time
        print(f"Training completed in {training_time:.2f} seconds with {len(self.support_vectors)} support vectors")
        
    def _decision_function(self, X, support_vectors, support_vector_labels):
        """Compute decision function for samples X"""
        if len(X.shape) == 1:
            X = X.reshape(1, -1)
        kernel_matrix = self._kernel_function(X, support_vectors)
        return np.sum(self.alphas * support_vector_labels * kernel_matrix, axis=1) + self.b
        
    def predict(self, X):
        """
        Predict class labels for samples in X
        
        Args:
            X (np.ndarray): Features to predict
            
        Returns:
            np.ndarray: Predicted class labels
        """
        if self.support_vectors is None:
            raise Exception("Model not trained yet!")
            
        if len(X.shape) == 1:
            X = X.reshape(1, -1)
            
        decision_values = self._decision_function(X, self.support_vectors, self.support_vector_labels)
        return np.sign(decision_values)

class MLP:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01, max_epochs=1000):
        """
        Initialize Multi-Layer Perceptron
        
        Args:
            input_size (int): Number of input features
            hidden_size (int): Number of neurons in hidden layer
            output_size (int): Number of output classes
            learning_rate (float): Learning rate for gradient descent
            max_epochs (int): Maximum number of training epochs
        """
        self.weights1 = np.random.randn(input_size, hidden_size) * 0.01
        self.bias1 = np.zeros((1, hidden_size))
        self.weights2 = np.random.randn(hidden_size, output_size) * 0.01
        self.bias2 = np.zeros((1, output_size))
        self.learning_rate = learning_rate
        self.max_epochs = max_epochs
        
    def _sigmoid(self, x):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))  # Clip to avoid overflow
    
    def _sigmoid_derivative(self, x):
        """Derivative of sigmoid function"""
        return x * (1 - x)
        
    def fit(self, X, y):
        """
        Train the MLP classifier using backpropagation
        
        Args:
            X (np.ndarray): Training features
            y (np.ndarray): Training labels
        """
        # Convert y to one-hot encoding if needed
        if len(y.shape) == 1:
            y_one_hot = np.zeros((y.shape[0], 2))
            y_one_hot[np.arange(y.shape[0]), y] = 1
            y = y_one_hot
            
        for epoch in range(self.max_epochs):
            # Forward propagation
            layer1 = self._sigmoid(np.dot(X, self.weights1) + self.bias1)
            output = self._sigmoid(np.dot(layer1, self.weights2) + self.bias2)
            
            # Backpropagation
            output_error = y - output
            output_delta = output_error * self._sigmoid_derivative(output)
            
            layer1_error = np.dot(output_delta, self.weights2.T)
            layer1_delta = layer1_error * self._sigmoid_derivative(layer1)
            
            # Update weights and biases
            self.weights2 += self.learning_rate * np.dot(layer1.T, output_delta)
            self.bias2 += self.learning_rate * np.sum(output_delta, axis=0, keepdims=True)
            self.weights1 += self.learning_rate * np.dot(X.T, layer1_delta)
            self.bias1 += self.learning_rate * np.sum(layer1_delta, axis=0, keepdims=True)
            
            # Early stopping if error is small enough
            if np.mean(np.abs(output_error)) < 1e-4:
                break
                
    def predict(self, X):
        """
        Predict class labels for samples in X
        
        Args:
            X (np.ndarray): Features to predict
            
        Returns:
            np.ndarray: Predicted class labels
        """
        layer1 = self._sigmoid(np.dot(X, self.weights1) + self.bias1)
        output = self._sigmoid(np.dot(layer1, self.weights2) + self.bias2)
        return np.argmax(output, axis=1)

def generate_datasets(n_samples: int) -> Tuple[List[np.ndarray], List[np.ndarray]]:
    """
    Generate half-circles and moons datasets
    
    Args:
        n_samples (int): Number of samples to generate
        
    Returns:
        Tuple containing lists of X and y for both datasets
    """
    # Generate half circles
    X_circles, y_circles = make_circles(n_samples=n_samples, noise=0.1, factor=0.5)
    
    # Generate moons
    X_moons, y_moons = make_moons(n_samples=n_samples, noise=0.1)
    
    # Scale the features
    scaler = StandardScaler()
    X_circles = scaler.fit_transform(X_circles)
    X_moons = scaler.fit_transform(X_moons)
    
    return [X_circles, X_moons], [y_circles, y_moons]

def visualize_dataset(X: np.ndarray, y: np.ndarray, title: str):
    """
    Visualize a dataset with different colors for different classes
    
    Args:
        X (np.ndarray): Features
        y (np.ndarray): Labels
        title (str): Plot title
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='blue', label='Class 0')
    plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='red', label='Class 1')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()

def visualize_decision_boundary(model, X, y, title):
    """
    Visualize the decision boundary of a trained model
    
    Args:
        model: Trained model (SVM or MLP)
        X (np.ndarray): Features
        y (np.ndarray): Labels
        title (str): Plot title
    """
    # Create a mesh grid
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                        np.arange(y_min, y_max, 0.02))
    
    # Make predictions on the mesh grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Plot decision boundary and points
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='blue', label='Class 0')
    plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='red', label='Class 1')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.show()

def evaluate_model(model, X_train, y_train, X_test, y_test):
    """
    Evaluate a model's performance
    
    Args:
        model: Trained model (SVM or MLP)
        X_train (np.ndarray): Training features
        y_train (np.ndarray): Training labels
        X_test (np.ndarray): Test features
        y_test (np.ndarray): Test labels
        
    Returns:
        dict: Dictionary containing various performance metrics
    """
    # Start timing
    start_time = time.time()
    
    # Train the model
    model.fit(X_train, y_train)
    
    # End timing
    training_time = time.time() - start_time
    
    # Get predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    # Calculate accuracy
    train_accuracy = np.mean(y_train_pred == y_train)
    test_accuracy = np.mean(y_test_pred == y_test)
    
    return {
        'train_accuracy': train_accuracy,
        'test_accuracy': test_accuracy,
        'training_time': training_time
    }

def main():
    # Generate datasets
    n_samples_list = [1000, 10000]
    datasets = []
    labels = []
    
    for n_samples in n_samples_list:
        X_list, y_list = generate_datasets(n_samples)
        datasets.extend(X_list)
        labels.extend(y_list)
    
    # Visualize datasets
    dataset_names = ['Half-circles (1000)', 'Moons (1000)', 
                    'Half-circles (10000)', 'Moons (10000)']
    
    for X, y, name in zip(datasets, labels, dataset_names):
        visualize_dataset(X, y, name)
    
    # Initialize results dictionary
    results = {
        'dataset': [],
        'model': [],
        'train_accuracy': [],
        'test_accuracy': [],
        'training_time': []
    }
    
    # Perform k-fold cross validation
    k_folds = 5
    kf = KFold(n_splits=k_folds, shuffle=True, random_state=42)
    
    # Models to evaluate
    svm_kernels = ['linear', 'poly', 'rbf', 'sigmoid']
    
    for i, (X, y) in enumerate(zip(datasets, labels)):
        dataset_name = dataset_names[i]
        print(f"\nProcessing {dataset_name}...")
        
        # Evaluate SVM with different kernels
        for kernel in svm_kernels:
            print(f"Training SVM with {kernel} kernel...")
            fold_results = []
            best_model = None
            best_accuracy = -1
            
            for train_idx, test_idx in kf.split(X):
                X_train, X_test = X[train_idx], X[test_idx]
                y_train, y_test = y[train_idx], y[test_idx]
                
                # Convert labels to -1, 1 for SVM
                y_train_svm = 2 * y_train - 1
                y_test_svm = 2 * y_test - 1
                
                svm = SVM(kernel=kernel)
                metrics = evaluate_model(svm, X_train, y_train_svm, X_test, y_test_svm)
                fold_results.append(metrics)
                
                # Keep track of best model
                if metrics['test_accuracy'] > best_accuracy:
                    best_accuracy = metrics['test_accuracy']
                    best_model = svm
            
            # Average results across folds
            avg_results = {
                'train_accuracy': np.mean([r['train_accuracy'] for r in fold_results]),
                'test_accuracy': np.mean([r['test_accuracy'] for r in fold_results]),
                'training_time': np.mean([r['training_time'] for r in fold_results])
            }
            
            # Store results
            results['dataset'].append(dataset_name)
            results['model'].append(f'SVM-{kernel}')
            results['train_accuracy'].append(avg_results['train_accuracy'])
            results['test_accuracy'].append(avg_results['test_accuracy'])
            results['training_time'].append(avg_results['training_time'])
            
            # Visualize decision boundary for best model
            if best_model is not None:
                visualize_decision_boundary(best_model, X, 2 * y - 1,
                                         f'SVM-{kernel} Decision Boundary - {dataset_name}')
        
        # Evaluate MLP
        print("Training MLP...")
        fold_results = []
        best_model = None
        best_accuracy = -1
        
        for train_idx, test_idx in kf.split(X):
            X_train, X_test = X[train_idx], X[test_idx]
            y_train, y_test = y[train_idx], y[test_idx]
            
            mlp = MLP(input_size=2, hidden_size=10, output_size=2)
            metrics = evaluate_model(mlp, X_train, y_train, X_test, y_test)
            fold_results.append(metrics)
            
            # Keep track of best model
            if metrics['test_accuracy'] > best_accuracy:
                best_accuracy = metrics['test_accuracy']
                best_model = mlp
        
        # Average results across folds
        avg_results = {
            'train_accuracy': np.mean([r['train_accuracy'] for r in fold_results]),
            'test_accuracy': np.mean([r['test_accuracy'] for r in fold_results]),
            'training_time': np.mean([r['training_time'] for r in fold_results])
        }
        
        # Store results
        results['dataset'].append(dataset_name)
        results['model'].append('MLP')
        results['train_accuracy'].append(avg_results['train_accuracy'])
        results['test_accuracy'].append(avg_results['test_accuracy'])
        results['training_time'].append(avg_results['training_time'])
        
        # Visualize decision boundary for best model
        if best_model is not None:
            visualize_decision_boundary(best_model, X, y,
                                     f'MLP Decision Boundary - {dataset_name}')
    
    # Create results DataFrame and display
    results_df = pd.DataFrame(results)
    print("\nResults Summary:")
    print(results_df.to_string(index=False))
    
    # Save results to CSV
    results_df.to_csv('classification_results.csv', index=False)
    print("\nResults have been saved to 'classification_results.csv'")

if __name__ == "__main__":
    main()
