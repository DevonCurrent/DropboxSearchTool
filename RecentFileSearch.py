class RecentFileSearch:
    """
    Class used to represent the recent files searched
    -----
    Methods
    -----
    recent_file_search(dropboxBot)
        returns the the 5 most recently edited file in the dropbox
    """
    def recent_file_search(dropboxBot):
        """
        returns the the 5 most recently edited file in the dropbox

        Parameters
        ----------
        dropboxBot : class 'DropboxBot.DropboxBot'
            an instance of DropboxBot that has access to the Dropbox account

        Returns
        -------
        mostRecentFiles
            List of most recently edited files
        """
        NUM_FILES = 5
        dbx = dropboxBot.dbx
        mostRecentFiles = []
        dropboxEntries = dbx.files_list_folder('', True).entries # makes a copy so that we can remove the most recent entries

        for num in range(0, NUM_FILES):
            bestTimeTuple = None
            possibleMostRecent = None

            #searches recursively through the entire dropbox beginning at the root
            for entry in dropboxEntries:
                if "." in entry.path_display:
                    timeTuple = entry.client_modified.timetuple()

                    if(bestTimeTuple == None):
                        bestTimeTuple = timeTuple
                        possibleMostRecent = entry

                    if(timeTuple.tm_year > bestTimeTuple.tm_year):
                        bestTimeTuple = timeTuple
                        possibleMostRecent = entry

                    elif(timeTuple.tm_year == bestTimeTuple.tm_year):
                        if(timeTuple.tm_yday > bestTimeTuple.tm_yday):
                            bestTimeTuple = timeTuple
                            possibleMostRecent = entry

                    elif(timeTuple.tm_yday == bestTimeTuple.tm_yday):
                        if(timeTuple.tm_hour > bestTimeTuple.tm_hour):
                            bestTimeTuple = timeTuple
                            possibleMostRecent = entry

            mostRecentFiles.append(possibleMostRecent)
            dropboxEntries.remove(possibleMostRecent)

        return mostRecentFiles