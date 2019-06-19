import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["dropbox", "slackclient", "docx", "pptx", "openpyxl", "PyPDF2", "nltk", "sklearn", 
                    "idna", 'pkg_resources._vendor', 'numpy.core._methods'], 
                    "include_files":["BagOfWords.py", "ContentParser.py", "DropboxBot.py", "SearchMain.py",
                    "FileContentSearch.py", "FileNameSearch.py", "FileSearch.py", "Message.py", "ParseMessage.py", "RecentFileSearch.py",
                    "RelevantFileList.py", "Search.py", "SearchFeedback.py", "SlackBot.py", "StemmedCountVectorizer.py", 
                    "DropboxSlackIcon.ico"]}


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    pass

setup( name = "Dropbox Search Tool",
            version = "4.0.0",
            description = "Dropbox Search Tool through Slack",
            options = {"build_exe": build_exe_options},
            executables = [Executable("DropboxSearchTool.py", base = base, icon = "DropboxSlackIcon.ico")])