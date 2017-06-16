"""
Function definitions for scrapping the files from the server location are contained in this module.
"""

from __future__ import print_function
import requests
import easygui
import shutil
import os
from bs4 import BeautifulSoup


def move_file(filename, test_taker, task_folder, dest_fldr_root):
    """Moves a file from one locaion to another

    :param filename: file to be moved
    :param test_taker: name of the test taker
    :param task_folder: name of the task folder under test taker folder
    :param dest_fldr_root: root path
    :return: None
    """
    shutil.move(os.path.join(os.getcwd(), filename),
                os.path.join(dest_fldr_root, test_taker, task_folder, filename))


def file_fldr_exists(file_url):
    """Checks if the file exists

    :param file_url: url to the file to be downloaded
    :return: True or False
    """
    r = requests.get(file_url, stream=True)
    if r.status_code == 200:
        return True
    return False


def file_download(file_url):
    """Downloads file from the server

    :param file_url: url to the file to be downloaded
    :return: Either the downloaded file or False
    """
    local_filename = file_url.split('/')[-1]
    r = requests.get(file_url, stream=True)
    if r.status_code == 200:
        with open(local_filename, 'wb') as f:
            count = 0
            for chunk in r.iter_content(chunk_size=1024):
                count += 1
                if count <= 3000:
                    if chunk:
                        f.write(chunk)
                        f.flush()
                else:
                    return 0
        return local_filename
        pass
    return 0


def test_takers():
    """Create a list of test takers from a txt file

    :return: List with usernames of test takers
    """
    try:
        msg = "Choose a text file with test taker's usernames on separate lines."
        title = "Choose a .txt file"
        file_name = easygui.fileopenbox(msg=msg, title=title, filetypes=["*.txt"])
        open_file = open(file_name, "r")
        test_takers_list = open_file.readlines()
        if open_file:
            open_file.close()
        test_takers_list_ref = []
        for i in range(len(test_takers_list)):
            if test_takers_list[i].endswith("\n") and test_takers_list[i] != "\n" and test_takers_list[i] != "":
                test_takers_list_ref.append(test_takers_list[i][:-1])
        return list(set(test_takers_list_ref))

    except Exception as e:
        if file_name is None:
            easygui.msgbox("No text file with usernames selected!" + "\n" + "Script exited", "Error")
            raise SystemExit("No text file with usernames selected!")
        else:
            easygui.msgbox(e.message, "Error")
            raise


def filenames_from_html(src_path):
    """Check for the files in the Task folder

    :return: List of full file name
    """
    with open(src_path) as fp:
        soup = BeautifulSoup(fp, "html.parser")
        existing_files = [link.get('href') for link in soup.findAll('a', href=True) if "." in link['href']]

        # for link in soup.findAll('a', href=True):
        #     if "." in link['href']:
        #         existing_files += link['href']
        return existing_files

