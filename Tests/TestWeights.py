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
            file = filedialog.askopenfilename()
            tokens = open(file, "r")
            lines = tokens.readlines()
            slack = lines[0]
            dropbox = lines[1]

            slackToken = slack
            dropboxToken = dropbox

            dropboxBot = DropboxBot(dropboxToken)
            unittest.main()