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

        dbx = dropboxBot.dbx
    
        cFlag = False
        yFlag = False

        if(len(search.companies)>0):
            cFlag = True
        if(len(search.years)>0):
            yFlag = True

        fileList = []
        pathList = []

        for entry in dbx.files_list_folder('', True).entries:
            #Checks only files, no folders
            if "." in entry.path_display:
                path = entry.path_display.split('/')

                #removes empty first element
                path.pop(0)
                path.append(entry)
                pathList.append(path)

        if yFlag:
            for path in pathList:
                if path[0] not in search.years:
                    pathList.remove(path)

        if cFlag:
            for path in pathList:
                if path[1] not in search.companies:
                    pathList.remove(path)    


        for path in pathList:
            fileList.append(path[3])
    
        return fileList