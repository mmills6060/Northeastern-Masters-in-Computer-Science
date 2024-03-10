# Imports
import os
import matplotlib.pyplot as plt
from PIL import Image
import math

# Configuration
dir_with_examples = './imagecopies'
files_per_row = 3

# List the directory and perform computations
files_in_dir = os.listdir(dir_with_examples)
number_of_cols = files_per_row
number_of_rows = int(len(files_in_dir) / number_of_cols)

# Generate the subplots
fig, axs = plt.subplots(number_of_rows, number_of_cols)
fig.set_size_inches(8, 5, forward=True)

# Map each file to subplot
for i in range(0, len(files_in_dir)):
  file_name = files_in_dir[i]
  image = Image.open(f'{dir_with_examples}/{file_name}')
  row = math.floor(i / files_per_row)
  col = i % files_per_row
  axs[row, col].imshow(image)
  axs[row, col].axis('off')

# Show the plot
plt.show()
