from __future__ import print_function
import requests
import os
import errno
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
        test_takers_list_ref = []
        for i in range(len(test_takers_list)):
            if test_takers_list[i].endswith("\n") and test_takers_list[i] != "\n" and test_takers_list[i] != "":
                test_takers_list_ref.append(test_takers_list[i][:-1])
        return test_takers_list_ref

    except Exception as e:
        print(e.message)
        raise


def main():
    """Entry point to the script

    This function runs and generates report on how
    successful the script ran.
    """
    import datetime

    tasks_folders = ["Task1", "Task2", "Task3"]
    test_takers_list = test_takers()
    print(test_takers_list)

    curr_dir = os.getcwd()
    rep_dir = os.path.join(curr_dir, "Reports")
    if not os.path.exists(rep_dir):
        os.mkdir(rep_dir)

    with open(os.path.join("Reports", "report " + str(datetime.datetime.now()) + ".txt"), "w") as report_file:
        report_file.write(" " + "_"*64 + "\n")
        report_file.write("| Test Taker " + "| Tasks " + "  |                  Status                 |" + "\n")
        report_file.write(" " + "-"*64 + "\n")
        for test_taker in test_takers_list:
            count = 0
            for tasks_folder in tasks_folders:
                count += 1
                # fileurl = "http://users.fs.cvut.cz/~" + test_taker + "/" + tasks_folder + "/test.docx"
                # fileurl = "http://users.fs.cvut.cz/~" + test_taker + "/test.docx"
                fileurl = "http://users.fs.cvut.cz/~" + test_taker
                if file_download(fileurl):
                    test = file_download(fileurl)
                    if count == 1:
                        report_file.write("|  " + test_taker + "  | " + tasks_folder + "   |      Files successfully downloaded      |" + "\n")
                    else:
                        report_file.write("|            | " + tasks_folder + "   |      Files successfully downloaded      |" + "\n")
                else:
                    if count == 1:
                        report_file.write("|  " + test_taker + "  | " + tasks_folder + "   |Error while downloading files from server|" + "\n")
                    else:
                        report_file.write("|            | " + tasks_folder + "   |Error while downloading files from server|" + "\n")
        report_file.write(" " + "-"*64 + "\n")
        report_file.close()

if __name__ == "__main__":
    main()
    # pass
