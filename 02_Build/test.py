from __future__ import absolute_import
from unittest import TestCase
import scrapper
import os.path


class TestDocxFileDownload(TestCase):
    def test(self):
        scrapper.file_download("http://users.fs.cvut.cz/~tandoaks/test.docx")
        self.assertIs(True, os.path.isfile("test.docx"))

