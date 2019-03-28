from BagOfWords import BagOfWords
import pdb
class FileNameSearch:
    """
    Class used to represent the file name search
    -----
    Methods
    -----
    file_name_search(self, fileList, search)
        Formats the fileList found on Dropbox to a list of fileNames. This is then passed to the BagOfWords to find
        the most accurate searches.
    """
    def file_name_search(self, fileList, search):

        """
        Formats the fileList found on Dropbox to a list of fileNames. This is then passed to the BagOfWords to find
        the most accurate searches.

        Parameters
        ----------
        fileList : list
            A list of files found on the Dropbox that are located in the specified companies and year fields.
        search : class 'Search.Search'
            Search object that contains tuples for keywords, companies, years, and specified searches by the Slack user

        Returns
        -------
        distList
            A list of each file's distance. Each file's distance is the accuracy of the file's name to
            that of the Slack search query of the user
        """
        
        fileNameList = []
        for entry in fileList:
            # this removes the .ext from entry names when adding to fileNameList
            splitEntry = entry.name.split('.')
            fileName = ""
            for word in splitEntry[:-1]: # there could be more than one '.'
                fileName += word

            fileNameList.append(fileName)

        keywords = ' '.join(search.keywords)
        
        return BagOfWords.find_accurate_docs(fileList, fileNameList, keywords)

    
    def __init__(self, dropboxBot): 
        self.dropboxBot = dropboxBot