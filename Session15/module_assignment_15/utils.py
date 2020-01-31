import numpy as np
import time, math
from tqdm import tqdm_notebook as tqdm

import tensorflow as tf
import tensorflow.contrib.eager as tfe

from PIL import Image
import numpy as np
import skimage.io as io

tf.enable_eager_execution()

BATCH_SIZE = 512
MOMENTUM = 0.9
LEARNING_RATE = 0.4
WEIGHT_DECAY = 5e-4
EPOCHS =  24


IMAGE_HEIGHT = 40
IMAGE_WIDTH = 40
IMAGE_DEPTH = 3
NUM_CLASSES = 10
train_tfrecords_filename = 'Training_tf_records.tfrecords'
test_tfrecords_filename = 'Testing_tf_records.tfrecords'

