import numpy as np
import time, math
from tqdm import tqdm_notebook as tqdm

import tensorflow as tf
import tensorflow.contrib.eager as tfe

from PIL import Image
import numpy as np
import skimage.io as io

from module_assignment_15.data import load_data
from module_assignment_15.optim_scheduler import load_optim
from module_assignment_15.model import load_model

# from load_data import *
#from .data import load_checkpoint


BATCH_SIZE = 512
MOMENTUM = 0.9
LEARNING_RATE = 0.4
WEIGHT_DECAY = 5e-4
EPOCHS =  24

t = time.time()

train_tfrecords_filename = '/content/gdrive/My Drive/EVA/tf_records_datasets_folder/Training_tf_records.tfrecords'
test_tfrecords_filename = '/content/gdrive/My Drive/EVA/tf_records_datasets_folder/Testing_tf_records.tfrecords'

model = load_model.DavidNet()

"""## Read test TFRecord data"""
test_set = load_data.fetch_tf_record_data(test_tfrecords_filename, isTraining=False).batch(BATCH_SIZE)


for epoch in range(EPOCHS):
  train_loss = test_loss = train_acc = test_acc = 0.0
  
  #### Read training TFRecords data
  train_set = load_data.fetch_tf_record_data(train_tfrecords_filename).map(load_optim.data_aug).shuffle(load_data.len_train).batch(BATCH_SIZE).prefetch(1)
  tf.keras.backend.set_learning_phase(1)

  for (x, y) in tqdm(train_set):
    with tf.GradientTape() as tape:
      loss, correct = model(x, y)

    var = model.trainable_variables
    grads = tape.gradient(loss, var)
    for g, v in zip(grads, var):
      g += v * WEIGHT_DECAY * BATCH_SIZE
    load_optim.opt.apply_gradients(zip(grads, var), global_step=load_optim.global_step)

    train_loss += loss.numpy()
    train_acc += correct.numpy()

  tf.keras.backend.set_learning_phase(0)
  for (x, y) in test_set:
    loss, correct = model(x, y)
    test_loss += loss.numpy()
    test_acc += correct.numpy()
    
  print('epoch:', epoch+1, 'lr:', load_optim.lr_schedule(epoch+1), 'train loss:', train_loss / (load_data.len_train), 'train acc:', train_acc / (load_data.len_train), 'val loss:', test_loss / (load_data.len_test), 'val acc:', test_acc / (load_data.len_test), 'time:', time.time() - t)

