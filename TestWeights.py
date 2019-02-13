import unittest
import warnings

from SlackBot import SlackBot
from DropboxBot import DropboxBot
from Message import Message
from Search import Search
from ParseMessage import parse_message

class TestWeights(unittest.TestCase):
    
    def test_filename_weights_1(self):
        


if __name__ == "__main__":
    slackToken = input("Enter Slack OAuth2 token For Test Account: ")
    dropboxToken = input("Enter Dropbox OAuth2 token For Test Account: ")

    dropboxBot = DropboxBot(dropboxToken)
    unittest.main()