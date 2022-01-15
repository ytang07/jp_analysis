import os

# get filenames
def get_filenames():
    filenames = []
    for filename in os.listdir("./jp/"):
        filenames.append(filename[:-5])
    return filenames