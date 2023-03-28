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

def generate_flower_inference():
    # Define the class names
    class_names = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

    # Reload a fresh Keras model from the saved model in directory
    new_model = tf.keras.models.load_model("C:\\Users\\Michael Mills\\Documents\\Final Project\\Saved_Models\\flower_model")

    # Check its architecture
    new_model.summary()

    # Preprocess the input image
    def preprocess_image(image_path):
        img = image.load_img(image_path, target_size=(180, 180))
        img_array = image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis
        return img_array

    # Make a prediction using the loaded model
    def predict_image(image_path, model):
        img_array = preprocess_image(image_path)
        prediction = model.predict(img_array)
        return prediction

    # Specify the path to the input image
    image_path = "C:\\Users\\Michael Mills\\Documents\\Final Project\\Photos\\Flower_Test_Photo\\test_photo.jpg"

    # Make a prediction using the loaded model
    prediction = predict_image(image_path, new_model)

    # Print the predicted class name and the corresponding probability
    predicted_class_index = np.argmax(prediction)
    predicted_class_name = class_names[predicted_class_index]
    print("Predicted class:", predicted_class_name)
    print("Probability:", prediction[0][predicted_class_index])


def main():
    generate_flower_inference()

if __name__ == "__main__":
    main()
