from __future__ import absolute_import
from unittest import TestCase
from scrapper import file_download
# import os.path
import os

class TestDocxFileDownload(TestCase):
    """
    Modify the url parameters to the file_download to test.
    Use url to the file for the user account to which you have access.
    """

    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    BASE_DIR = os.getcwd()

    def test(self):
        if os.path.isfile("test.docx"):
            os.remove(os.path.join(BASE_DIR, "test.docx"))
        else:
            file_download("http://users.fs.cvut.cz/~tandoaks/test.docx")
            self.assertIs(True, os.path.isfile("test.docx"))
