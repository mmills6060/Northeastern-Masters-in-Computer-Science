import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import hamming_loss, jaccard_score
import pandas as pd
import requests
import io

class MultiLabelSVM:
    def __init__(self):
        self.classifiers = []
        
    def fit(self, X, y):
        """
        Train a binary SVM classifier for each label
        
        Parameters:
        X: Features matrix
        y: Labels matrix (multi-label format)
        """
        n_labels = y.shape[1]
        self.classifiers = []
        
        print("Training multi-label SVMs:")
        for i in range(n_labels):
            print(f"Training classifier for label {i+1}/{n_labels}...")
            # Create and train a binary SVM for each label with faster parameters
            svm = SVC(kernel='rbf', probability=True, max_iter=1000, tol=1e-3)
            svm.fit(X, y[:, i])
            self.classifiers.append(svm)
            print(f"Finished training classifier {i+1}")
    
    def predict(self, X):
        """
        Predict labels for input samples
        
        Parameters:
        X: Features matrix
        
        Returns:
        Predictions matrix (multi-label format)
        """
        n_samples = X.shape[0]
        n_labels = len(self.classifiers)
        predictions = np.zeros((n_samples, n_labels))
        
        for i, classifier in enumerate(self.classifiers):
            predictions[:, i] = classifier.predict(X)
            
        return predictions

def load_plantgo_dataset():
    """
    Load the PlantGo dataset from local ARFF files
    """
    # Local paths for the PlantGo dataset
    train_path = "/home/michael-mills/Documents/Northeastern-Masters-in-Computer-Science/CS_6140/PlantGO-RandomTrainTest-Mulan/PlantGO-train.arff"
    test_path = "/home/michael-mills/Documents/Northeastern-Masters-in-Computer-Science/CS_6140/PlantGO-RandomTrainTest-Mulan/PlantGO-test.arff"
    
    try:
        # Function to parse ARFF format
        def parse_arff(file_path):
            with open(file_path, 'r') as f:
                content = f.readlines()
            
            data_section = False
            header = []
            data = []
            n_attributes = 0
            
            for line in content:
                line = line.strip()
                if line.lower().startswith('@data'):
                    data_section = True
                    continue
                elif line.lower().startswith('@attribute'):
                    header.append(line.split()[1])
                    n_attributes += 1
                elif data_section and line:
                    # Handle sparse ARFF format
                    if line.startswith('{'):
                        # Remove braces and split by comma
                        pairs = line.strip('{}').split(',')
                        # Create a zero vector
                        row = np.zeros(n_attributes)
                        # Fill in non-zero values
                        for pair in pairs:
                            if pair.strip():  # Skip empty pairs
                                idx, val = pair.strip().split()
                                row[int(idx)] = float(val)
                        data.append(row)
                    else:
                        # Handle dense format if present
                        data.append([float(x) if x != '?' else 0 for x in line.split(',')])
            
            return np.array(data)
        
        # Load and parse training and test data
        train_data = parse_arff(train_path)
        test_data = parse_arff(test_path)
        
        if len(train_data) == 0 or len(test_data) == 0:
            raise Exception("Failed to parse data")
        
        # The last 12 columns are labels in PlantGo dataset
        X_train = train_data[:, :-12]
        y_train = train_data[:, -12:]
        
        X_test = test_data[:, :-12]
        y_test = test_data[:, -12:]
        
        return X_train, X_test, y_train, y_test
        
    except Exception as e:
        print(f"Error loading PlantGo dataset: {e}")
        print("Please ensure the ARFF files exist in the specified paths")
        return None, None, None, None

def evaluate_multilabel(y_true, y_pred):
    """
    Evaluate multi-label classification results
    """
    results = {
        'Hamming Loss': hamming_loss(y_true, y_pred),
        'Jaccard Score': jaccard_score(y_true, y_pred, average='samples'),
        'Precision': precision_score(y_true, y_pred, average='macro'),
        'Recall': recall_score(y_true, y_pred, average='macro'),
        'F1 Score': f1_score(y_true, y_pred, average='macro')
    }
    return results

def evaluate_multiclass(y_true, y_pred):
    """
    Evaluate multi-class classification results
    """
    results = {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, average='macro'),
        'Recall': recall_score(y_true, y_pred, average='macro'),
        'F1 Score': f1_score(y_true, y_pred, average='macro')
    }
    return results

def main():
    # Part 1: Multi-Label Classification with PlantGo dataset
    print("Part 1: Multi-Label Classification (PlantGo Dataset)")
    print("-" * 50)
    
    # Load PlantGo dataset
    X_train, X_test, y_train, y_test = load_plantgo_dataset()
    
    if X_train is not None:
        # Scale the features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Train multi-label SVM
        print("Training Multi-Label SVM...")
        mlsvm = MultiLabelSVM()
        mlsvm.fit(X_train_scaled, y_train)
        
        # Make predictions
        print("Making predictions...")
        y_pred = mlsvm.predict(X_test_scaled)
        
        # Evaluate results
        results = evaluate_multilabel(y_test, y_pred)
        print("\nMulti-Label Classification Results:")
        for metric, value in results.items():
            print(f"{metric}: {value:.4f}")
    
    # Part 2: Multi-Class Classification with MNIST dataset
    print("\nPart 2: Multi-Class Classification (MNIST Dataset)")
    print("-" * 50)
    
    # Load MNIST dataset
    print("Loading MNIST dataset...")
    mnist = fetch_openml('mnist_784', version=1, as_frame=False)
    X, y = mnist.data, mnist.target
    
    # Convert data to float32 for faster processing
    X = X.astype('float32')
    
    # Use a smaller subset of the data (10% for training)
    print("Preparing data subset...")
    X_subset, _, y_subset, _ = train_test_split(X, y, train_size=0.1, random_state=42)
    
    # Split the subset into train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X_subset, y_subset, test_size=0.2, random_state=42
    )
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train multi-class SVM with faster parameters
    print("Training Multi-Class SVM...")
    svm = SVC(kernel='rbf', decision_function_shape='ovr', max_iter=1000, tol=1e-3)
    svm.fit(X_train_scaled, y_train)
    
    # Make predictions
    print("Making predictions...")
    y_pred = svm.predict(X_test_scaled)
    
    # Evaluate results
    results = evaluate_multiclass(y_test, y_pred)
    print("\nMulti-Class Classification Results:")
    for metric, value in results.items():
        print(f"{metric}: {value:.4f}")

if __name__ == "__main__":
    main()
