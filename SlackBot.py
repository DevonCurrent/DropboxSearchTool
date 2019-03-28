from Message import Message
from slackclient import SlackClient

class SlackBot:
    """
    Class that initializes the slackbot
     -----
    Attributes
    -----
    slackClient: string
        the slackbot token
    id: user string
        the slack user id
    -----
    Methods
    -----
    listen_for_message(self)
        listens for a message sent by a user
    send_slack_message(self, message)
        sends the message necessary back to the user
    """
    def __init__(self):
        slackToken = open("DropboxSearchTokens.txt").readline().rstrip()

        self.slackClient = SlackClient(slackToken)

        if not self.slackClient.rtm_connect(with_team_state=False):
            print("Connection could not be established")
            exit()
        
        self.id = self.slackClient.api_call("auth.test")["user_id"]
        print("Connection established with Slack")
        
        #found where to put the greeting, not sure how to make it so the bot says it to the user
        greeting="If you need to search for files start a direct message with me and use the following commands: \n -k for a specific keyword. \n -kn for a file's name. \n -kc for a file's content. \n -c for the company the file was made for. \n -y for the year the file was created. \n -t for a file type. \n -r for recently edited files."
        self.slackClient.api_call('chat.postMessage', channel='#general', text=greeting)

    def listen_for_message(self):
        """
        listens for a message sent by a user

        Returns
        -------
        message
            the message initialized with this information
        """
        for event in self.slackClient.rtm_read():
            if event["type"] == "message" and not "subtype" in event:
                message = Message(event["text"], event["user"], event["client_msg_id"], event["channel"])
                return message

    def send_slack_message(self, message):
        """
        sends the message necessary back to the user

        Parameters
        ----------
        message: string
            message that is entered by the user

        """
        self.slackClient.api_call(
            "chat.postMessage",
            channel=message.channel,
            text=message.text
        )
