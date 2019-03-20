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

        pathList = []
        fileList = []

        for entry in dropboxbot.dbx.files_list_folder('',True).entries:
            if '.' in entry.path_display:
                path = entry.path_display.split('/')

                #removes empty first element
                path.pop(0)

                pathList.append(path)

        if yFlag:
            filtered_pathList = [(x,y,z) for (x,y,z) in pathList if x in search.years]
            pathList = filtered_pathList
        
        if cFlag:
            filtered_pathList = [(x,y,z) for (x,y,z) in pathList if y in search.companies]
            pathList = filtered_pathList

        for path in pathList:
            fileList.append(path[2])

        return fileList