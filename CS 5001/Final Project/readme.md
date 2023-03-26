# Convolutional neural network
# Transfer Learning - applying the learnings from a previous training session to a new session
# Inception model - when we feed in an image at each layer it will perform a series of 
# operations on that data until it outputs a label and classification percentage. 
# Each layer is a different set of abstractions. In the first layers, it basically taught itself edge 
 # detection
 # Transfer learning will basically add a representation of darth vader to its repository of knowledge
 

 # Fatkun Batch Download Image to download all pictures on google images    


# Overfitting
# When there are a small number of training examples, the model sometimes learns from noises or unwanted details from training examples—to an extent that it negatively impacts the performance of the model on new examples. 
# This phenomenon is known as overfitting. It means that the model will have a difficult time generalizing on a new dataset.



# Steps

1. Get tensorflow to work with a provided dataset
2. Do the same thing but provide my own dataset
3. Write a script that will pull data of 100 listings from zillow api (Photo, listing price) and download to directory on computer. 
4. Rather than classification, use the "regression" functionality with tensorflow to assign an integer to each individual photo. Maybe increase number of listings to 1000 or something. Train machine learning model based on 1000 listings. (3,389 total listings in NYC)
6. Integrate other variables from the Zillow API such as Bed, Bath, Location, etc and train a new model with additional variables. (more than one input?) Is the model more accurate?
5. Create functionality that will check for new listings every hour. Roughly 173 new listings per day. 7 listings per hour. Retrain model with new listings.
6. Create functionality that will keep track of the listing, look to see if it was rented, record rented price.
7. Change algorithm to learn and predict the actual price the apartment was "rented" for as opposed to what it was "listed" for. 

# Problems

Batch download worked for a litte bit, but google images would only display 100 photos. 
Changed Epochs to 25 and that dramatically increased the accuracy of the machine learning algorithm.
Correctly prediccted Agassi with a 99.76 percent confidence.