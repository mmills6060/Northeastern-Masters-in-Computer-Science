
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



model = tf.saved_model.load('translator')

response1 = model('este é o primeiro livro que eu fiz.').numpy()
print(response1)
response2 = model('este é o primeiro livro que eu fiz.').numpy()
print(response2)

response3 = model('este é o primeiro livro que eu fiz.').numpy()
print(response3)

response4 = model('este é o primeiro livro que eu fiz.').numpy()
print(response4)

response5 = model('este é o primeiro livro que eu fiz.').numpy()
print(response5)