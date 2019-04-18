from BagOfWords import BagOfWords
import pdb

class RelevantFileList:

    def retrieve_relevant_files(dropboxBot, search):
        
        """
        Retrieves a list of files found on the Dropbox that are located in the specified folders.
        Keywords are not used to determine this list

        Parameters
        ----------
        dropboxBot : class 'DropboxBot.DropboxBot'
            an instance of DropboxBot that has access to the Dropbox account
        search : class 'Search.Search'
            Search object that contains tuples for keywords, specified folders, and specified searches by the Slack user

        Returns
        -------
        fileList
            A list of files found on the Dropbox that are located in the specified companies and year fields.
        """

        dbx = dropboxBot.dbx
    
        fFlag = False
        tFlag = False

        if(len(search.folders)>0):
            fFlag = True
        if(len(search.types)>0):
            tFlag = True

        entryList = []
        fileList = []

        for entry in dbx.files_list_folder('',True).entries:
            if '.' in entry.path_display:
                path = entry.path_display.split('/')

                path.pop(0) #removes empty first element
                path[1] = path[1].lower() # lowercase the company names so they will match search.companies
                path[-1] = path[-1].split('.')[-1] # last element is file extension (type)

                path.append(entry) # add file metadata
                entryList.append(path)

        # looks at all parent folders of a file. Checks to see if one of the folders is related to the folder parameter the user wanted
        if fFlag:
            filtered_entryList = []
            for entry in entryList:
                for folder in entry[0:-2]:
                    folder = folder.lower()
                    folder = folder.replace(" ", "_") # possible solution for folders that have spaces in their name. Example: "r8 Folder"
                    if(folder in search.folders):
                        filtered_entryList.append(entry)
            entryList = filtered_entryList

        if tFlag:
            filtered_entryList = [(x,types,z) for (x,types,z) in entryList if types in search.types]
            entryList = filtered_entryList

        for entry in entryList:
            fileList.append(entry[-1])

        return fileList