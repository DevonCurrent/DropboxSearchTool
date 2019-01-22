from slackclient import SlackClient

class SlackBot:

    def __init__(self, token):
        self.t = token
        self.slackClient = SlackClient(self.t)

    def Connect(self):
        if not self.slackClient.rtm_connect(with_team_state=False):
            print("Connection could not be established")
            exit()
        
        print("Connection established with Slack")
        self.id = self.slackClient.api_call("auth.test")["user_id"]

    

