from ParseMessage import ParseMessage
from SlackBot import SlackBot

if __name__ == "__main__":
    token_file = open("Tokens.txt", 'r')
    tokens = (token_file.read()).split(' ')
    slack_token = tokens[0]
    dropbox_token = tokens[1]

    slack_bot = SlackBot(slack_token)
    slack_bot.Connect()

    while True:
        m = slack_bot.ListenForMessage()
        if m:
            error, message = ParseMessage(m)

            #if error:
                

