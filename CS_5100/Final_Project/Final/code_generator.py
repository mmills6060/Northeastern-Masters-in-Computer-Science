
import logging
import time
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
# Redirect stderr to /dev/null (Linux/Unix) or a log file
sys.stderr = open(os.devnull, 'w')
import tensorflow_datasets as tfds
import tensorflow as tf
import tensorflow_text



model = tf.saved_model.load('code_generator')

response = model('Print merry christmas in the terminal').numpy()
print(response)
