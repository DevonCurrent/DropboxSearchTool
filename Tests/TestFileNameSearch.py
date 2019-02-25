import unittest
import warnings
import sys, os

runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

from SlackBot import SlackBot
from DropboxBot import DropboxBot
from Message import Message
from Search import Search
from ParseMessage import parse_message

class TestWeights(unittest.TestCase):
    
    def test_filename_weights_1(self):
        if __name__ == "__main__":

            slackToken = slack
            dropboxToken = dropbox

            dropboxBot = DropboxBot(dropboxToken)
            unittest.main()