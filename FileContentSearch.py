import tika
from tika import parser
from BagOfWords import BagOfWords
import pdb
import dropbox

from io import BytesIO

class FileContentSearch:

    def __init__(self):
        """
        Initilizes the tiki VM server.

        This is the slowest portion of the search, so only doing it once will speed everything up considerably
        """
        tika.initVM()
    
    def file_content_search(dropboxBot, fileList, search):
        """
        Finds how many times keywords are used.

        Uses Tika's python interface to parse a document, and then check all of the keywords against it.

        Parameters
        ----------
        file : requests.models.Response
            a dropbox file object returned by the dbx.files_download("path") call
        keywords : tuple
            tuple of keywords in the format ["k1", "k2",...]

        Returns
        -------
        dict
            A dictionary where each key is a keyword and the value contained is the number of times that keyword is used in the document.

        """
        contentList = []

        for files in fileList:
            metadata, resp = dropboxBot.dbx.files_download(files.path_display)

            stream = BytesIO(resp.content)
            parsed = parser.from_buffer(stream)
            docString = parsed["content"].lower()
            contentList.append(docString)

        keywordDict = {}
        """
        for word in search.keywords:
            count = docString.count(word.lower())
            keywordDict[word] = count
        pdb.set_trace()
        return keywordDict
        """
        
        keywords = ' '.join(search.keywords)

        return BagOfWords.find_accurate_docs(fileList, contentList, keywords)
