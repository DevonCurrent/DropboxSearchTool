import unittest
import warnings
import sys, os
import concurrent.futures

runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

from ContentParser import ContentParser
from FileSearch import FileSearch
from DropboxBot import DropboxBot

class TestFileContentSearch(unittest.TestCase):

    def test_concurrent(self):
        futureParsedList = [('docx', '/2018/Dell/Money.docx', 0), ('pptx','/2014/Google/powertest.pptx', 1)]

        dropboxBot = DropboxBot()

        contentParser = ContentParser(dropboxBot)
        dataList = contentParser.parse_file_list(futureParsedList)

        self.assertEqual(dataList[0][0], "money money money money money\ni love money")

if __name__ == "__main__":
    unittest.main()