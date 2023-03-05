import PIL
import numpy
from database_creation import database_to_list
from os import listdir
from prediction import load_image
from keras.models import load_model

all_coordinates = database_to_list()
# for coordinate in all_coordinates:
#     print(coordinate.latitude)

# TODO: 1. Create a dataset of pictures(300)
#       2. Loop through the pictures and if panda then send coordinates and timestamps to heatmap

def create_dictionary():
    list = []
    i = 0
    folder = '/Users/pattaponpuapanichya/Documents/GitHub/Hack-The-Burgh-2023/animal_image_db/'
    for file in listdir(folder):
        try:
            img = load_image(folder + file)
            model = load_model('/Users/pattaponpuapanichya/Documents/GitHub/Hack-The-Burgh-2023/final_model.h5')
            temp = numpy.round(model.predict(img), 0)
            if temp > 0.75:
                item = {
                    'latitude': all_coordinates[i].latitude,
                    'longitude': all_coordinates[i].longitude,
                    'timestamp': all_coordinates[i].epoch_time
                }
                list.append(item)
            i += 1
        except PIL.UnidentifiedImageError:
            continue

    return list

a = create_dictionary()

for x in range(len(a)):
    print(a[x])