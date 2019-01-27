import dropbox
from dropbox.exceptions import AuthError

def CheckAgainstKeywords(file, keywords):
    file = file.lower()
    count = 0
    for i in keywords:
        i = i.lower()
        if i in file:
            count += 1
    return count
    
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

    def SearchDropbox(self, search):
        cFlag = False
        yFlag = False

        if(len(search.companies)>0):
            cFlag = True
        if(len(search.years)>0):
            yFlag = True

        fileList = []

        if(yFlag == False) and (cFlag == False):
            #searches recursively through the entire dropbox beginning at the root
            for entry in self.dbx.files_list_folder('', True).entries:
                if "." in entry.path_display:
                    count = CheckAgainstKeywords(entry.name, search.keywords)
                    if count != 0:
                        fileList.append([entry, count])
    
        elif(yFlag == True) and (cFlag == False):
            #searches through specific YEAR folders, but no specific companies
            for yearEntry in self.dbx.files_list_folder('').entries:
                if yearEntry.name in search.years:
                    for entry in self.dbx.files_list_folder(yearEntry.path_display, True).entries:
                        count = CheckAgainstKeywords(entry.name, search.keywords)
                        if count != 0:
                            fileList.append([entry, count])
        
        elif(yFlag == False) and (cFlag == True):
            #searches through specific company folders, but any year
            for yearEntry in self.dbx.files_list_folder('').entries:
                for companyEntry in self.dbx.files_list_folder(yearEntry.path_display).entries:
                    if companyEntry.name.lower() in search.companies:
                        for entry in self.dbx.files_list_folder(companyEntry.path_display).entries:
                            count = CheckAgainstKeywords(entry.name, search.keywords)
                            if count != 0:
                                fileList.append([entry, count])
                
        else:   #will need to search through only the years and companies specified by the user
            #searches through the YEAR folders in the Dropbox
            for yearEntry in self.dbx.files_list_folder('').entries:
                if yearEntry.name in search.years:
                    for companyEntry in self.dbx.files_list_folder(yearEntry.path_display).entries:
                        if companyEntry.name.lower() in search.companies:
                            for entry in self.dbx.files_list_folder(companyEntry.path_display).entries:
                                count = CheckAgainstKeywords(entry.name, search.keywords)
                                if count != 0:
                                    fileList.append([entry, count])

        return fileList

        