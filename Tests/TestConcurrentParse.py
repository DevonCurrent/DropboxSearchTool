import unittest
import warnings

import concurrent.futures

from FileSearch import FileSearch
from DropboxBot import DropboxBot

class TestFileContentSearch(unittest.TestCase):

    def test_concurrent(self):
        Files = [('doc','/2014/Google/SRS4.doc'), ('docx', '/2014/Google/coolmoney.docx'), ('pptx','/2014/Google/powertest.pptx')]

        dropboxBot = DropboxBot()

        def downloadAndParse(fileType, filePath):
            return [("Path: " + str(filePath)), ("Type: " + str(fileType)), ('')]


        dataList = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_url = {executor.submit(downloadAndParse, file[0], file[1]): file for file in Files}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                    dataList.append(data)
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))
                #else:
                    #print('%r page is %d bytes' % (url, len(data)))

        for data in dataList:
            for d in data:
                print(d)

if __name__ == "__main__":
    unittest.main()