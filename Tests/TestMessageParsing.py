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

"""
Tests that messages can be parsed into Search objects, with the appropriate fields.
"""

class TestMessageParsing(unittest.TestCase):

    #Keywords should be split at spaces and turned lowercase
    def test_parse_keywords(self):
        msg = Message("-f This is a test", "N/A", "N/A", "N/A")
        search = parse_message(dropboxBot, msg)

        self.assertEqual(search.keywords, ["this", "is", "a", "test"])


    def test_parse_companies(self):
        msg = Message("-f This is a test -l IBM google apple", "N/A", "N/A", "N/A")
        search = parse_message(dropboxBot, msg)

        self.assertEqual(search.folders, ["ibm", "google", "apple"])

    
    def test_parse_years(self):
        msg = Message("-f This is a test -l 2015 2017 2018", "N/A", "N/A", "N/A")
        search = parse_message(dropboxBot, msg)

        self.assertEqual(search.folders, ["2015", "2017", "2018"])


    def test_parse_types(self):
        msg = Message("-f This is a test -t .pdf docx .doc", "N/A", "N/A", "N/A")
        search = parse_message(dropboxBot, msg)

        self.assertEqual(search.types, ["pdf", "docx", "doc"])

    
    def test_recent_file_search_flag(self):
        msg = Message("-r", "N/A", "N/A", "N/A")
        search = parse_message(dropboxBot, msg)

        self.assertTrue(search.recentFileSearch)
    

    def test_help_response(self):
        msg = Message("-h", "N/A", "N/A", "N/A")
        search = parse_message(dropboxBot, msg)
        
        botResp = search.dropbox_search(DropboxBot)
        helpResp = "If you need to search for files start a direct message with me and use the following commands: \n -f for a specific word. \n -fn for a file's name. \n -fc for a file's content. \n -c for the company the file was made for. \n -y for the year the file was created. \n -t for a file type. \n -r for recently edited files."

        self.assertEqual(botResp, helpResp)
    

    def test_no_keywords(self):
        #lack of keywords should result in an error since there is no specific file to search for
        msg = Message("-y 2015 2017 2018", "N/A", "N/A", "N/A")
        search = parse_message(DropboxBot, msg)

        botResp = search.dropbox_search(DropboxBot)
        noKeywordsResp = "Not sure what you mean. Please make sure that you typed it correctly. Example: -f cool -y 2014* -c google* where * is optional. If you need help please enter -h."

        self.assertEqual(botResp, noKeywordsResp)

if __name__ == "__main__":
    os.chdir('..')
    
    slackBot = SlackBot()
    dropboxBot = DropboxBot()

    unittest.main()