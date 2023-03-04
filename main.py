# organize dataset into a useful structure
from os import makedirs
from os import listdir
from shutil import copyfile
from random import seed
from random import random
import numpy

# baseline model for the dogs vs cats dataset
import sys
from matplotlib import pyplot
from keras.utils import load_img
from keras.utils import img_to_array
from os import listdir
from numpy import append
from numpy import asarray
from numpy import save
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator

# # create directories
# dataset_home = 'dataset_dogs_vs_cats/'
# subdirs = ['train/', 'test/']
#
# for subdir in subdirs:
#     # create label subdirectories
#     # labeldirs = ['dogs/', 'cats/']
#     for labldir in labeldirs:
#         newdir = dataset_home + subdir + labldir
#         makedirs(newdir, exist_ok=True)
#
# # seed random number generator
# seed(1)
#
# # define ratio of pictures to use for validation
# val_ratio = 0.25
#
# copy training dataset images into subdirectories
# src_directory = 'train/'
# for file in listdir(src_directory):
#     src = src_directory + '/' + file
#     dst_dir = 'train/'
#     if random() < val_ratio:
#         dst_dir = 'test/'
#     if file.startswith('cat'):
#         dst = dataset_home + dst_dir + 'cats/'  + file
#         copyfile(src, dst)
#     if file.startswith('dog'):
#         dst = dataset_home + dst_dir + 'dogs/'  + file
#         copyfile(src, dst)

# # define location of dataset
# folder = 'dataset/train/'
# photos, labels = list(), list()
# # enumerate files in the directory
# for file in listdir(folder):
#     # determine class
#     output = 1.0
#     if file.startswith('Panda'):
#         output = 1.0
#     # load image
#     photo = load_img(folder + file, target_size=(200, 200))
#     print(folder + file)
#     # convert to numpy array
#     photo = img_to_array(photo)
#     # store
#     photos.append(photo)
#     labels.append(output)
#     # convert to a numpy arrays
#     photos = asarray(photos)
#     labels = asarray(labels)
#     print(photos.shape, labels.shape)
#     # save the reshaped photos
#     save('panda_images_photos.npy', photos)
#     save('panda_images_labels.npy', labels)
#


# # define cnn model
# def define_model():
#     model = Sequential()
#     model.add(Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(200, 200, 3)))
#     model.add(MaxPooling2D((2, 2)))
#     model.add(Flatten())
#     model.add(Dense(128, activation='relu', kernel_initializer='he_uniform'))
#     model.add(Dense(1, activation='sigmoid'))
#     # compile model
#     opt = SGD(lr=0.001, momentum=0.9)
#     model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
#     return model
#

# # plot diagnostic learning curves
# def summarize_diagnostics(history):
#     # plot loss
#     pyplot.subplot(211)
#     pyplot.title('Cross Entropy Loss')
#     pyplot.plot(history.history['loss'], color='blue', label='train')
#     pyplot.plot(history.history['val_loss'], color='orange', label='test')
#     # plot accuracy
#     pyplot.subplot(212)
#     pyplot.title('Classification Accuracy')
#     pyplot.plot(history.history['accuracy'], color='blue', label='train')
#     pyplot.plot(history.history['val_accuracy'], color='orange', label='test')
#     # save plot to file
#     filename = sys.argv[0].split('/')[-1]
#     pyplot.savefig(filename + '_plot.png')
#     pyplot.close()
#
#
# # run the test harness for evaluating a model
# def run_test_harness():
#     # define model
#     model = define_model()
#     # create data generator
#     datagen = ImageDataGenerator(rescale=1.0 / 255.0)
#     # prepare iterators
#     train_it = datagen.flow_from_directory('train/',
#                                            class_mode='binary', batch_size=64, target_size=(200, 200))
#     test_it = datagen.flow_from_directory('test/',
#                                           class_mode='binary', batch_size=64, target_size=(200, 200))
#     # fit model
#     history = model.fit_generator(train_it, steps_per_epoch=len(train_it),
#                                   validation_data=test_it, validation_steps=len(test_it), epochs=20, verbose=0)
#     # evaluate model
#     _, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=0)
#     print('> %.3f' % (acc * 100.0))
#     # learning curves
#     summarize_diagnostics(history)
#     model.save('final_model.h5')
#
#
# # entry point, run the test harness
# run_test_harness()


# make a prediction for a new image.
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model

# load and prepare the image
def load_image(filename):
	# load the image
	img = load_img(filename, target_size=(200, 200))
	# convert to array
	img = img_to_array(img)
	# reshape into a single sample with 3 channels
	img = img.reshape(1, 200, 200, 3)
	# center pixel data
	img = img.astype('float32')
	img = img - [123.68, 116.779, 103.939]
	return img

# load an image and predict the class
def run_example():
	# define location of dataset
	folder = 'massTesting/'
	count = 0
	# enumerate files in the directory
	for file in listdir(folder):
		if file == '.DS_Store':
			continue
		# load the image
		img = load_image(folder + file)
		# load model
		model = load_model('final_model.h5')
		# predict the class
		count += numpy.round(model.predict(img), 0)
		print(model.predict(img))
		# print percentage of pandas
	print(count/len(listdir(folder)))

# entry point, run the example
run_example()
