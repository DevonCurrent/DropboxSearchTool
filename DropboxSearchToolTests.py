import unittest
import warnings

from SlackBot import SlackBot
from DropboxBot import DropboxBot
from Message import Message
from Search import Search

class TestConnections(unittest.TestCase):

    slack_token = ""
    dropbox_token = ""

    def test_slack_connection(self):
        warnings.simplefilter("ignore", ResourceWarning)
        try:
            slack_bot = SlackBot(slack_token)
        except:
            self.fail("Connection to Slack Test Account Failed, check that app is online")

        del slack_bot
            
    def test_dropbox_connection(self):
        warnings.simplefilter("ignore", ResourceWarning)
        try:
            dropbox_bot = DropboxBot(dropbox_token)
        except:
            self.fail("Connection to Dropbox Failed, check that app is online")

        del dropbox_bot

class TestSearch(unittest.TestCase):

    def test_addSplitSearchTerms(self):
        m = Message("This is a test", "N/A", "N/A", "N/A")
        search_1 = Search(m)
        search_2 = Search(m)

        #Keywords should be split at spaces and turned lowercase
        #Function working on keywords is the same that works on companies, years, etc
        search_1.addKeyword(" ThisShouldNotSplit")
        self.assertEqual(['thisshouldnotsplit'], search_1.keywords)
        self.assertEqual(1, len(search_1.keywords))

        search_2.addKeyword(" This Should be Split")
        self.assertEqual(['this', 'should', 'be', 'split'], search_2.keywords)
        self.assertEqual(4, len(search_2.keywords))



if __name__ == "__main__":
    slack_token = input("Enter Slack OAuth2 token For Test Account: ")
    dropbox_token = input("Enter Dropbox OAuth2 token For Test Account: ")

    unittest.main()