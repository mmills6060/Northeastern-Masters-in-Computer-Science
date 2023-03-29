import requests
import json
import os
import pandas as pd
import tensorflow as tf
import subprocess
from pretrained_flower_model import generate_flower_inference
from pretrained_tennis_model import generate_tennis_inference
from pretrained_zillow_model import generate_zillow_inference
from flowers_train_model import flowers_train_model
from tennis_train_model import tennis_train_model
from zillow_train_model import zillow_train_model

def refresh_dataset():
    # Implementation of refreshing dataset
    while True:
        # Print menu options
        print("\nWhat would you like to do?")
        print("1. How many listings would you like to add to your dataset?")
        print("2. Refresh dataset")
        print("3. Back")
        # Get user input
        choice = input("Enter the number of your choice: ")
    
        # Perform the selected action
        if choice == "1":
            pass
        elif choice == "2":
            refresh_dataset()
        elif choice == "3":
            print("Goodbye!")
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
        print("Refreshing dataset...")
def generate_inference():
    # Implementation of generating an inference 
    while True:
        # Print menu options
        print("\nWhich topic would you like to generate an inference for?")
        print("1. Flowers")
        print("2. Tennis")
        print("3. Zillow")
        print("4. Back")
        # Get user input
        choice = input("Enter the number of your choice: ")
    
        # Perform the selected action
        if choice == "1":
            generate_flower_inference()
            main()         
        elif choice == "2":
            generate_tennis_inference()
            main()
        elif choice == "3":
            generate_zillow_inference()
            main()
        elif choice == "4":
            main()
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
        ("Estimating listing price...")
def delete_dataset():
    pass
def train_model():
        # implementation of training a model
    while True:
        # Print menu options
        print("\nWhich model would you like to train?")
        print("1. Flowers")
        print("2. Tennis")
        print("3. Zillow")
        print("4. Back")
        # Get user input
        choice = input("Enter the number of your choice: ")
    
        # Perform the selected action
        if choice == "1":
            print("\nEpochs: Press enter for default(2)")
            epochs = input("Enter the number of epochs for this model: ")
            if epochs == "":
                epochs = 2
            else:
                epochs = int(epochs)
            print("\nImage Target Size: Press enter for default(180)")
            image_target_size = (input("Enter the image target size (ie. 180): "))
            if image_target_size == "":
                image_target_size = 180
            else:
                image_target_size = int(image_target_size)
            print("\nValidation Split: Press enter for default(180)")
            validation_split = (input("Enter the percent of the dataset you would like to use for training (and the rest for validation) (ie. .2) for this model: "))
            if validation_split == "":
                validation_split = 0.2
            else:
                validation_split = float(validation_split)
            flowers_train_model(epochs, image_target_size, validation_split)
            print("Training completed successfully")
            main()
        elif choice == "2":
            print("\nEpochs: Press enter for default(2)")
            epochs = input("Enter the number of epochs for this model: ")
            if epochs == "":
                epochs = 2
            else:
                epochs = int(epochs)
            print("\nImage Target Size: Press enter for default(180)")
            image_target_size = (input("Enter the image target size (ie. 180): "))
            if image_target_size == "":
                image_target_size = 180
            else:
                image_target_size = int(image_target_size)
            print("\nValidation Split: Press enter for default(180)")
            validation_split = (input("Enter the percent of the dataset you would like to use for training (and the rest for validation) (ie. .2) for this model: "))
            if validation_split == "":
                validation_split = 0.2
            else:
                validation_split = float(validation_split)
            tennis_train_model(epochs, image_target_size, validation_split)
            print("Training completed successfully")
            main()
        elif choice == "3":
            print("\nEpochs: Press enter for default(2)")
            epochs = input("Enter the number of epochs for this model: ")
            if epochs == "":
                epochs = 2
            else:
                epochs = int(epochs)
            print("\nImage Target Size: Press enter for default(180)")
            image_target_size = (input("Enter the image target size (ie. 180): "))
            if image_target_size == "":
                image_target_size = 180
            else:
                image_target_size = int(image_target_size)
            print("\nValidation Split: Press enter for default(180)")
            validation_split = (input("Enter the percent of the dataset you would like to use for training (and the rest for validation) (ie. .2) for this model: "))
            if validation_split == "":
                validation_split = 0.2
            else:
                validation_split = float(validation_split)
            zillow_train_model(epochs, image_target_size, validation_split)
            print("Training completed successfully")
            main()
        elif choice == "4":
            main()
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
        ("Estimating listing price...")
def main():
    while True:
        # Print menu options
        print("\nWhat would you like to do?")
        print("1. Generate Inference")
        print("2. Train Model")
        print("3. Refresh dataset")
        print ("4. Delete dataset")
        print("5. Quit")
        
        # Get user input
        choice = input("Enter the number of your choice: ")
        
        # Perform the selected action
        if choice == "1":
            generate_inference()
        elif choice == "2":
            train_model()
        elif choice == "3":
            refresh_dataset()
        elif choice == "4":
            delete_dataset()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
    
