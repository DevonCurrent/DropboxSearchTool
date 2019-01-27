from Message import Message
from ParseMessage import ParseMessage
from SlackBot import SlackBot
from DropboxBot import DropboxBot 

if __name__ == "__main__":
    token_file = open("Tokens.txt", 'r')
    tokens = (token_file.read()).split(' ')
    slack_token = tokens[0]
    dropbox_token = tokens[1]

    slack_bot = SlackBot(slack_token)
    dropbox_bot = DropboxBot(dropbox_token)

    while True:
        m = slack_bot.ListenForMessage()
        if m:
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
                    resp = str(len(file_list)) + " results found"
                    results_message = Message(resp, m.user, m.msg_id, m.channel)
                    slack_bot.SendSlackMessage(results_message)

                    links = dropbox_bot.ReturnListOfLinks(file_list)

                    for link in links:
                        link_message = Message(link, m.user, m.msg_id, m.channel)
                        slack_bot.SendSlackMessage(link_message)
