import tika
from tika import parser
from BagOfWords import BagOfWords
import pdb
import dropbox

from io import BytesIO

class FileSearch:
    """
    Class used to represent the file search
    -----
    Methods
    -----
    file_search(self, dropboxBot, fileList, search)
        Formats the fileList found on Dropbox to a list of each files' content. This is then passed to the 
        BagOfWords to find the most accurate searches.
    """

    def __init__(self):
        """
        Initilizes the tiki VM server.

        This is the slowest portion of the search, so only doing it once will speed everything up considerably
        """
        tika.initVM()
    
    def file_search(self, dropboxBot, fileList, search):
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
            Search object that contains tuples for keywords, companies, years, and specified searches by the Slack user

        Returns
        -------
        accurateDocList
            The list of files that are most accurate to the search that the Slack user requested.
        """
        list = []
        searchableFileTypes = ['.doc','.docx', '.ppt', '.pptx', 'xlsx', '.pdf', '.txt']

        for file in fileList:
            if any(fileType in file.name for fileType in searchableFileTypes):
                metadata, resp = dropboxBot.dbx.files_download(file.path_display)
            
                #Currently not using the metadata
                del metadata

                stream = BytesIO(resp.content)
                parsed = parser.from_buffer(stream)
                docString = parsed["content"].lower()

                #Adds file name to doc string so that it is also searched
                docString = docString + " " + file.name

                list.append(docString)
            else:
                #Adds filenames to search instead of content
                list.append(file.name)
        
        keywords = ' '.join(search.keywords)

        return BagOfWords.find_accurate_docs(fileList, list, keywords)
