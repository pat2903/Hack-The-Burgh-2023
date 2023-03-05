from database_creation import database_to_list

all_coordinates = database_to_list()
for coordinate in all_coordinates:
    print(coordinate.latitude)

# TODO: 1. Create a dataset of pictures(300)
#       2. Loop through the pictures and if panda then send coordinates and timestamps to heatmap
