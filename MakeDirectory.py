# create directories
from os import makedirs

dataset_home = 'dataset_dogs_vs_cats/'
subdirs = ['train/', 'test/']
for subdir in subdirs:
     # create label subdirectories
     labeldirs = ['dogs/', 'cats/']
     for labldir in labeldirs:
         newdir = dataset_home + subdir + labldir
         makedirs(newdir, exist_ok=True)