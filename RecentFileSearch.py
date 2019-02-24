class RecentFileSearch:

    def recent_file_search(dropboxBot):

        dbx = dropboxBot.dbx

        mostRecentFile = None
        bestTimeTuple = None

        #searches recursively through the entire dropbox beginning at the root
        for entry in dbx.files_list_folder('', True).entries:
            if "." in entry.path_display:
                timeTuple = entry.client_modified.timetuple()

                if(bestTimeTuple == None):
                    bestTimeTuple = timeTuple
                    mostRecentFile = entry

                if(timeTuple.tm_year > bestTimeTuple.tm_year):
                    bestTimeTuple = timeTuple
                    mostRecentFile = entry

                elif(timeTuple.tm_year == bestTimeTuple.tm_year):
                    if(timeTuple.tm_yday > bestTimeTuple.tm_yday):
                        bestTimeTuple = timeTuple
                        mostRecentFile = entry
                    
                    elif(timeTuple.tm_yday == bestTimeTuple.tm_yday):
                        if(timeTuple.tm_hour > bestTimeTuple.tm_hour):
                            bestTimeTuple = timeTuple
                            mostRecentFile = entry

        return [mostRecentFile]