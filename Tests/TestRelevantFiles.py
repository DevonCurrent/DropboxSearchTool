import sys, os
import unittest
import warnings

runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

import dropbox
from dropbox.exceptions import AuthError

from Search import Search
from DropboxBot import DropboxBot

class TestRelevantFiles(unittest.TestCase):

    dropboxToken = ''

    def test_flags(self):

        dropboxbot = DropboxBot()
        search = Search()

        search.companies = ['Google', 'IBM']
        search.years = ['2014', '2016']
        search.keywords = ['key', 'words']

        cFlag = False
        yFlag = False

        if(len(search.companies)>0):
            cFlag = True
        
        if(len(search.years)>0):
            yFlag = True

        self.assertEqual(cFlag, True)
        self.assertEqual(yFlag, True)

        fileList = []
        pathList = []

        for entry in dropboxbot.dbx.files_list_folder('',True).entries:
            if '.' in entry.path_display:
                path = entry.path_display.split('/')

                #removes empty first element
                path.pop(0)

                pathList.append(path)

        if yFlag:
            filtered_pathList = [(x,y,z) for (x,y,z) in pathList if x in search.years]
            pathList = filtered_pathList
        
        if cFlag:
            filtered_pathList = [(x,y,z) for (x,y,z) in pathList if y in search.companies]
            pathList = filtered_pathList
        
        for path in pathList:
            if path[0] != '2014':
                if path[0] != '2016':
                    self.fail()

            if path[1] != 'Google':
                if path[1] != 'IBM':
                    self.fail()
        



if __name__ == "__main__":

    dropboxToken = open("DropboxSearchTokens.txt").readlines()[1].strip()
    unittest.main()

