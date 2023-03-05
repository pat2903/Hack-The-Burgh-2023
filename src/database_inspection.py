import PIL
import numpy
from database_creation import database_to_list
from os import listdir
from prediction import load_image
from keras.models import load_model

all_coordinates = database_to_list()


def select_coordinates():
    list_coordinates = []
    folder = '../animal_image_db/'
    for i in range(len(listdir(folder))):
        try:
            img = load_image(folder + listdir(folder)[i])
            model = load_model('../final_model.h5')
            image_prediction = numpy.round(model.predict(img), 0)
            if image_prediction > 0.75:
                coordinate = {
                    'latitude': all_coordinates[i].latitude,
                    'longitude': all_coordinates[i].longitude,
                    'timestamp': all_coordinates[i].epoch_time
                }
                list_coordinates.append(coordinate)
        except PIL.UnidentifiedImageError:
            continue
    return list_coordinates
