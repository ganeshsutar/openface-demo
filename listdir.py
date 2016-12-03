from os import walk
import os

def get_files(path):
    files = []
    for (dirpath, dirnames, filenames) in walk(path):
        for file in filenames:
            files.append(os.path.join(dirpath, file))
    return files
