from __future__ import print_function
import requests
import easygui


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
        if file_name is None:
            print("No text file with usernames selected!")
        else:
            print(e.message)
            raise
