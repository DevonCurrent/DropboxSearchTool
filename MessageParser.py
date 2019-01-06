import os
import time
import re
import DropboxTool
from slackclient import SlackClient
import pdb

def setup_search(value, searchTerm):
    splitSearchTerms = value.split(" ")
    for i in range(1, len(splitSearchTerms)):
        searchTerm.append(splitSearchTerms[i])
    if '' in searchTerm:  # removes blank space at the end of a search
        searchTerm.remove('')


def parse_message(slack_client, command, channel):
    """
        Executes bot command if the command is known
    """    

    # Sets all search terms to none for a new search
    keywords = []
    companies = []
    years = []

    # Finds and executes the given command, filling in response
    response = ""
    # -k keywords -y year -c company
    delimited_search = command.split("-")
    for value in delimited_search:
        if value:
            if value[0] == 'k':
                setup_search(value, keywords)

            elif value[0] == 'c':
                setup_search(value, companies)

            elif value[0] == 'y':
                setup_search(value, years)

    #keywords are needed, or there is no way to know what the user wants to search for. Anything else is optional
    if(keywords == []):
        response = "Not sure what you mean. Please make sure that you typed it correctly. Example: -k leadership -y 2014* -c Microsoft* where * is optional"
        # Sends the response back to the channel
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )

    else:
        response = "Ok! I will search for " + str(keywords).strip('[]') + " \nfrom " + str(companies).strip('[]') + " \nfrom the year(s) " + str(years).strip('[]')
        # Sends the response back to the channel
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=response
        )
        fileList = DropboxTool.search_dropbox(keywords, companies, years)