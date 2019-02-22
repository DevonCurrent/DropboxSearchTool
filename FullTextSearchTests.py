import unittest
import warnings

import dropbox
from dropbox.exceptions import AuthError
from io import BytesIO

#from docx import Document
#from pptx import Presentation

import tika
from tika import parser

from FullTextSearch import FullTextSearch


class TestExtraction(unittest.TestCase):

    t = ''

    def test_docx(self):
        warnings.simplefilter("ignore", ResourceWarning)
        dbx = dropbox.Dropbox(t)

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
        
        dbx = dropbox.Dropbox(t)

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
        
        dbx = dropbox.Dropbox(t)

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
        
        dbx = dropbox.Dropbox(t)

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
        dbx = dropbox.Dropbox(t)
        try:
            dbx.users_get_current_account()
        except AuthError as err:
            print(err)
            print("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
            exit()
        
        try:
            metadata, file1 = dbx.files_download('/2014/Google/CapstoneExcelTest.xlsx')
        except dropbox.files.DownloadError as err:
            print(err)
            exit()

        search = FullTextSearch()
        k_dict = search.to_be_searched(file1, ['Test','TRUE','False'])

        self.assertEqual(12, k_dict['Test'])
        self.assertEqual(9, k_dict['TRUE'])
        self.assertEqual(9, k_dict['False'])


if __name__ == "__main__":
    t = input("Enter Dropbox OAuth2 token For Test Account: ")
    tika.initVM()
    unittest.main()