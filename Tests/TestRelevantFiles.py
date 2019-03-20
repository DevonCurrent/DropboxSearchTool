import sys, os
import unittest
import warnings

runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

import dropbox
from dropbox.exceptions import AuthError

from Search import Search

class TestRelevantFiles(unittest.TestCase):

    dropboxToken = ''

    def test_parse(self):
        search = Search()
        search.companies = ['Google', 'Facebook']
        search.years = ['2014', '2016']
        search.keywords = ['key', 'words']


if __name__ == "__main__":

    dropboxToken = open("DropboxSearchTokens.txt").readlines()[1].strip()
    unittest.main()

