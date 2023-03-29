# Michael Arthur Mills
# March 24, 2023
# This is the second test that uses the same concepts of learning, but uses my own dataset. 


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
import pandas as pd


# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)

data_dir = pathlib.Path("C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow")
csv_dir = pathlib.Path("C:\\Users\\Michael Mills\\Documents\\Final Project\\Datasets\\zillow.csv")

zillow_train = pd.read_csv(csv_dir, names= ["listing_price", "bathrooms", "bedrooms", "living_area", "days_on_zillow", "zpid"])
zillow_train.head()
print(zillow_train.head())
zillow_features = zillow_train.copy()

#seperate labels and features for training
zillow_labels = zillow_features.pop('listing_price')
zillow_features = zillow_features.astype(int)

# Pack the features into a single numpy array
zillow_features = np.array(zillow_features)
print(zillow_features)



# Make a regression model predict the price
zillow_model = tf.keras.Sequential([
  layers.Dense(64),
  layers.Dense(1)
])

zillow_model.compile(loss = tf.keras.losses.MeanSquaredError(),
                      optimizer = tf.keras.optimizers.Adam())

# train the model by passing the features and labels to model.fit
zillow_model.fit(zillow_features, zillow_labels, epochs=100)

# create a sample input to make a prediction on
sample_input = np.array([[1, 2, 886, 0, 2121729151]])

# make a prediction based on the input using the trained model
predicted_price = zillow_model.predict(sample_input)

# print the predicted price
print("The predicted price for the given input is: $", predicted_price[0][0])


# tell me how many images there are 
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

# here are some cheap apartments
roses = list(data_dir.glob('1000/*'))
PIL.Image.open(str(roses[0]))
PIL.Image.open(str(roses[1]))


# here are some expensive apartments
tulips = list(data_dir.glob('10000/*'))
PIL.Image.open(str(tulips[0]))
PIL.Image.open(str(tulips[1]))

# Define some parameters for the loader
batch_size = 32
img_height = 360
img_width = 360

# create a validation split for the model. Use 80% of the images for training and 20% for validation
train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# create validation and use 20%
val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

# print some of the class names 
class_names = train_ds.class_names
print(class_names)


# here are the first nine images from the training dataset
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
  for i in range(9):
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(images[i].numpy().astype("uint8"))
    plt.title(class_names[labels[i]])
    plt.axis("off")

# manually iterate over the dataset and retrieve batches of images
for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)
  break

# The image_batch is a tensor of the shape (32, 180, 180, 3). 
# This is a batch of 32 images of shape 180x180x3 (the last dimension refers to color channels RGB). 
# The label_batch is a tensor of the shape (32,), these are corresponding labels to the 32 images.

# configure dataset for performance
# dataset.cache = keeps the images in memory after they're loaded off disk during the first epoch. 
# This will ensure the dataset does not become a bottleneck while training the model. 
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


# Standardize the data. The RGB channel values are in the [0, 255] range. This is not ideal for a neural network; in general you should seek to make your input values small.
# Here, you will standardize values to be in the [0, 1] range by using tf.keras.layers.Rescaling:

normalization_layer = layers.Rescaling(1./255)
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]
# Notice the pixel values are now in `[0,1]`.
print(np.min(first_image), np.max(first_image))



# Create the model

def create_model():
  num_classes = len(class_names)

  model = Sequential([
    layers.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes)
  ])


  # Compile the model
  model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
  return model

# Create a basic model instance
model = create_model()

# Model Summary
model.summary()


# Train the model
epochs=1
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs
)

# Visualize training results
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()


# Data Augmentation
# Overfitting generally occurs when there are a small number of training examples. 
# Data augmentation takes the approach of generating additional training data from your existing examples by augmenting them using random transformations that yield believable-looking images. 
# This helps expose the model to more aspects of the data and generalize better.

data_augmentation = keras.Sequential(
  [
    layers.RandomFlip("horizontal",
                      input_shape=(img_height,
                                  img_width,
                                  3)),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1),
  ]
)

# Visualize a few augmented examples by applying data augmentation to the same image several times
plt.figure(figsize=(10, 10))
for images, _ in train_ds.take(1):
  for i in range(9):
    augmented_images = data_augmentation(images)
    ax = plt.subplot(3, 3, i + 1)
    plt.imshow(augmented_images[0].numpy().astype("uint8"))
    plt.axis("off")


# Another technique to reduce overfitting is to introduce dropout regularization to the network.

# When you apply dropout to a layer, it randomly drops out (by setting the activation to zero) a number of output units from the layer during the training process. 
# Dropout takes a fractional number as its input value, in the form such as 0.1, 0.2, 0.4, etc. This means dropping out 10%, 20% or 40% of the output units randomly from the applied layer.
# Create a new neural network with tf.keras.layers.Dropout before training it using the augmented images:
def apply_dropoutlayer():
  model = Sequential([
    data_augmentation,
    layers.Rescaling(1./255),
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Dropout(0.2),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, name="outputs")
  ])


checkpoint_path = "C:\\Users\\Michael Mills\\Github Repositories\\Northeastern-Masters-in-Computer-Science-4\\CS 5001\\Final Project\\Tensorflow_Test\\training_1\\cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# Compile and train the model. This is the one that matters
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.summary()
epochs = 2
history = model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=epochs,
  callbacks=[cp_callback]
)

# specify the directory path to create
directory = "C:\\Users\\Michael Mills\\Documents\\Final Project\\Saved_Models\\"

# check if directory already exists
if not os.path.exists(directory):
    # create directory
    os.makedirs(directory)
    print(f"Directory {directory} created successfully.")
else:
    print(f"Directory {directory} already exists.")
# Save the entire model as a SavedModel.

model.save("C:\\Users\\Michael Mills\\Documents\\Final Project\\Saved_Models\\zillow_model")

# Create a basic model instance
model = create_model()

# Evaluate the model
loss, acc = model.evaluate(val_ds, verbose=2)
print("Untrained model, accuracy: {:5.2f}%".format(100 * acc))

# Loads the weights
model.load_weights(checkpoint_path)

# Re-evaluate the model
loss, acc = model.evaluate(val_ds, verbose=2)
print("Restored model, accuracy: {:5.2f}%".format(100 * acc))

# Visualize training results
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()



# Predict on new data
Apartment_dir = "C:\\Users\\Michael Mills\\Pictures\\Final Project\\Zillow\\5000\\4af2e0367dcd1d246ab83162d25e001e-p_e.jpg"

img = PIL.Image.open(Apartment_dir).resize((img_height, img_width))
img_array = image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely is listed at ${} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)


