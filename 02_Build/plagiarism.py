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

#
# def compare_files(root_folder):
#     for Answer_folder in retrieve_folder_content(root_folder):
#         for Student_folder in retrieve_folder_content(Answer_folder):
#             for Task_folder in retrieve_folder_content(Student_folder):
#                 for Ans_file in retrieve_folder_content(Task_folder, True):
#                     with open(Ans_file, 'r') as fp:
#                         s = fp.readlines()
#                         for Student_folder2 in retrieve_folder_content(Student_folder):
#                             if Student_folder2 != Student_folder:
#                                 for Task_folder2 in retrieve_folder_content(Task_folder):
#                                     if Task_folder2 == Task_folder:
#                                         for Ans_file2 in retrieve_folder_content(Task_folder2, True):
#                                             with open(Ans_file2, 'r') as fp2:
#                                                 s_to_comp = fp2.readlines()
#                                                 result = fuzz.ratio(s, s_to_comp)
#                                                 return result

