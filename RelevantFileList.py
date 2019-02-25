from BagOfWords import BagOfWords
import pdb

class RelevantFileList:

    def retrieve_relevant_files(dropboxBot, search):
        
        """
        Retrieves a list of files found on the Dropbox that are located in the specified companies and year fields.
        Keywords are not used to determine this list

        Parameters
        ----------
        dropboxBot : class 'DropboxBot.DropboxBot'
            an instance of DropboxBot that has access to the Dropbox account
        search : class 'Search.Search'
            Search object that contains tuples for keywords, companies, years, and specified searches by the Slack user

        Returns
        -------
        fileList
            A list of files found on the Dropbox that are located in the specified companies and year fields.
        """

        pdb.set_trace()
        dbx = dropboxBot.dbx
    
        cFlag = False
        yFlag = False

        if(len(search.companies)>0):
            cFlag = True
        if(len(search.years)>0):
            yFlag = True

        fileList = []

        if(yFlag == False) and (cFlag == False):
            #searches recursively through the entire dropbox beginning at the root
            for entry in dbx.files_list_folder('', True).entries:
                if "." in entry.path_display:
                    fileList.append(entry)
    
        elif(yFlag == True) and (cFlag == False):
            #searches through specific YEAR folders, but no specific companies
            for yearEntry in dbx.files_list_folder('').entries:
                if yearEntry.name in search.years:
                    for entry in dbx.files_list_folder(yearEntry.path_display, True).entries:
                        fileList.append(entry)
        
        elif(yFlag == False) and (cFlag == True):
            #searches through specific company folders, but any year
            for yearEntry in dbx.files_list_folder('').entries:
                for companyEntry in dbx.files_list_folder(yearEntry.path_display).entries:
                    if companyEntry.name.lower() in search.companies:
                        for entry in dbx.files_list_folder(companyEntry.path_display).entries:
                            fileList.append(entry)

        else:   #will need to search through only the years and companies specified by the user
            #searches through the YEAR folders in the Dropbox
            for yearEntry in dbx.files_list_folder('').entries:
                if yearEntry.name in search.years:
                    for companyEntry in dbx.files_list_folder(yearEntry.path_display).entries:
                        if companyEntry.name.lower() in search.companies:
                            for entry in dbx.files_list_folder(companyEntry.path_display).entries:
                                fileList.append(entry)


        keywords = ' '.join(search.keywords)

        return fileList