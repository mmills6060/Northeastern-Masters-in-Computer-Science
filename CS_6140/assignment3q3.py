import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from typing import List, Tuple
import seaborn as sns

class SimpleRNN:
    def __init__(self, input_size: int, hidden_size: int, output_size: int):
        """
        Initialize RNN parameters
        Args:
            input_size: dimension of input features
            hidden_size: dimension of hidden state (memory size)
            output_size: dimension of output
        """
        # Initialize weights with random values
        self.Wxh = np.random.randn(hidden_size, input_size) * 0.01
        self.Whh = np.random.randn(hidden_size, hidden_size) * 0.01
        self.Why = np.random.randn(output_size, hidden_size) * 0.01
        
        # Initialize biases
        self.bh = np.zeros((hidden_size, 1))
        self.by = np.zeros((output_size, 1))
        
        self.hidden_size = hidden_size
        
    def forward(self, inputs: np.ndarray) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        """
        Forward pass of the RNN
        Args:
            inputs: sequence of input vectors
        Returns:
            hidden_states: list of hidden states
            outputs: list of outputs
        """
        h = np.zeros((self.hidden_size, 1))  # Initial hidden state
        hidden_states, outputs = [], []
        
        # Forward pass for each time step
        for x in inputs:
            x = x.reshape(-1, 1)
            h = np.tanh(np.dot(self.Wxh, x) + np.dot(self.Whh, h) + self.bh)
            y = np.dot(self.Why, h) + self.by
            hidden_states.append(h)
            outputs.append(y)
            
        return hidden_states, outputs
    
    def train(self, X: np.ndarray, y: np.ndarray, learning_rate: float = 0.01, epochs: int = 100) -> List[float]:
        """
        Train the RNN using backpropagation through time (BPTT)
        Args:
            X: input sequences
            y: target sequences
            learning_rate: learning rate for gradient descent
            epochs: number of training epochs
        Returns:
            losses: list of losses during training
        """
        losses = []
        
        for epoch in range(epochs):
            total_loss = 0
            
            for i in range(len(X)):
                # Forward pass
                hidden_states, outputs = self.forward(X[i])
                
                # Compute loss
                loss = np.mean((np.array(outputs) - y[i].reshape(-1, 1)) ** 2)
                total_loss += loss
                
                # Backward pass
                dWxh = np.zeros_like(self.Wxh)
                dWhh = np.zeros_like(self.Whh)
                dWhy = np.zeros_like(self.Why)
                dbh = np.zeros_like(self.bh)
                dby = np.zeros_like(self.by)
                dhnext = np.zeros((self.hidden_size, 1))
                
                # Backpropagate through time
                for t in reversed(range(len(X[i]))):
                    dy = 2 * (outputs[t] - y[i][t].reshape(-1, 1))
                    dWhy += np.dot(dy, hidden_states[t].T)
                    dby += dy
                    
                    dh = np.dot(self.Why.T, dy) + dhnext
                    dhraw = (1 - hidden_states[t] ** 2) * dh
                    dbh += dhraw
                    dWxh += np.dot(dhraw, X[i][t].reshape(1, -1))
                    dWhh += np.dot(dhraw, hidden_states[t-1].T) if t > 0 else np.dot(dhraw, np.zeros((self.hidden_size, 1)).T)
                    dhnext = np.dot(self.Whh.T, dhraw)
                
                # Update weights using gradient descent
                self.Wxh -= learning_rate * dWxh
                self.Whh -= learning_rate * dWhh
                self.Why -= learning_rate * dWhy
                self.bh -= learning_rate * dbh
                self.by -= learning_rate * dby
            
            losses.append(total_loss / len(X))
            
            if epoch % 10 == 0:
                print(f'Epoch {epoch}, Loss: {total_loss/len(X)}')
                
        return losses

def generate_long_term_dependency_data(n_samples: int, sequence_length: int, dependency_lag: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate time series data with long-term dependencies
    Args:
        n_samples: number of sequences to generate
        sequence_length: length of each sequence
        dependency_lag: how far back the dependency goes
    Returns:
        X: input sequences
        y: target sequences
    """
    X = np.zeros((n_samples, sequence_length))
    y = np.zeros((n_samples, sequence_length))
    
    for i in range(n_samples):
        # Generate random binary signal
        signal = np.random.choice([0, 1], size=sequence_length)
        
        # Create dependency: if signal[t-dependency_lag] == 1, add a sine wave component
        for t in range(dependency_lag, sequence_length):
            if signal[t-dependency_lag] == 1:
                signal[t] += 0.5 * np.sin(t/5)
        
        X[i] = signal
        y[i] = np.roll(signal, -1)  # Target is next time step
    
    return X, y

def plot_results(true_values: np.ndarray, predicted_values: np.ndarray, title: str):
    """
    Plot true vs predicted values
    """
    plt.figure(figsize=(12, 6))
    plt.plot(true_values, label='True Values', color='blue')
    plt.plot(predicted_values, label='Predicted Values', color='red', linestyle='--')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Generate data
    n_samples = 100
    sequence_length = 20
    dependency_lag = 5
    X, y = generate_long_term_dependency_data(n_samples, sequence_length, dependency_lag)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Visualize sample data
    plt.figure(figsize=(12, 6))
    plt.plot(X[0], label='Sample Sequence')
    plt.title('Example of Generated Time Series with Long-term Dependencies')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Test different memory sizes
    memory_sizes = [2, 5]
    results = {}
    
    for memory_size in memory_sizes:
        print(f"\nTraining RNN with memory size {memory_size}")
        rnn = SimpleRNN(input_size=1, hidden_size=memory_size, output_size=1)
        
        # Train the model
        losses = rnn.train(X_train, y_train, learning_rate=0.01, epochs=100)
        
        # Evaluate on test set
        test_predictions = []
        for seq in X_test:
            _, outputs = rnn.forward(seq)
            test_predictions.append([o[0][0] for o in outputs])
        
        # Calculate MSE
        mse = np.mean((np.array(test_predictions) - y_test) ** 2)
        results[memory_size] = {
            'mse': mse,
            'predictions': test_predictions
        }
        
        # Plot training loss
        plt.figure(figsize=(10, 5))
        plt.plot(losses)
        plt.title(f'Training Loss (Memory Size = {memory_size})')
        plt.xlabel('Epoch')
        plt.ylabel('MSE Loss')
        plt.grid(True)
        plt.show()
        
        # Plot predictions vs ground truth for a sample sequence
        sample_idx = 0
        plot_results(y_test[sample_idx], test_predictions[sample_idx], 
                    f'Predictions vs Ground Truth (Memory Size = {memory_size})')
    
    # Print results table
    print("\nResults Summary:")
    print("Memory Size | Test MSE")
    print("----------------------")
    for size, result in results.items():
        print(f"{size:^10} | {result['mse']:.6f}")

if __name__ == "__main__":
    main()
