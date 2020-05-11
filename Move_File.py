import logging
import os
import shutil

def move_file(old_path,new_path,file_name):
    # Moving a file
    logging.info("moving a file fucntion")
    logging.info("old path - " + old_path)
    logging.info("new path - " + new_path)

    source_path = old_path + '/' + file_name
    destination_path = new_path + '/' +file_name
    shutil.move(source_path, destination_path)

    