
def txt_file_read(file_location):
    # Read a text file (Returns a string)
    file_object = open(file_location, "r")
    return file_object.read()

