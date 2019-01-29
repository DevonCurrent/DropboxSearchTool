import unittest
import warnings

from SlackBot import SlackBot
from DropboxBot import DropboxBot
from Message import Message
from Search import Search
from ParseMessage import ParseMessage

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

        search_1.addCompanies(" Amazon Google")
        search_1.addYears(" 2016 2017 1994")

        search_1.createCorrectSearchResponse()

        print(search_1.response)
    
    def test_response_generation(self):
        m = Message("This is a test", "N/A", "N/A", "N/A")
        search = Search(m)

        search.addKeyword(" Hello World")
        search.addCompanies(" Amazon Google")
        search.addYears(" 2016 2017 1994")

        search.createCorrectSearchResponse()

        goal_resp = "Ok! I will search for 'hello', 'world' from 'amazon', 'google' from the year(s) '2016', '2017', '1994'"

        self.assertEqual(search.response, goal_resp)

    def test_parse_message(self):
        m_1 = Message("-fn ", "N/A", "N/A", "N/A")
        m_2 = Message("-fc content ", "N/A", "N/A", "N/A")
        m_3 = Message("-fn Education -c Google -y 2019", "N/A", "N/A", "N/A")

        #Returning True means that the function realized there is an error
        self.assertTrue(ParseMessage(m_1))
        self.assertTrue(ParseMessage(m_2))

        error, search = ParseMessage(m_3)

        self.assertFalse(error)
        self.assertEqual(search.companies, ['google'])
        self.assertEqual(search.keywords, ['education'])
        self.assertEqual(search.years, ['2019'])

    #Test will only work if it is supplied the correct Dropbox account
    def test_dropbox_bot(self):
        dropbox_bot = DropboxBot(dropbox_token)

        m = Message("-fn More -c Amazon -y 2017", "N/A", "N/A", "N/A")
        
        error, s = ParseMessage(m)

        if not error:
            s_list = dropbox_bot.SearchDropbox(s)
            self.assertEqual(3, len(s_list))
            
            #Checks that the files were returned in the correct order, highest to smallest
            count = 3
            for file in s_list:
                self.assertEqual(count,file[0].name.count('More'))
                count -= 1



if __name__ == "__main__":
    slack_token = input("Enter Slack OAuth2 token For Test Account: ")
    dropbox_token = input("Enter Dropbox OAuth2 token For Test Account: ")

    unittest.main()