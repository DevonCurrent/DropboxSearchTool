from Message import Message
from ParseMessage import ParseMessage
from SlackBot import SlackBot
from DropboxBot import DropboxBot
import threading

def SearchThread(slack_bot, dropbox_bot, m):
    error, search = ParseMessage(m)

    if error:
        error_message = Message(search, m.user, m.msg_id, m.channel)
        slack_bot.SendSlackMessage(error_message)
    else:
        file_list = dropbox_bot.SearchDropbox(search)

        if len(file_list) < 1:
            no_results_message = Message("No results found", m.user, m.msg_id, m.channel)
            slack_bot.SendSlackMessage(no_results_message)
        else:
            resp_1 = str(len(file_list)) + " results found"
            resp_2 = "Ok! I will search for " + str(search.keywords).strip('[]') + " \nfrom " + str(search.companies).strip('[]') + " \nfrom the year(s) " + str(search.years).strip('[]')
            results_message_1 = Message(resp_1, m.user, m.msg_id, m.channel)
            slack_bot.SendSlackMessage(results_message_1)
            results_message_2 = Message(resp_2, m.user, m.msg_id, m.channel)
            slack_bot.SendSlackMessage(results_message_2)

            links = dropbox_bot.ReturnListOfLinks(file_list)

            for link in links:
                link_message = Message(link, m.user, m.msg_id, m.channel)
                slack_bot.SendSlackMessage(link_message)

if __name__ == "__main__":
    
    slack_token = input("Enter a valid Slack OAuth2 token: ")
    dropbox_token = input("Enter a valid Dropbox OAuth2 token: ")
    

    slack_bot = SlackBot(slack_token)
    dropbox_bot = DropboxBot(dropbox_token)

    print("The program can now recieve search queries")

    while True:
        m = slack_bot.ListenForMessage()
        
        if m is not None:
            threading.Thread(target=SearchThread,
                args=(slack_bot, dropbox_bot, m)).start()
            
