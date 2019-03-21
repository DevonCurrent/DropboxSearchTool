import unittest
import warnings
import sys, os

runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

from SlackBot import SlackBot
from DropboxBot import DropboxBot
from Search import Search
from FileNameSearch import FileNameSearch

"""
Tests that a fileList can be given to FileNameSearch and a list of files most accurate to the search will be returned
"""

class TestMessageParsing(unittest.TestCase):

    def test_file_name_search1(self):
        search = Search()
        search.keywords = ["different", "leadership"]
        
        fileList = [dbx.files_get_metadata("/2014/Microsoft/Different Leadership.docx")]

        fns = FileNameSearch.file_name_search(dropboxBot, fileList, search)
        
        self.assertEqual(fileList[0].name, fns[0].name)
        self.assertEqual(len(fileList), len(fns))

if __name__ == "__main__":
    os.chdir('..')
    
    slackBot = SlackBot()
    dropboxBot = DropboxBot()
    dbx = dropboxBot.dbx

    unittest.main()