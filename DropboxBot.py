import dropbox
from dropbox.exceptions import AuthError
from BagOfWords import BagOfWords
import pdb
    
class DropboxBot:

    def __init__(self, t):
        self.token = t
        self.dbx = dropbox.Dropbox(t)

        try:
            self.dbx.users_get_current_account()
        except AuthError as err:
            print(err)
            print("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
            exit()
        
        print("Connection established with Dropbox")

    def search_dropbox(self, search):
    
        cFlag = False
        yFlag = False
        tFlag = False

        if(len(search.companies)>0):
            cFlag = True
        if(len(search.years)>0):
            yFlag = True
        if(len(search.type)>0):
            tFlag = True

        fileList = []

        if(yFlag == False) and (cFlag == False) and (tFlag == False):
            #searches recursively through the entire dropbox beginning at the root
            for entry in self.dbx.files_list_folder('', True).entries:
                if "." in entry.path_display:
                    fileList.append(entry)
    
        elif(yFlag == True) and (cFlag == False) and (tFlag == False):
            #searches through specific YEAR folders, but no specific companies
            for yearEntry in self.dbx.files_list_folder('').entries:
                if yearEntry.name in search.years:
                    for entry in self.dbx.files_list_folder(yearEntry.path_display, True).entries:
                        fileList.append(entry)
        
        elif(yFlag == False) and (cFlag == True) and (tFlag == False):
            #searches through specific company folders, but any year
            for yearEntry in self.dbx.files_list_folder('').entries:
                for companyEntry in self.dbx.files_list_folder(yearEntry.path_display).entries:
                    if companyEntry.name.lower() in search.companies:
                        for entry in self.dbx.files_list_folder(companyEntry.path_display).entries:
                            fileList.append(entry)

        elif(yFlag == False) and (cFlag == False) and (tFlag == True):
            #search for file type
            for typeEntry in self.dbx.files_list_folder('').entries:
                if typeEntry in self.dbx.files_list_folder(typeEntry.path_display, True).entries:
                    for entry in self.dbx.files_list_folder(companyEntry.path_display).entries:
                            fileList.append(entry)                 
                
        else:   #will need to search through only the years and companies specified by the user
            #searches through the YEAR folders in the Dropbox
            for yearEntry in self.dbx.files_list_folder('').entries:
                if yearEntry.name in search.years:
                    for companyEntry in self.dbx.files_list_folder(yearEntry.path_display).entries:
                        if companyEntry.name.lower() in search.companies:
                            for typeEntry in self.dbx.files_list_folder(yearEntry.path_display).entries:
                                if typeEntry in search.companies:
                                    for entry in self.dbx.files_list_folder(companyEntry.path_display).entries:
                                        fileList.append(entry)

        keywords = ' '.join(search.keywords)

        return BagOfWords(fileList, keywords).find_accurate_docs()


    def return_list_of_links(self, bestDocFileList):
        links = []
        for file in bestDocFileList:
            path = file.path_display
            links.append(self.dbx.sharing_create_shared_link(path).url)
        
        return links