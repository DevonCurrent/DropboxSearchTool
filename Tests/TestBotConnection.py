import unittest
import warnings
import sys, os

runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

from SlackBot import SlackBot
from DropboxBot import DropboxBot

class TestBotConnections(unittest.TestCase):

    def test_slack_connection(self):
        warnings.simplefilter("ignore", ResourceWarning)
        try:
            testSlackBot = SlackBot()
        except:
            self.fail("Connection to Slack Test Account Failed, check that app is online")

        del testSlackBot
            
    def test_dropbox_connection(self):
        warnings.simplefilter("ignore", ResourceWarning)
        try:
            testDropboxBot = DropboxBot()
        except:
            self.fail("Connection to Dropbox Failed, check that app is online")

        del testDropboxBot

if __name__ == "__main__":
    os.chdir('..')

    unittest.main()