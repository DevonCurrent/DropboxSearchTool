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

        entryList = []
        fileList = []

        for entry in dbx.files_list_folder('',True).entries:
            if '.' in entry.path_display:
                path = entry.path_display.split('/')
                path.append(entry)
                #removes empty first element
                path.pop(0)

                entryList.append(path)

        if yFlag:
            filtered_entryList = [(year,_,_,_) for (year,_,_,_) in entryList if year in search.years]
            entryList = filtered_entryList
        
        if cFlag:
            filtered_entryList = [(_,comp,_,_) for (_,comp,_,_) in entryList if comp in search.companies]
            entryList = filtered_entryList

        for entry in entryList:
            fileList.append(entry[3])

        return fileList