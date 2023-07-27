# -*- coding: utf-8 -*-
"""pet_recognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gqcU41x69MN_ayBV_fasssVPY331ABeH

# Importing Lib
"""

import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator

tf.__version__

"""#Training Data"""

train_datagen = ImageDataGenerator(rescale = 1./255 ,
                                   shear_range = 0.2 ,
                                   zoom_range = 0.2 ,
                                   horizontal_flip = True
                                   )
training_set = train_datagen.flow_from_directory('/content/drive/MyDrive/pet_recognition',
                                                 target_size = (64,64),
                                                 batch_size = 32,
                                                 class_mode = 'binary'
                                                 )

test_datagen = ImageDataGenerator(rescale = 1./255)
test_set = test_datagen.flow_from_directory('/content/drive/MyDrive/pet_recognition',
                                           target_size = (64, 64),
                                           batch_size = 32,
                                           class_mode = 'binary')

"""# Trainign CNN"""

cnn = tf.keras.models.Sequential()

cnn .add(tf.keras.layers.Conv2D(filters = 32,
                                kernel_size = 3,
                                activation = 'relu',
                                input_shape = [64, 64, 3]))

cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2,
                                  strides = 2))

cnn.add(tf.keras.layers.Conv2D(filters = 32,
                               kernel_size = 3,
                               activation = 'relu'))

cnn.add(tf.keras.layers.MaxPool2D(pool_size = 2,
                               strides = 2))

cnn.add(tf.keras.layers.Flatten())

cnn.add(tf.keras.layers.Dense(units = 128, activation = 'relu'))

cnn.add(tf.keras.layers.Dense(units = 1, activation = 'sigmoid'))

cnn.compile(optimizer = 'adam',
            loss = 'binary_crossentropy',
            metrics = ['accuracy'])

cnn.fit(x = training_set,
        validation_data = test_set,
        epochs = 25)

pip install Pillow

from PIL import Image
import numpy as np

test_image = Image.open('/content/predict.jpg').resize((64, 64))
test_image = np.array(test_image)
test_image = np.expand_dims(test_image, axis=0)

result = cnn.predict(test_image)
training_set.class_indices
if result [0][0] == 1:
  prediction = 'dog'
else:
  prediction = 'cat'

print(prediction)