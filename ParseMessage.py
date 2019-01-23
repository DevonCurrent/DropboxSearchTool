from Message import Message

def setup_search(value, searchTerm):
    splitSearchTerms = value.split(" ")
    splitSearchTerms = [term.lower() for term in splitSearchTerms]
    for i in range(1, len(splitSearchTerms)):
        searchTerm.append(splitSearchTerms[i])
    if '' in searchTerm:  # removes blank space at the end of a search
        searchTerm.remove('')

def ParseMessage(message):

    keywords = []
    companies = []
    years = []
    fileContentSearch = False

    delimited_search = message.text.split("-")
    
    for value in delimited_search:
        if value:
            if value[0] == 'f':
                if value[1] == 'c':
                    fileContentSearch = True
                setup_search(value, keywords)

            elif value[0] == 'c':
                setup_search(value, companies)

            elif value[0] == 'y':
                setup_search(value, years)

    #keywords are needed, or there is no way to know what the user wants to search for. Anything else is optional
    if(keywords == []):
        return True, "Not sure what you mean. Please make sure that you typed it correctly. Example: -fn cool -y 2014* -c google* where * is optional"
    else if filteContentSearch:
        return True, "Sorry! I do not have that functionality yet!"

    
    

