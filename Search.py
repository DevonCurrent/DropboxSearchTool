from FileSearch import FileSearch
from FileContentSearch import FileContentSearch
from FileNameSearch import FileNameSearch

from RecentFileSearch import RecentFileSearch
from RelevantFileList import RelevantFileList

"""
Determines the type of Search to make on Dropbox with the given keywords, companies, and years.
Handles exceptions such as help (-h), incorrect searches, and having no keywords in a given search.

"""

class Search:

    def __init__(self):
        self.keywords = []
        self.companies = []
        self.years = []
        self.type = []
        self.recentFileSearch = False
        self.fileTypeSearch = False
        self.help = False
        self.kn = False
        self.kf = False

    def dropbox_search(self, dropboxBot, fileSearch):
        """
        A Search object that stores Slack user message metadata, which can then be passed onto the appropriate 
        search algorithm, or return a message to the user.

        Parameters
        ----------
        dropboxBot : class 'DropboxBot.DropboxBot'
            an instance of DropboxBot that has access to the Dropbox account

        Returns
        -------
        botResp
            A string that can be formatted by the Slack bot to be sent back to the user for communication.
        accurateDocList
            A list of files requested by the Slack user that are the most accurate searches found on the Dropbox  
        """

        if(self.help):
            return "To search for files use one of the following: \n -k for a specific keyword. \n -fn for a file's name. \n -fc for a file's content. \n You may also use these optionally for more specific searches: \n -c for the company the file was made for. \n  -y for the year the file was created "
        
        elif(self.recentFileSearch):
            return RecentFileSearch.recent_file_search(dropboxBot)

        #keywords are needed, or there is no way to know what the user wants to search for. Anything else is optional
        elif(self.keywords == []):
            return "Not sure what you mean. Please make sure that you typed it correctly. Example: -k cool -y 2014* -c google* where * is optional. If you need help please enter -h."
        
        fileList = RelevantFileList.retrieve_relevant_files(dropboxBot, self)

        if self.kf == True:
            return FileContentSearch().file_content_search(dropboxBot, fileList, self)
        
        if self.kn == True:
            return FileNameSearch.file_name_search(dropboxBot, fileList, self)
            
        return fileSearch.file_search(dropboxBot, fileList, self)

    

    def retrieve_hyperlink_list(self, dropboxBot, bestDocFileList):
        links = []
        for file in bestDocFileList:
            path = file.path_display
            links.append(dropboxBot.dbx.sharing_create_shared_link(path).url)
        
        return links