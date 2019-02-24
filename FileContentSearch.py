import tika
from tika import parser
from BagOfWords import BagOfWords

from io import BytesIO

class FileContentSearch:

    def __init__(self):
        """
        Initilizes the tiki VM server.

        This is the slowest portion of the search, so only doing it once will speed everything up considerably
        """
        tika.initVM()
    
    def file_content_search(self, file, keywords):
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
        stream = BytesIO(file.content)
        parsed = parser.from_buffer(stream)
        doc_string = parsed["content"].lower()

        keyword_dict = {}

        for word in keywords:
            count = doc_string.count(word.lower())
            keyword_dict[word] = count

        return keyword_dict
