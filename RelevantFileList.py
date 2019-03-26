from BagOfWords import BagOfWords
import pdb

class RelevantFileList:
    """
    Class used to represent the relevent files to find based on the search the user enters
    -----
    Methods
    -----
    retrieve_relevant_files(dropboxBot, search)
        Retrieves a list of files found on the Dropbox that are located in the specified companies and year fields.
        Keywords are not used to determine this list
    """

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
        tFlag = False

        if(len(search.companies)>0):
            cFlag = True
        if(len(search.years)>0):
            yFlag = True
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

        if yFlag:
            filtered_entryList = [(year,x,y,z) for (year,x,y,z) in entryList if year in search.years]
            entryList = filtered_entryList
        
        if cFlag:
            filtered_entryList = [(v,comp,y,z) for (v,comp,y,z) in entryList if comp in search.companies]
            entryList = filtered_entryList

        if tFlag:
            filtered_entryList = [(v,x,types,z) for (v,x,types,z) in entryList if types in search.types]
            entryList = filtered_entryList

        for entry in entryList:
            fileList.append(entry[3])

        return fileList