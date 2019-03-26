from BagOfWords import BagOfWords
import pdb

import dropbox
from dropbox.exceptions import AuthError

from io import BytesIO
import tempfile
from docx import Document
from pptx import Presentation
import openpyxl
import PyPDF2
from subprocess import check_output

import time

import concurrent.futures

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
    
    dropboxBot = None

    def _NameSearch(self, dropboxBot, fileList, search):
        fileNameTextList = []
        for entry in fileList:
            # this removes the .ext from entry names when adding to fileNameTextList
            splitEntry = entry.name.split('.')
            fileName = ""
            for word in splitEntry[:-1]: # there could be more than one '.'
                fileName += word
            fileNameTextList.append(fileName)

        keywords = ' '.join(search.keywords)

        return BagOfWords.find_accurate_docs(fileList, fileNameTextList, keywords)

    def _DocxParse(self, filename):
        try:
            metadata, f = self.dropboxBot.dbx.files_download(filename)
        except dropbox.files.DownloadError as err:
            print(err)
            exit()

        stream = BytesIO(f.content)

        doc = Document(stream)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text.lower())

        return '\n'.join(fullText)

    def _DocParse(self, filename):

        out = ''
        with tempfile.NamedTemporaryFile(delete=False, suffix='.doc') as temp:
            self.dropboxBot.dbx.files_download_to_file(temp.name, filename)
            out = check_output(['antiword', '-f' ,temp.name])
        
        return out.lower()

    def _PptxParse(self, filename):
        try:
            metadata, f = self.dropboxBot.dbx.files_download(filename)
        except dropbox.files.DownloadError as err:
            print(err)
            exit()

        stream = BytesIO(f.content)

        #pptx only works with .pptx but not with .ppt
        prs = Presentation(stream)
        text_runs = []
            
        for slide in prs.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        text_runs.append(run.text.lower())

        text = ''
        for run in text_runs:
            text += run
        
        return text

    def _XlsxParse(self, filename):
        try:
            metadata, f = self.dropboxBot.dbx.files_download(filename)
        except dropbox.files.DownloadError as err:
            print(err)
            exit()

        stream = BytesIO(f.content)

        stream = BytesIO(f.content)
        book = openpyxl.load_workbook(stream)

        string = ''

        for sheet in book:
            for row in sheet.iter_rows():
                for cell in row:
                    string += ' '
                    string += str(cell.value).lower()

        return string

    def _PdfParse(self, filename):
        try:
            metadata, f = self.dropboxBot.dbx.files_download(filename)
        except dropbox.files.DownloadError as err:
            print(err)
            exit()

        stream = BytesIO(f.content)

        pdfReader = PyPDF2.PdfFileReader(stream)

        numberOfPages = pdfReader.numPages
        string = ''

        for i in range(0, numberOfPages):
            string += ' '
            string += str(pdfReader.getPage(i).extractText().lower())

        return string

    def _NonsupportedParse(self, filename):
        splitEntry = filename.split('.')
        fileName = ""

        for word in splitEntry[:-1]: # there could be more than one '.'
            fileName += word

        return fileName

    def Search(self, fileList, search, type):
        if type:
            return self._NameSearch(self.dropboxBot, fileList, search)

        list = []

        total1 = time.time()
        
        fileParseType = []
        for file in fileList:
            filePath = file.path_display
            fileType = file.name.split('.')[-1]
            data = (fileType, filePath)
            fileParseType.append(data)

        def downloadAndParse(fileType, filePath):
            if (fileType == 'doc'):
                t1 = time.time()
                x = self._DocParse(filePath)
                t2 = time.time()

                print("Time for .doc file " + filePath + ": " + str(t2 - t1))
                
                return x
            elif (fileType == 'docx'):
                t1 = time.time()
                x = self._DocxParse(filePath)
                t2 = time.time()

                print("Time for .docx file " + filePath + ": " + str(t2 - t1))
                
                return x
            elif (fileType == 'pptx'):
                t1 = time.time()
                x = self._PptxParse(filePath)
                t2 = time.time()

                print("Time for .pptx file " + filePath + ": " + str(t2 - t1))
                
                return x
            elif (fileType == 'xlsx'):
                t1 = time.time()
                x = self._XlsxParse(filePath)
                t2 = time.time()

                print("Time for .Xlsx file " + filePath + ": " + str(t2 - t1))
                
                return x
            elif (fileType == 'pdf'):
                t1 = time.time()
                x = self._PdfParse(filePath)
                t2 = time.time()

                print("Time for .pdf file " + filePath + ": " + str(t2 - t1))
                
                return x
            else:
                t1 = time.time()
                x = self._NonsupportedParse(filePath)
                t2 = time.time()

                print("Time for other file " + filePath + ": " + str(t2 - t1))
                
                return x

        list = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_parses = {executor.submit(downloadAndParse, file[0], file[1]): file for file in fileParseType}
            for future in concurrent.futures.as_completed(future_parses):
                name = future_parses[future]
                try:
                    data = future.result()
                    list.append(data)
                except Exception as exc:
                    print('%r generated an exception: %s' % (name, exc))
        
        total2 = time.time()

        print("Total parse time for " + str(len(fileList)) + " files: " + str(total2 - total1))

        keywords = ' '.join(search.keywords)

        return BagOfWords.find_accurate_docs(fileList, list, keywords)

    def __init__(self, dropboxBot):
        """
        Formats the fileList found on Dropbox to a list of each files' content. This is then passed to the 
        BagOfWords to find the most accurate searches.'

        Parameters
        ----------
        dropboxBot : class 'DropboxBot.DropboxBot'
            an instance of DropboxBot that has access to the Dropbox account
        fileList : list
            A list of files found on the Dropbox that are located in the specified companies and year fields.
        search : class 'Search.Search'
            Search object that contains tuples for keywords, companies, years, and specified searches by the Slack user
        type : 0 for content search, 1 for name search
        
        Returns
        -------
        accurateDocList
            The list of files that are most accurate to the search that the Slack user requested.
        """
        self.dropboxBot = dropboxBot

            
