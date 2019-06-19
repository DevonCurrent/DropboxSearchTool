from ContentParser import ContentParser
from BagOfWords import BagOfWords
import pdb

import dropbox
from dropbox.exceptions import AuthError

from io import BytesIO
import tempfile
from docx import Document
from pptx import Presentation
import openpyxl
import PyPDF2
from subprocess import check_output

import time

import concurrent.futures

class FileContentSearch:
    """
    Class used to represent the file content search
    -----
    Methods
    -----
    file_content_search(self, dropboxBot, fileList, search)
        Formats the fileList found on Dropbox to a list of each files' content. This is then passed to the 
        BagOfWords to find the most accurate searches.
    """
    
    def file_content_search(self, fileList, search, slackBot, m):
        """
        Formats the fileList found on Dropbox to a list of each files' content. This is then passed to the 
        BagOfWords to find the most accurate searches.

        Parameters
        ----------
        dropboxBot : class 'DropboxBot.DropboxBot'
            an instance of DropboxBot that has access to the Dropbox account
        fileList : list
            A list of files found on the Dropbox that are located in the specified companies and year fields.
        search : class 'Search.Search'
            Search object that contains tuples for keywords, specified folders, and specified searches by the Slack user

        Returns
        -------
        distList
            A list of each file's distance. Each file's distance is the accuracy of the file's content to
            that of the Slack search query of the user
        """
            
        futureParsedList = []

        for index, file in enumerate(fileList, start=0):
            filePath = file.path_display
            fileType = file.name.split('.')[-1]
            data = (fileType, filePath, index)
            print(data[1])
            futureParsedList.append(data)

        contentParser = ContentParser(self.dropboxBot)
        list = contentParser.parse_file_list(futureParsedList, slackBot, m)
        
        keywords = ' '.join(search.keywords)

        #Resorts list to follow the original index, for BagOfWords
        list.sort(key=lambda tup: tup[1])

        dataList = []
        for element in list:
            dataList.append(element[0])

        return BagOfWords.find_accurate_docs(fileList, dataList, keywords)


    def __init__(self, dropboxBot): 
        self.dropboxBot = dropboxBot