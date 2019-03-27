from Message import Message
from ParseMessage import parse_message
from SlackBot import SlackBot
from DropboxBot import DropboxBot
import FileSearch
import threading

"""
    Main Class used to start the bot and receive searches
    -----
    Methods
    -----
    search_thread(slackBot, dropboxBot, fileSearch, m)
        takes search entered and returns the output to the user
"""

def search_thread(slackBot, dropboxBot, m):
    """
        takes search entered and returns the output to the user

        Parameters
        ----------
        slackBot: class 'slackBot.SlackBot'
            an instance of Slack that has access to the slack account
        dropboxBot:class 'dropboxBot.DropboxBot'
            an instance of DropboxBot that has access to the Dropbox account
        m:
            Message instance
    """

    search = parse_message(dropboxBot, m)

    searchResult = search.dropbox_search(dropboxBot)

    if(type(searchResult) == str):
        resp = Message(searchResult, m.user, m.msgID, m.channel)
        slackBot.send_slack_message(resp)

    else:
        # This should be sent after it is known that it is a search request and before the search request is done (maybe within Search?)
        # Should be formatted so that it only displays the chosen options
        searchConfirm = "Ok! I will search for " + str(search.keywords).strip('[]') + " \nfrom " + str(search.companies).strip('[]') + " \nfrom the year(s) " + str(search.years).strip('[]')
        searchConfirmMsg = Message(searchConfirm, m.user, m.msgID, m.channel)
        slackBot.send_slack_message(searchConfirmMsg)

        if (searchResult is None):
            noResultsMessage = Message("No results found", m.user, m.msgID, m.channel)
            slackBot.send_slack_message(noResultsMessage)
        else:
            resp1 = str(len(searchResult)) + " results found"
            resultsMessage1 = Message(resp1, m.user, m.msgID, m.channel)
            slackBot.send_slack_message(resultsMessage1)
            
            links = search.retrieve_hyperlink_list(dropboxBot, searchResult)

            for link in links:
                linkMessage = Message(link, m.user, m.msgID, m.channel)
                slackBot.send_slack_message(linkMessage)

if __name__ == "__main__":

    slackBot = SlackBot()
    dropboxBot = DropboxBot()

    print("The program can now receive search queries")

    while True:
        m = slackBot.listen_for_message()
      
        if m is not None:
            """
            threading.Thread(target=search_thread,
                args=(slackBot, dropboxBot, m)).start()
            """
            search_thread(slackBot, dropboxBot, m)
            
