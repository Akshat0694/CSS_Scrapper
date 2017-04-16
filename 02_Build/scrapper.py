from __future__ import print_function
import requests
import os
import easygui
import logging


def file_download(file_url):
    """Downloads file from the server

    :param file_url: url to the file to be downloaded
    :return: Either the downloaded file or False
    """
    local_filename = file_url.split('/')[-1]
    r = requests.get(file_url, stream=True)
    if r.status_code == 200:
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        return local_filename
        pass
    return False


def test_takers():
    """Create a list of test takers from a txt file

    :return: List with usernames of test takers
    """
    try:
        # easygui.fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
        msg = "Choose a text file with test taker's usernames on separate lines."
        title = "Choose a .txt file"
        file_name = easygui.fileopenbox(msg=msg, title=title, filetypes=["*.txt"])
        open_file = open(file_name, "r")
        test_takers_list = open_file.readlines()
        if open_file:
            open_file.close()
        return test_takers_list
    except Exception as e:
        print(e.message)
        raise


def main():
    tasks_folders = ["Task1"]
    test_takers_list = test_takers()
    print(test_takers_list)
    print(" ___________" + "__________________________________________")
    print("| Test Taker " + "|                  Status                |")
    for test_taker in test_takers_list:
        fileurl = "http://users.fs.cvut.cz/~" + test_taker + "/test.docx"
        if file_download(fileurl):
            for tasks_folder in tasks_folders:
                # fileUrl = "http://users.fs.cvut.cz/~" + test_taker + "/"+ tasks_folders "/test.docx"
                test = file_download(fileurl)
                print("|  " + test_taker + "  |      Files successfully downloaded     |")
        else:
            print("|  " + test_taker + "  |Error while downloading files from server|")


if __name__ == "__main__":
    main()
    # pass
