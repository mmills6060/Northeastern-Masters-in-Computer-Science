import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import mean_absolute_error
import io  # Import the io module

# Initialize an empty list to store data for all stock symbols
all_data = []
stock_info = []
# Open the CSV file and read each row
with open('prices-split-adjusted.csv', 'r') as file:
    # Initialize a Pandas DataFrame for the entire dataset
    all_data = pd.DataFrame()
    
    # Read the first line to get column labels
    column_labels = file.readline().strip().split(',')
    
    for line in file:
        # Read each line and append it to the list
        all_data.append(line.strip().split(','))
print (all_data)    
# Filter the dataset for a specific stock symbol (you can change this)
stock_symbol = 'WLTW'
stock_data = all_data[all_data['symbol'] == stock_symbol]

# Sort the data by date
stock_data = stock_data.sort_values('date')

# Feature selection
features = ['open', 'close', 'low', 'high', 'volume']

# Preprocessing
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(stock_data[features])

# Split data into training and testing sets
train_size = int(len(scaled_data) * 0.8)
test_size = len(scaled_data) - train_size
train_data, test_data = scaled_data[0:train_size, :], scaled_data[train_size:len(scaled_data), :]

# Function to create dataset for training the model
def create_dataset(data, time_steps=1):
    X, Y = [], []
    for i in range(len(data) - time_steps - 1):
        X.append(data[i:(i + time_steps), :])
        Y.append(data[i + time_steps, 1])  # Predicting the 'close' price
    return np.array(X), np.array(Y)

# Time steps for the LSTM model
time_steps = 10

# Create the dataset
X_train, Y_train = create_dataset(train_data, time_steps)
X_test, Y_test = create_dataset(test_data, time_steps)

# Build LSTM model
model = Sequential([
    LSTM(50, input_shape=(X_train.shape[1], X_train.shape[2])),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_train, Y_train, epochs=50, batch_size=64, validation_data=(X_test, Y_test), verbose=1)

# Make predictions
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# Inverse transform the predictions
train_predict = scaler.inverse_transform(np.concatenate((np.zeros((len(train_predict), len(features)-1)), train_predict), axis=1))[:, 1]
test_predict = scaler.inverse_transform(np.concatenate((np.zeros((len(test_predict), len(features)-1)), test_predict), axis=1))[:, 1]

# Inverse transform the actual values
Y_train_inv = scaler.inverse_transform(np.concatenate((np.zeros((len(Y_train), len(features)-1)), Y_train.reshape(-1, 1)), axis=1))[:, 1]
Y_test_inv = scaler.inverse_transform(np.concatenate((np.zeros((len(Y_test), len(features)-1)), Y_test.reshape(-1, 1)), axis=1))[:, 1]

# Calculate Mean Absolute Error
train_mae = mean_absolute_error(Y_train_inv, train_predict)
test_mae = mean_absolute_error(Y_test_inv, test_predict)
print(f'Train MAE: {train_mae}')
print(f'Test MAE: {test_mae}')

# Plotting
plt.figure(figsize=(14, 7))

# Plot training data
train_dates = stock_data['date'][time_steps:len(train_predict) + time_steps]
plt.plot(train_dates, Y_train_inv, label='Actual (Training)')
plt.plot(train_dates, train_predict, label='Predicted (Training)')

# Plot testing data
test_dates = stock_data['date'][len(train_predict) + 2 * time_steps:len(train_predict) + 2 * time_steps + len(test_predict)]
plt.plot(test_dates, Y_test_inv, label='Actual (Testing)')
plt.plot(test_dates, test_predict, label='Predicted (Testing)')

plt.title(f'Stock Price Prediction for {stock_symbol}')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

