import logging
import os
import numpy 

def get_file_size(file_path):
    # Get size of file in kb
    logging.info("getting file size fucntion")
    file_size = os.stat(file_path).st_size

    file_size_in_kb = int(numpy.ceil(file_size/1024))
    return file_size_in_kb

#print(get_file_size('D:/Movies/Friends/Season 1/friends_s01e01_720p_bluray_x264-sujaidr.mkv'))