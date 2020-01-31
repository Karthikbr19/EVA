import numpy as np
import time, math
from tqdm import tqdm_notebook as tqdm

import tensorflow as tf
import tensorflow.contrib.eager as tfe

from PIL import Image
import numpy as np
import skimage.io as io


IMAGE_HEIGHT = 40
IMAGE_WIDTH = 40
IMAGE_DEPTH = 3
NUM_CLASSES = 10

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def convert_data_to_tf(data, labels, tfrecords_filename):
  with tf.python_io.TFRecordWriter(tfrecords_filename) as record_writer:
    num_entries_in_batch = len(labels)
    for i in range(num_entries_in_batch):
      example = tf.train.Example(features=tf.train.Features(
        feature={
          'image': _bytes_feature(data[i].tobytes()),
          'label': _int64_feature(labels[i])
        }))
      record_writer.write(example.SerializeToString())

def get_each_record(serialized_example, isTraining = True):
  features = tf.parse_single_example(
    serialized_example,
    features={
      'image': tf.FixedLenFeature([], tf.string),
      'label': tf.FixedLenFeature([], tf.int64),
    })
  
  image = features['image']
  image = tf.decode_raw(image, tf.float32)

  if(isTraining):
    image = tf.reshape(image, [IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_DEPTH])
  else:
    image = tf.reshape(image, [32, 32, IMAGE_DEPTH])
  
  label = tf.cast(features['label'], tf.int64)
  return image, label

def fetch_tf_record_data(file_name, isTraining = True):
  dataset = tf.data.TFRecordDataset(filenames=file_name)
  dataset = dataset.map(lambda x: get_each_record(x, isTraining))
  return dataset      


def sample_func():
  print("asdasdsa")


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
len_train, len_test = len(x_train), len(x_test)
y_train = y_train.astype('int64').reshape(len_train)
y_test = y_test.astype('int64').reshape(len_test)

train_mean = np.mean(x_train, axis=(0,1,2))
train_std = np.std(x_train, axis=(0,1,2))

normalize = lambda x: ((x - train_mean) / train_std).astype('float32') # todo: check here
pad4 = lambda x: np.pad(x, [(0, 0), (4, 4), (4, 4), (0, 0)], mode='reflect')

x_train = normalize(pad4(x_train))
x_test = normalize(x_test)
#return x_train,x_test

