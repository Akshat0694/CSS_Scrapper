from __future__ import absolute_import
from unittest import TestCase
from .scrapper import file_download, filenames_from_html
from .plagiarism import *
import os
import shutil


class TestDocxFileDownload(TestCase):
    """
    Modify the url parameters to the file_download to test.
    Use url to the file for the user account to which you have access.
    """

    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    BASE_DIR = os.getcwd()

    def test(self):
        base_dir = os.getcwd()
        if os.path.isfile("test.docx"):
            os.remove(os.path.join(base_dir, "test.docx"))
        else:
            file_download("http://users.fs.cvut.cz/~tandoaks/test.docx")
            result = os.path.isfile("test.docx")
            os.remove(os.path.join(base_dir, "test.docx"))
            self.assertIs(True, result)


class TestFilenamesFromHTML(TestCase):

    def test(self):
        file_download("http://users.fs.cvut.cz/~tandoaks/Task1")
        src_path = os.path.join(os.getcwd(), "Task1.html")
        shutil.move(os.path.join(os.getcwd(), "Task1"), src_path)
        existing_files = filenames_from_html(src_path)
        os.remove(src_path)
        self.assertIs(True, "task1.docx" in existing_files)


class TestRetrieveFolderContent(TestCase):

    def test(self):
        src_path = os.getcwd()
        folder_to_search = os.path.join(src_path, "Test")
        if not os.path.exists(folder_to_search):
            os.mkdir(folder_to_search)
        contents = retrieve_folder_content(src_path)
        os.rmdir(folder_to_search)
        self.assertIs(True, folder_to_search in contents)
