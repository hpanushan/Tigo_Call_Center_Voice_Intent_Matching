from os import listdir
from os.path import isfile, join

def get_file_name(my_path):
    # Getting files name in current dir
    only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

    return only_files[0]

#my_path = 'C:/Users/Anushan Temp/Desktop/New folder (2)/voice-clips'
#print(get_file_name(my_path))

