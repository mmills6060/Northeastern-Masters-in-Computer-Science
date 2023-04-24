import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import os
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
import pathlib
from tensorflow.keras.models import load_model

def generate_tennis_inference(model, class_names):
    
    # Predict on new data
    tennis_path = "CS 5001/Final Project/Final/Assets/Test_photos/Tennis/agassi.jpeg"

    img = tf.keras.utils.load_img(
        tennis_path, target_size=(360, 360)
    )
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

def main():
    # Load the model
    model_path = "/Users/michaelmills/Saved_Models/tennis_model"
    model = load_model(model_path)

    # Define the class names
    class_names = ["Agassi", "Federer"]

    # Generate the flower inference
    generate_tennis_inference(model, class_names)

if __name__ == "__main__":
    main()
