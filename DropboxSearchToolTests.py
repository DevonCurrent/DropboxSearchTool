import unittest
import warnings

from SlackBot import SlackBot
from DropboxBot import DropboxBot
from Message import Message
from Search import Search
from parse_message import parse_message

class TestConnections(unittest.TestCase):

    slackToken = ""
    dropboxToken = ""

    def test_slack_connection(self):
        warnings.simplefilter("ignore", ResourceWarning)
        try:
            slackBot = SlackBot(slackToken)
        except:
            self.fail("Connection to Slack Test Account Failed, check that app is online")

        del slackBot
            
    def test_dropbox_connection(self):
        warnings.simplefilter("ignore", ResourceWarning)
        try:
            dropboxBot = DropboxBot(dropboxToken)
        except:
            self.fail("Connection to Dropbox Failed, check that app is online")

        del dropboxBot

class TestSearch(unittest.TestCase):

    def test_add_split_search_terms(self):
        m = Message("This is a test", "N/A", "N/A", "N/A")
        search1 = Search(m)
        search2 = Search(m)

        #Keywords should be split at spaces and turned lowercase
        #Function working on keywords is the same that works on companies, years, etc
        search1.add_keywords(" ThisShouldNotSplit")
        self.assertEqual(['thisshouldnotsplit'], search1.keywords)
        self.assertEqual(1, len(search1.keywords))

        search2.add_keywords(" This Should be Split")
        self.assertEqual(['this', 'should', 'be', 'split'], search2.keywords)
        self.assertEqual(4, len(search2.keywords))

        search1.add_companies(" Amazon Google")
        search1.add_years(" 2016 2017 1994")

        search1.create_correct_search_response()

        print(search1.response)
    
    def test_response_generation(self):
        m = Message("This is a test", "N/A", "N/A", "N/A")
        search = Search(m)

        search.add_keywords(" Hello World")
        search.add_companies(" Amazon Google")
        search.add_years(" 2016 2017 1994")

        search.create_correct_search_response()

        goalResp = "Ok! I will search for 'hello', 'world' from 'amazon', 'google' from the year(s) '2016', '2017', '1994'"

        self.assertEqual(search.response, goalResp)

    def test_parse_message(self):
        m_1 = Message("-fn ", "N/A", "N/A", "N/A")
        m_2 = Message("-fc content ", "N/A", "N/A", "N/A")
        m_3 = Message("-fn Education -c Google -y 2019", "N/A", "N/A", "N/A")

        #Returning True means that the function realized there is an error
        self.assertTrue(parse_message(m_1))
        self.assertTrue(parse_message(m_2))

        error, search = parse_message(m_3)

        self.assertFalse(error)
        self.assertEqual(search.companies, ['google'])
        self.assertEqual(search.keywords, ['education'])
        self.assertEqual(search.years, ['2019'])

    #Test will only work if it is supplied the correct Dropbox account
    def test_dropbox_bot(self):
        dropboxBot = DropboxBot(dropboxToken)

        m = Message("-fn More -c Amazon -y 2017", "N/A", "N/A", "N/A")
        
        error, s = parse_message(m)

        if not error:
            searchList = dropboxBot.search_dropbox(s)
            self.assertEqual(3, len(searchList))
            
            #Checks that the files were returned in the correct order, highest to smallest
            count = 3
            for file in searchList:
                self.assertEqual(count,file[0].name.count('More'))
                count -= 1



if __name__ == "__main__":
    slackToken = input("Enter Slack OAuth2 token For Test Account: ")
    dropboxToken = input("Enter Dropbox OAuth2 token For Test Account: ")

    unittest.main()