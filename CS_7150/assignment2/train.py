# Imports
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Data configuration
training_set_folder = './imagecopies/fruits-360_dataset/fruits-360/Training'
test_set_folder     = './imagecopies/fruits-360_dataset/fruits-360/Test'


# Model configuration
batch_size = 25
img_width, img_height, img_num_channels = 25, 25, 3
loss_function = sparse_categorical_crossentropy
no_classes = 150
no_epochs = 200
optimizer = Adam()
verbosity = 1

# Determine shape of the data
input_shape = (img_width, img_height, img_num_channels)

# Create a generator
train_datagen = ImageDataGenerator(
  rescale=1./255
)

train_datagen = train_datagen.flow_from_directory(
        training_set_folder,
        save_to_dir='./adapted-images',
        save_format='jpeg',
        batch_size=batch_size,
        target_size=(25, 25),
        class_mode='sparse')

# Create the model
model = Sequential()
model.add(Conv2D(16, kernel_size=(5, 5), activation='relu', input_shape=input_shape))
model.add(Conv2D(32, kernel_size=(5, 5), activation='relu'))
model.add(Conv2D(64, kernel_size=(5, 5), activation='relu'))
model.add(Conv2D(128, kernel_size=(5, 5), activation='relu'))

# take the output from the previous layer which is multi dimensional, and turn it into a single dimension
model.add(Flatten())
# a dense layer takes all of the extracted features and maps them to the output nodes. This is the classification part
model.add(Dense(16, activation='relu'))
# add another layer with a node for each class. This will essentially give a probability of the image being in each class
model.add(Dense(no_classes, activation='softmax'))



# Display a model summary
model.summary()

# Compile the model
model.compile(loss=loss_function,
              optimizer=optimizer,
              metrics=['accuracy'])

# Start training
model.fit(
        train_datagen,
        epochs=no_epochs,
        shuffle=False)






