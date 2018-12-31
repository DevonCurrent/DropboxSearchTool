import os
import time
import re
import DropboxTool
from slackclient import SlackClient
import pdb

def parse_message(slack_client, command, channel):
    """
        Executes bot command if the command is known
    """    
    # Default response is help text for the user
    default_response = "Not sure what you mean. Please make sure that you typed it correctly. Example: -k leadership -y 2014* -c Microsoft* where * is optional"

    # Finds and executes the given command, filling in response
    response = None
    print(command)
    # -k keywords -y year -c company
    delimited_search = command.split("-")
    for value in delimited_search:
        # Apparently Python lacks a switch statement
        # implements keywords, year, company
        if value:
            if value[0] == 'k':
                split_keywords = value.split(" ")
                for i in range(1, len(split_keywords)):
                    keywords.append(split_keywords[i])
            elif value[0] == 'c':
                global comp
                global cFlag
                cFlag = True
                comp = value[2:]
                if comp[len(comp) - 1] == " ":
                    comp = comp[0:len(comp) - 1]
            elif value[0] == 'y':
                global year
                global yFlag
                cFlag = True
                year = value[2:]
                if year[len(year) - 1] == " ":
                    year = year[0:len(year) - 1]
            else:
                response = "Not sure what you mean. Please make sure that you typed it correctly. Example: -k leadership -y 2014* -c Microsoft* where * is optional"

    # Sends the response back to the channel
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )