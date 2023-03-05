from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model
from os import listdir
import numpy


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
def predict_test_image(image):
    # load the image
    img = load_image(image)

    # load model
    model = load_model('../final_model.h5')

    # predict the class
    result = model.predict(img)
    print(result[0])


def predict_test_images():
    # define location of dataset
    folder = '../mass_testing/'
    count = 0

    # enumerate files in the directory
    for file in listdir(folder):
        if file == '.DS_Store':
            continue

        # load the image
        print(folder + file)
        img = load_image(folder + file)

        # load model
        model = load_model('../final_model.h5')

        # predict the class
        count += numpy.round(model.predict(img), 0)

    # print percentage of correctly predicted images
    incorrect_guess_percentage = (count / len(listdir(folder))) * 100
    print(f"{(100 - incorrect_guess_percentage)}%")
