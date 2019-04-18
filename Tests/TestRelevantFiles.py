import sys, os
import unittest
import warnings

runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

import dropbox
from dropbox.exceptions import AuthError

from Search import Search
from DropboxBot import DropboxBot
from RelevantFileList import RelevantFileList

class TestRelevantFiles(unittest.TestCase):

    def test_retrieve_all_files(self):
        search = Search()
        search.keywords = ["money"]

        rfl = RelevantFileList.retrieve_relevant_files(dropboxBot, search)

        numDropboxFiles = 0
        for entry in dbx.files_list_folder('',True).entries: # number of files in the Dropbox
            if '.' in entry.path_display:
                numDropboxFiles = numDropboxFiles + 1

        self.assertEqual(len(rfl), numDropboxFiles)


    def test_retrieve_year_files(self):
        search = Search()
        search.keywords = ["money"]
        search.folders = ["2014"]

        rfl = RelevantFileList.retrieve_relevant_files(dropboxBot, search)

        numDropboxFiles = 0
        for entry in dbx.files_list_folder('/2014',True).entries: #number of files in the 2014 folder
            if '.' in entry.path_display:
                numDropboxFiles = numDropboxFiles + 1

        self.assertEqual(len(rfl), numDropboxFiles)


    def test_retreive_comp_files(self):
        search = Search()
        search.keywords = ["money"]
        search.folders = ["2014", "google"]

        rfl = RelevantFileList.retrieve_relevant_files(dropboxBot, search)

        numDropboxFiles = 0
        for entry in dbx.files_list_folder('/2014/Google',True).entries: #number of files in the 2014 folder
            if '.' in entry.path_display:
                numDropboxFiles = numDropboxFiles + 1
        
        self.assertEqual(len(rfl), numDropboxFiles)


    def test_retrieve_type_files(self):
        search = Search()
        search.keywords = ["money"]
        search.folders = ["2014", "google"]
        search.types = ["docx"]

        rfl = RelevantFileList.retrieve_relevant_files(dropboxBot, search)
        self.assertEqual(rfl[0].name, "coolmoney.docx") # there is one docx file in this location


    def test_flags(self):
        search = Search()

        search.folders = ['2014', '2016', "google", "IBM"]
        search.keywords = ['key', 'words']

        fFlag = False

        if(len(search.folders)>0):
            fFlag = True
        
        self.assertEqual(fFlag, True)

        """
        fileList = []
        pathList = []

        for entry in dropboxBot.dbx.files_list_folder('',True).entries:
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

        """


if __name__ == "__main__":
    os.chdir('..')
    dropboxBot = DropboxBot()
    dbx = dropboxBot.dbx

    unittest.main()

