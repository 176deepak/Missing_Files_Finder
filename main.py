import os
from pathlib import Path


def directory_files_comparer(direc_name1, direc_name2):
    direc_name1 = Path(str(direc_name1))
    direc_name2 = Path(str(direc_name2))

    dir1_files = os.listdir(direc_name1)
    dir2_files = os.listdir(direc_name2)
    dir1_filenames = []
    dir2_filenames = []

    for i in dir1_files:
        name, _ = i.split(".")
        dir1_filenames.append(name)

    for i in dir2_files:
        name, _ = i.split(".")
        dir2_filenames.append(name)

    absent_files = " "

    for i in dir2_filenames:
        if i not in dir1_filenames:
            absent_files = absent_files+i+", "

    return absent_files
