import os
import time
import math
import random
import datetime
from pathlib import Path

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"  # reduce the amount of console output from TF
import tensorflow as tf

from transformers import *
from datasets import load_dataset

logging.set_verbosity_warning()
logging.set_verbosity_error()

import logging

print('TF version',tf.__version__)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU'))) # check GPU available


def model_fn(x, y, z):
    return tf.reduce_sum(x + y * z)