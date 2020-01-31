import numpy as np
import time, math
from tqdm import tqdm_notebook as tqdm

import tensorflow as tf
import tensorflow.contrib.eager as tfe

from PIL import Image
import numpy as np
import skimage.io as io

BATCH_SIZE = 512
MOMENTUM = 0.9
LEARNING_RATE = 0.4
WEIGHT_DECAY = 5e-4
EPOCHS =  24

# from module_assignment_15.model import load_model
from module_assignment_15.data import load_data

batches_per_epoch = load_data.len_train//BATCH_SIZE *+ 1

lr_schedule = lambda t: np.interp([t], [0, (EPOCHS+1)//5, EPOCHS], [0, LEARNING_RATE, 0])[0]
global_step = tf.train.get_or_create_global_step()
lr_func = lambda: lr_schedule(global_step/batches_per_epoch)/BATCH_SIZE
opt = tf.train.MomentumOptimizer(lr_func, momentum=MOMENTUM, use_nesterov=True)
data_aug = lambda x, y: (tf.image.random_flip_left_right(tf.random_crop(x, [32, 32, 3])), y)
