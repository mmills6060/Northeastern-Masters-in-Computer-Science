import requests
import json
import os
import pandas as pd
import tensorflow as tf


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
            estimate_listing_price()
        elif choice == "2":
            refresh_dataset()
        elif choice == "3":
            print("Goodbye!")
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
        print("Refreshing dataset...")
def estimate_listing_price():
    # Implementation of estimating listing 
    while True:
        # Print menu options
        print("\nWhat would you like to do?")
        print("1. Estimate listing ")
        print("2. Refresh dataset")
        print("3. Back")
        # Get user input
        choice = input("Enter the number of your choice: ")
    
        # Perform the selected action
        if choice == "1":
            estimate_listing_price()
        elif choice == "2":
            refresh_dataset()
        elif choice == "3":
            print("Goodbye!")
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
        ("Estimating listing price...")
def delete_dataset():
    pass    
while True:
    # Print menu options
    print("\nWhat would you like to do?")
    print("1. Estimate listing ")
    print("2. Refresh dataset")
    print ("3. Delete dataset")
    print("4. Quit")
    
    # Get user input
    choice = input("Enter the number of your choice: ")
    
    # Perform the selected action
    if choice == "1":
        estimate_listing_price()
    elif choice == "2":
        refresh_dataset()
    elif choice == "3":
        delete_dataset()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")
