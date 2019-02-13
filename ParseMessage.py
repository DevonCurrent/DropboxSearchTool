from Message import Message
from Search import Search

def parse_message(message):

    delimitedSearch = message.text.split("-")
    search = Search()
    
    for value in delimitedSearch:
        if value:
            if value[0] == 'f':
                if value[1] == 'c':
                    search.fileContentSearch = True
                search.add_keywords(value)

            elif value[0] == 'c':
                search.add_companies(value)

            elif value[0] == 'y':
                search.add_years(value)

    #keywords are needed, or there is no way to know what the user wants to search for. Anything else is optional
    if(search.keywords == []):
        return True, "Not sure what you mean. Please make sure that you typed it correctly. Example: -fn cool -y 2014* -c google* where * is optional"
    elif (search.fileContentSearch == True):
        return True, "Sorry! I do not have that functionality yet!"

    search.create_correct_search_response()

    return False, search

    
    

