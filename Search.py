from FileNameSearch import FileNameSearch
from FileContentSearch import FileContentSearch
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
        self.fileContentSearch = False
        self.fileNameSearch = False
        self.recentFileSearch = False
        self.fileTypeSearch = False
        self.help = False

    def dropbox_search(self, dropboxBot):

        if(self.help):
            return "To search for files use one of the following: \n -fn for a file's name. \n -ft for the file type. \n -fc for a file's content. \n You may also use these optionally for more specific searches: \n -c for the company the file was made for. \n  -y for the year the file was created "
        
        elif(self.recentFileSearch):
            return RecentFileSearch.recent_file_search(dropboxBot)

        #keywords are needed, or there is no way to know what the user wants to search for. Anything else is optional
        elif(self.keywords == []):
            return "Not sure what you mean. Please make sure that you typed it correctly. Example: -fn cool -y 2014* -c google* where * is optional"
        
        elif(self.fileNameSearch):
            fileList = RelevantFileList.retrieve_relevant_files(dropboxBot, self)
            return FileNameSearch.file_name_search(fileList, self)

        elif(self.fileContentSearch):
            fileList = RelevantFileList.retrieve_relevant_files(dropboxBot, self)
            return FileContentSearch.file_content_search(dropboxBot, fileList, self)

    

    def retrieve_hyperlink_list(self, dropboxBot, bestDocFileList):
        links = []
        for file in bestDocFileList:
            path = file.path_display
            links.append(dropboxBot.dbx.sharing_create_shared_link(path).url)
        
        return links