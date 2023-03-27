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
3. change the directory in which the saved ML models are stored. Git cant hold more than 100mb. 
4. See if I can classify images into different levels of quality
5. Rather than classification, look to see if I can create a quantifiable value that characterises the quality
6. Turn the number value into an actual price
7. Integrate other variables from the Zillow API such as Bed, Bath, Location, Etc. 
8. Create functionality that will automatically import data from listings that have just come on the market

# Problems

Batch download worked for a litte bit, but google images would only display 100 photos. 
Changed Epochs to 25 and that dramatically increased the accuracy of the machine learning algorithm.
Correctly prediccted Agassi with a 99.76 percent confidence.
i included a timer but it didn't seem to do anything
zillow API only returns 800 listings. 
training just photos only rsulted in about 30% confidence