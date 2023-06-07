import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import os
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
import pathlib
import pandas as pd
from PIL import Image
from io import BytesIO
import requests
import time

# Load CSV file into a Pandas DataFrame
data = pd.read_csv("C:\\Users\\Michael Mills\\Documents\\Final Project\\Datasets\\zillow.csv", names=["photo_url", "price", "beds", "baths", "sqft", "doz", "zpid"])

# Create an empty list to store arrays of photo arrays
photo_arrays = []

# Set batch size for loading images
batch_size = 100

# Calculate number of batches
num_batches = len(data) // batch_size
if len(data) % batch_size != 0:
    num_batches += 1

# Loop through each batch of rows in the DataFrame, extract the photo_url, load the image from the URL, convert it to a NumPy array, and append it to the list
for i in range(0, num_batches * batch_size, batch_size):
    batch = data[i:i+batch_size]
    batch_arrays = []
    for index, row in batch.iterrows():
        try:
            response = requests.get(row['photo_url'])
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
        img = Image.open(BytesIO(response.content))
        photo_array = img.resize((224, 224))
        photo_array = np.array(img)
        batch_arrays.append(photo_array)
        print ("Added image", index, "of", len(data), "to the dataset")
    photo_arrays.append(np.array(batch_arrays))
    
# Concatenate the list of arrays into a single NumPy array
photo_arrays = np.concatenate(photo_arrays, axis=0)

# Remove the 'photo_url' and 'price' and 'zpid' columns from the DataFrame to create the features DataFrame
data_features = data.drop(['photo_url', 'price', 'zpid'], axis=1)

# Convert the features DataFrame into a NumPy array
data_features = np.array(data_features)

# Convert the 'price' column into a NumPy array to use as labels
data_labels = np.array(data['price'])

# Define input layers for photo arrays and data features
photo_input = layers.Input(shape=(446, 596, 3), name='photo_input')
data_input = layers.Input(shape=(data_features.shape[1],), name='data_input')
# Process the photo input with convolutional layers
photo_conv = layers.Conv2D(32, (3, 3), activation='relu')(photo_input)
photo_conv = layers.MaxPooling2D((2, 2))(photo_conv)
photo_conv = layers.Flatten()(photo_conv)

# Concatenate the processed photo input with the data input
concatenated = layers.concatenate([photo_conv, data_input])

# Process the concatenated input with dense layers
dense = layers.Dense(64, activation='relu')(concatenated)
dense = layers.Dense(32, activation='relu')(dense)

# Output layer
output = layers.Dense(1, activation='linear')(dense)

# Define the model
model = models.Model(inputs=[photo_input, data_input], outputs=output)

# Compile the model
model.compile(loss='mse', optimizer='adam')

# Train the model using both the photo arrays and data features
model.fit([photo_arrays, data_features], data_labels, epochs=10)

# Save the entire model as a SavedModel.

model.save("C:\\Users\\Michael Mills\\Documents\\Final Project\\Saved_Models\\zillow_model_photo_and_data")

print ("Model saved")