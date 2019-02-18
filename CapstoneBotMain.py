from Message import Message
from ParseMessage import parse_message
from SlackBot import SlackBot
from DropboxBot import DropboxBot
import threading

def search_thread(slackBot, dropboxBot, m):
    error, search = parse_message(dropboxBot, m)
    
    if error:
        errorMessage = Message(search, m.user, m.msgID, m.channel)
        slackBot.send_slack_message(errorMessage)
    else:
        bestDocFileList = dropboxBot.search_dropbox(search)

        if len(bestDocFileList) < 1:
            noResultsMessage = Message("No results found", m.user, m.msgID, m.channel)
            slackBot.send_slack_message(noResultsMessage)
        else:
            resp1 = str(len(bestDocFileList)) + " results found"
            resp2 = "Ok! I will search for " + str(search.keywords).strip('[]') + " \nfrom " + str(search.companies).strip('[]') + " \nfrom the year(s) " + str(search.years).strip('[]')
            resultsMessage1 = Message(resp1, m.user, m.msgID, m.channel)
            slackBot.send_slack_message(resultsMessage1)
            resultsMessage2 = Message(resp2, m.user, m.msgID, m.channel)
            slackBot.send_slack_message(resultsMessage2)

            links = dropboxBot.return_list_of_links(bestDocFileList)

            for link in links:
                linkMessage = Message(link, m.user, m.msgID, m.channel)
                slackBot.send_slack_message(linkMessage)

if __name__ == "__main__":
    
    slackToken = input("Enter a valid Slack OAuth2 token: ")
    dropboxToken = input("Enter a valid Dropbox OAuth2 token: ")
    

    slackBot = SlackBot(slackToken)
    dropboxBot = DropboxBot(dropboxToken)

    print("The program can now receive search queries")

    while True:
        m = slackBot.listen_for_message()
        
        if m is not None:
            threading.Thread(target=search_thread,
                args=(slackBot, dropboxBot, m)).start()
            
