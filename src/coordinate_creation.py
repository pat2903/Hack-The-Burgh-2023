import random


# returns a list containing random coordinates
def create_coordinates():
    # TODO: come up with better comments in this function

    # minimum latitude value of selected place
    min_lat = 30
    # range through which latitude can differ
    lat_range = 13

    min_long = 81
    long_range = 36

    rand_lat = round(min_lat + random.random() * lat_range, 3)
    rand_long = round(min_long + random.random() * long_range, 3)

    return [rand_lat, rand_long]
