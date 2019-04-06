from ContentParser import ContentParser
from BagOfWords import BagOfWords
from FileContentSearch import FileContentSearch
from FileNameSearch import FileNameSearch
import pdb

import dropbox
from dropbox.exceptions import AuthError

class FileSearch:
    """
    Class used to represent the file search
    -----
    Methods
    -----
    file_search(self, dropboxBot, fileList, search)
        Formats the fileList found on Dropbox to a list of each files' content. This is then passed to the 
        BagOfWords to find the most accurate searches.
    file_search(self, fileList, search)
        Searches through the fileList from Dropbox    
    """


    def file_search(self, fileList, search):
        """
    Searches through the fileList from Dropbox  

    Parameters
    ----------
    fileList : list
            A list of files found on the Dropbox that are located in the specified companies and year fields.
    search : class 'Search.Search'
            Search object that contains tuples for keywords, specified folders, and specified searches by the Slack user
    Returns
    -------
    BagOfWords.find_accurate_docs(fileList, list, keywords)
        The most accurate documents based on the BagOfWords class
        
    """

        fns = FileNameSearch(self.dropboxBot)
        fcs = FileContentSearch(self.dropboxBot)

        nameDistList = fns.file_name_search(fileList, search)
        contentDistList = fcs.file_content_search(fileList, search)

        combinedDistList = [1] * len(contentDistList)
        for i in range(len(contentDistList)):
            combinedDistList[i] = (contentDistList[i] + nameDistList[i])/2
        
        return combinedDistList


    def __init__(self, dropboxBot): 
        self.dropboxBot = dropboxBot