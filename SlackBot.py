from Message import Message
from slackclient import SlackClient

class SlackBot:

    def __init__(self, token):
        self.t = token
        self.slackClient = SlackClient(self.t)

        if not self.slackClient.rtm_connect(with_team_state=False):
            print("Connection could not be established")
            exit()
        
        print("Connection established with Slack")
        self.id = self.slackClient.api_call("auth.test")["user_id"]      

    def ListenForMessage(self):
        for event in self.slackClient.rtm_read():
            if event["type"] == "message" and not "subtype" in event:
                message = Message(event["text"], event["user"], event["client_msg_id"], event["channel"])
                return message

    def SendSlackMessage(self, message):
        self.slackClient.api_call(
            "chat.postMessage",
            channel=message.channel,
            text=message.text
        )
