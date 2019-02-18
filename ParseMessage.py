from Message import Message
from Search import Search
from DropboxBot import DropboxBot

def parse_message(dropboxBot, message):

    delimitedSearch = message.text.split("-")
    search = Search()
    
    for value in delimitedSearch:
        if value:
            if value[0] == 'f':
                if value[1] == 'c':
                    search.fileContentSearch = True
                if value[1] == 't':
                    search.add_type(value)
                search.add_keywords(value)

            elif value[0] == 'c':
                search.add_companies(value)

            elif value[0] == 'y':
                search.add_years(value)

            elif value[0] == 'h':
                return True, "To search for files use the following commands: \n -fn for a file's name. \n -c for the company the file was made for. \n  -y for the year the file was created \n -ft for the file type."
            
            elif value[0] == 'r':
                return True, DropboxBot.recent_search(dropboxBot)

    #keywords are needed, or there is no way to know what the user wants to search for. Anything else is optional
    if(search.keywords == []):
        return True, "Not sure what you mean. Please make sure that you typed it correctly. Example: -fn cool -y 2014* -c google* where * is optional"
    elif (search.fileContentSearch == True):
        return True, "Sorry! I do not have that functionality yet!"

    search.create_correct_search_response()

    return False, search

    
    

