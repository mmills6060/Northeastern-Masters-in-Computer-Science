import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
import os
import platform
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image
import pathlib
from tensorflow.keras.models import load_model

def tennis_train_model(epochs, image_taget_size, validation_split):
    
    if platform.system() == "Windows":
        data_dir = pathlib.Path("CS 5001/Final Project/Final/Assets/Tennis Dataset")
    else:
        data_dir = pathlib.Path("CS 5001/Final Project/Final/Assets/Tennis Dataset")
    

    # tell me how many images there are 
    image_count = len(list(data_dir.glob('*/*.jpg')))
    print(image_count)

    # here are some roses
    roses = list(data_dir.glob('Agassi/*'))
    PIL.Image.open(str(roses[0]))
    PIL.Image.open(str(roses[1]))


    # here are some tupips
    tulips = list(data_dir.glob('Federer/*'))
    PIL.Image.open(str(tulips[0]))
    PIL.Image.open(str(tulips[1]))

    # Define some parameters for the loader
    batch_size = 32
    img_height = image_taget_size
    img_width = image_taget_size

    # create a validation split for the model. Use 80% of the images for training and 20% for validation
    train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=validation_split,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

    # create validation and use 20%
    val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=validation_split,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

    # print some of the class names 
    class_names = train_ds.class_names
    print(class_names)


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


    # determine the operating system and set the directory path accordingly
    if platform.system() == "Windows":
        directory = "C:\\Users\\Michael Mills\\Documents\\Final Project\\Saved_Models\\"
    else:
        directory = os.path.join(os.path.expanduser("~"), "Saved_Models")

    # check if directory already exists
    if not os.path.exists(directory):
        # create directory
        os.makedirs(directory)
        print(f"Directory {directory} created successfully.")
    else:
        print(f"Directory {directory} already exists.")

    # create a simple Keras model
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(10, input_shape=(784,)))
    model.add(keras.layers.Activation("softmax"))

    # compile the model
    model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

    # fit the model on a dummy dataset
    X = [[1.0] * 784] * 1000
    y = [[1.0] + [0.0] * 9] * 1000
    model.fit(X, y, epochs=10, batch_size=32)

    # save the entire model as a SavedModel
    model.save(os.path.join(directory, "flower_model"))
    


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




    # Another technique to reduce overfitting is to introduce dropout regularization to the network.

    # When you apply dropout to a layer, it randomly drops out (by setting the activation to zero) a number of output units from the layer during the training process. 
    # Dropout takes a fractional number as its input value, in the form such as 0.1, 0.2, 0.4, etc. This means dropping out 10%, 20% or 40% of the output units randomly from the applied layer.
    # Create a new neural network with tf.keras.layers.Dropout before training it using the augmented images:
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


    checkpoint_path = "C:\\Users\\Michael Mills\\Github Repositories\\Northeastern-Masters-in-Computer-Science-4\\CS 5001\\Final Project\\Tennis\\Tensorflow_Test\\training_1\\cp.ckpt"
    checkpoint_dir = os.path.dirname(checkpoint_path)

    # Create a callback that saves the model's weights
    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                    save_weights_only=True,
                                                    verbose=1)

    # Compile and train the model
    model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])
    model.summary()
    epochs = epochs
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

    model.save("C:\\Users\\Michael Mills\\Documents\\Final Project\\Saved_Models\\tennis_model")

def main():
    tennis_train_model()

if __name__ == "__main__":
    main()
