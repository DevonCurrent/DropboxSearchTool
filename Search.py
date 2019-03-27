import FileSearch

from RecentFileSearch import RecentFileSearch
from RelevantFileList import RelevantFileList


class Search:
    """
    Determines the type of Search to make on Dropbox with the given keywords, companies, and years.
    Handles exceptions such as help (-h), incorrect searches, and having no keywords in a given search.
    -----
    Attributes
    -----
    keywords: str array
        keywords entered 
    companies: str array
        companies entered
    years: str array
        years entered
    types: str array
        file types entered
    recentFileSearch: boolean
        keyword for recent files
    fileTypeSearch: boolean
        keyword for file type
    help: boolean
        keyword for help
    kn: boolean
        keyword for file name
    kf: boolean
        keyword for file content
    -----
    Methods
    -----
    dropbox_search(self, dropboxBot, fileSearch)
        A Search object that stores Slack user message metadata, which can then be passed onto the appropriate 
        search algorithm, or return a message to the user.
    retrieve_hyperlink_list(self, dropboxBot, bestDocFileList)
        Gathers the hyperlinks to the files that have been found matching the input
    """

    def __init__(self):
        self.keywords = []
        self.companies = []
        self.years = []
        self.types = []
        self.recentFileSearch = False
        self.fileTypeSearch = False
        self.help = False
        self.kn = False
        self.kf = False

    def dropbox_search(self, dropboxBot):
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
            return "If you need to search for files start a direct message with me and use the following commands: \n -k for a specific keyword. \n -kn for a file's name. \n -kc for a file's content. \n -c for the company the file was made for. \n -y for the year the file was created. \n -t for a file type. \n -r for recently edited files."

        elif(self.recentFileSearch):
            return RecentFileSearch.recent_file_search(dropboxBot)

        #keywords are needed, or there is no way to know what the user wants to search for. Anything else is optional
        elif(self.keywords == []):
            return "Not sure what you mean. Please make sure that you typed it correctly. Example: -k cool -y 2014* -c google* where * is optional. If you need help please enter -h."
        
        fileList = RelevantFileList.retrieve_relevant_files(dropboxBot, self)

        fs = FileSearch.FileSearch(dropboxBot)

        if self.kf == True:
            return fs.Search(fileList, self, 0)
        elif self.kn == True:
            return fs.Search(fileList, self, 1)
        else:
            return fs.Search(fileList, self, 0)
            

    def retrieve_hyperlink_list(self, dropboxBot, bestDocFileList):
        links = []
        for file in bestDocFileList:
            path = file.path_display
            links.append(dropboxBot.dbx.sharing_create_shared_link(path).url)
        
        return links