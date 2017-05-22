from __future__ import print_function
from fuzzywuzzy import fuzz
import os


def retrieve_folder_content(src_path, file_check=False):
    """

    :param src_path: full_path of the folder for which the subdirs are to be retrieved
    :param file_check: Check for files in folder
    :return: List of absolute path to the subdirs in a dir
    """

    if not file_check:
        contents = [os.path.abspath(name) for name in os.listdir(src_path) if os.path.isdir(os.path.join(src_path, name))]
    else:
        contents = [os.path.abspath(name) for name in os.listdir(src_path) if not os.path.isdir(os.path.join(src_path, name))]
    return contents


def compare_files(src_path):
    pass
