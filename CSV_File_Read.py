import csv
import os

def csv_file_read(file_location):
    keywords = []
    with open(file_location, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for keyword in row:
                # Remove white spaces in string
                out = keyword.replace(" ", "")
                keywords.append(out)

    # Getting unique values
    keywords = list(set(keywords))

    # Remove file
    os.remove(file_location)
    return keywords




