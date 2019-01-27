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
                


                

