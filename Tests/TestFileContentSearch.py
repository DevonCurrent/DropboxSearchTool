import unittest
import warnings
import tika
from tika import parser
import sys, os

runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))

from DropboxBot import DropboxBot
from Search import Search
from RelevantFileList import RelevantFileList
from BagOfWords import BagOfWords
import dropbox
from dropbox.exceptions import AuthError
from io import BytesIO

#from FileContentSearch import FileContentSearch


class TestFileContentSearch(unittest.TestCase):

    dropbox_token = ''

    def test_docx(self):
        warnings.simplefilter("ignore", ResourceWarning)
        dbx = dropbox.Dropbox(dropbox_token)

        try:
            dbx.users_get_current_account()
        except AuthError as err:
            print(err)
            print("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
            exit()

        try:
            metadata, f = dbx.files_download('/2014/Google/coolmoney.docx')
        except dropbox.files.DownloadError as err:
            print(err)
            exit()

        stream = BytesIO(f.content)

        """
        doc = Document(stream)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)

        print('\n'.join(fullText))
        """

        parsed = parser.from_buffer(stream)
        self.assertNotEqual(len(parsed["content"]),0)


    def test_pptx(self):
        warnings.simplefilter("ignore", ResourceWarning)
        
        dbx = dropbox.Dropbox(dropbox_token)

        try:
            dbx.users_get_current_account()
        except AuthError as err:
            print(err)
            print("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
            exit()

        try:
            metadata, f = dbx.files_download('/2014/Google/4.FeasibilityStudy.ppt')
        except dropbox.files.DownloadError as err:
            print(err)
            exit()

        stream = BytesIO(f.content)

        #pptx only works with .pptx but not with .ppt
        """
        prs = Presentation(stream)
        text_runs = []

        for slide in prs.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        text_runs.append(run.text)

        print(text_runs)
        """

        parsed = parser.from_buffer(stream)
        self.assertNotEqual(len(parsed["content"]),0)
    
    def test_xlsx(self):
        warnings.simplefilter("ignore", ResourceWarning)
        
        dbx = dropbox.Dropbox(dropbox_token)

        try:
            dbx.users_get_current_account()
        except AuthError as err:
            print(err)
            print("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
            exit()

        try:
            metadata, f = dbx.files_download('/2014/Google/CapstoneExcelTest.xlsx')
        except dropbox.files.DownloadError as err:
            print(err)
            exit()

        parsed = parser.from_buffer(BytesIO(f.content))

        count = parsed["content"].count('Test')
        self.assertEqual(count, 12)
    
    def test_keyword(self):
        warnings.simplefilter("ignore", ResourceWarning)
        
        dbx = dropbox.Dropbox(dropbox_token)

        try:
            dbx.users_get_current_account()
        except AuthError as err:
            print(err)
            print("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
            exit()

        try:
            metadata, f = dbx.files_download('/2014/Google/databases_week_3_ER_modeling.pdf')
        except dropbox.files.DownloadError as err:
            print(err)
            exit()

        stream = BytesIO(f.content)
        parsed = parser.from_buffer(stream)

        count = parsed["content"].count('Renet')
        self.assertEqual(count, 42)

    def test_full_text_search_object(self):
        warnings.simplefilter("ignore", ResourceWarning)
        
        dbx = DropboxBot()

        search = Search()
        search.keywords = ['Test', 'TRUE', 'False']
        search.years = ['2014']
        search.companies = ['google']

        fileList = RelevantFileList.retrieve_relevant_files(dbx, search)
        searchableFileTypes = ['.doc','.docx', '.ppt', '.pptx', 'xlsx', '.pdf']

        list = []
        
        for file in fileList:
            if any(fileType in file.name for fileType in searchableFileTypes):
                metadata, resp = dbx.dbx.files_download(file.path_display)
            
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

        results = BagOfWords.find_accurate_docs(fileList, list, keywords)

        self.assertEqual(results[0].path_display, '/2014/Google/CapstoneExcelTest.xlsx')

if __name__ == "__main__":

    dropbox_token = open("DropboxSearchTokens.txt").readlines()[1].strip()
    tika.initVM()
    unittest.main()