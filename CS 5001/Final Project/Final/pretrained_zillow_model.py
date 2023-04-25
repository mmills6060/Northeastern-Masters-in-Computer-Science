import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import requests
import os
from PIL import Image
import pandas as pd
from io import BytesIO
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
import pathlib
from tensorflow.keras.models import load_model

def generate_zillow_inference():
    # Load the saved model
    model = load_model("/Users/michaelmills/Saved_Models/zillow_model")

    # Load the new data
    new_data = pd.read_csv("/Users/michaelmills/Zillow_Dataset/mini-zillow.csv", names=["photo_url", "price", "beds", "baths", "sqft", "doz", "zpid"])

    batch_size = 100
    photo_arrays = []
    # Loop through each batch of rows in the DataFrame, extract the photo_url, load the image from the URL, convert it to a NumPy array, and append it to the list
    for i in range(0, len(new_data), batch_size):
        batch = new_data[i:i+batch_size]
        batch_arrays = []
        for index, row in batch.iterrows():
            response = requests.get(row['photo_url'])
            img = Image.open(BytesIO(response.content))
            photo_array = img.resize((360, 360))
            photo_array = np.array(img)
            batch_arrays.append(photo_array)
        photo_arrays.append(np.array(batch_arrays))
        print ("Loaded batch", i, "of", len(new_data))
        
    # Concatenate the list of arrays into a single NumPy array
    photo_arrays = np.concatenate(photo_arrays, axis=0)
    # Remove any columns that are not needed for prediction
    new_data = new_data.drop(['photo_url', 'zpid', 'price'], axis=1)

    # Convert the new data into a NumPy array
    new_data_array = np.array(new_data)


    # Predict on the new data
    predictions = model.predict([photo_arrays, new_data_array])
    print("Predictions:")
    # Print the predictions
    print(predictions)