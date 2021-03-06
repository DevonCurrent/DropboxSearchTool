from Message import Message
from Search import Search
from DropboxBot import DropboxBot
import pdb

"""
    Parses the message entered by the users
    -----
    Methods
    -----
    split_search_terms(search, value, letter)
        splits the entered search terms based on the different key words
    parse_message(dropboxBot, message)
        Parses a message to create a Search object that can be used to determine the correct search algorithm
        to find the appropriate file.
"""

def split_search_terms(search, value, letter):
        """
        splits the entered search terms based on the different key words

        Parameters
        ----------
        search: string
            the search entered by the user
        value: string
            value of the tag
        letter: letter
            tag used to differentiate the search

        """
        separated_keywords = value.split(" ")
        separated_keywords = [term.lower() for term in separated_keywords]
        for i in range(1, len(separated_keywords)):
            if letter is 'f':
                search.keywords.append(separated_keywords[i])
            elif letter is 'l':
                search.folders.append(separated_keywords[i])
            elif letter is 't':
                if(separated_keywords[i].startswith(".")):
                    separated_keywords[i] = separated_keywords[i].split(".")[1]
                search.types.append(separated_keywords[i])

        if letter is 'f':
            if '' in search.keywords:  # removes blank space at the end of a search
                search.keywords.remove('')
        elif letter is 'l':
            if '' in search.folders:  # removes blank space at the end of a search
                search.folders.remove('')
        elif letter is 't':
            if '' in search.types:  # removes blank space at the end of a search
                search.types.remove('')


def parse_message(dropboxBot, message):

    """
    Parses a message to createa a Search object that can be used to determine the correct search algorithm
    to find the appropriate file.

    Parameters
    ----------
    dropboxBot : class 'DropboxBot.DropboxBot'
        an instance of DropboxBot that has access to the Dropbox account
    message : class 'Message.Message'
        A Message object that stores the text, channel, and user so that the SlackBot can respond to the user.

    Returns
    -------
    Search
        A Search object that stores Slack user message metadata, which can then be passed onto the appropriate 
        search algorithm, or return a message to the user.
    """

    delimitedSearch = message.text.split("-")
    search = Search()
    
    for value in delimitedSearch:
        if value:
            if value[0] == 'f':
                split_search_terms(search, value, 'f')
                if value[1] == 'n':
                    search.fn = True
                elif value[1] == 'c':
                    search.fc = True

            elif value[0] == 'l':
                split_search_terms(search, value, 'l')

            elif value[0] == 't':
                split_search_terms(search, value, 't')

            elif value[0] == 'h':
                search.help = True

            elif value[0] == 'r':
                search.recentFileSearch = True

    return search