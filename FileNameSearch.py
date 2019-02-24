from BagOfWords import BagOfWords
import pdb
class FileNameSearch:

    def file_name_search(fileList, search):
        
        fileNameList = []
        for entry in fileList:
            fileNameList.append(entry.name)

        keywords = ' '.join(search.keywords)
        pdb.set_trace()
        return BagOfWords.find_accurate_docs(fileList, fileNameList, keywords)