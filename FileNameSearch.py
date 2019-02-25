from BagOfWords import BagOfWords
import pdb
class FileNameSearch:

    def file_name_search(fileList, search):

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
        accurateDocList
            The list of files that are most accurate to the search that the Slack user requested.
        """
        
        fileNameList = []
        for entry in fileList:
            fileNameList.append(entry.name)

        keywords = ' '.join(search.keywords)

        return BagOfWords.find_accurate_docs(fileList, fileNameList, keywords)