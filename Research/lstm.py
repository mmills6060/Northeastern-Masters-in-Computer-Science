from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam
from keras.utils import plot_model

# Define the LSTM model configuration
batch_size = 32
epochs = 20
input_shape = (10, 5)  # Example: 10 time steps, 5 features

# Build the LSTM model
model = Sequential()

# Add an LSTM layer
model.add(LSTM(units=64, input_shape=input_shape, return_sequences=False))

# Add a Dense layer with ReLU activation
model.add(Dense(units=32, activation='relu'))

# Add the output layer (assuming a single output)
model.add(Dense(units=1))

# Compile the model with the ADAM optimizer and Mean Squared Error loss function
model.compile(optimizer=Adam(), loss='mean_squared_error')

# Summary of the model architecture
model.summary()

# Save the model in the native Keras format
model.save('lstm_model.keras')

# Save the model plot
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

