import unittest
import warnings
import sys, os
import pdb

runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

from SlackBot import SlackBot
from DropboxBot import DropboxBot
from Message import Message
from Search import Search
from ParseMessage import parse_message

class TestFileNameSearch(unittest.TestCase):
    
    def test_file_name_search_1(self):
        msg = Message("-fn money -c ibm -y 2016", "N/A", "N/A", "N/A") # there is only one file called 'Money.docx' in this directory

        search = parse_message(dropboxBot, msg)
        fileList = search.dropbox_search(dropboxBot)
        fileName = fileList[0].name

        self.assertEqual(fileName, "Money.docx")

if __name__ == "__main__":
    os.chdir('..')
    
    slackBot = SlackBot()
    dropboxBot = DropboxBot()

    unittest.main()