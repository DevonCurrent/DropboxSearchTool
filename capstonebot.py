import os
import time
import re
import MessageParser
from slackclient import SlackClient
import pdb

# instantiate Slack client
slackClient = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
# starterbot's user ID in Slack: value is assigned after the bot starts up
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

if __name__ == "__main__":
    if slackClient.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slackClient.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slackClient.rtm_read())
            if command:
                urlList = MessageParser.parse_message(slackClient, command, channel)

                if len(urlList) == 0:
                    slackClient.api_call(
                        "chat.postMessage",
                        channel=channel,
                        text="Sorry! I wasn't able to find anything related to that search."
                    )
                else:
                    for url in urlList:
                        slackClient.api_call(
                            "chat.postMessage",
                            channel=channel,
                            text=url
                        )
                print("This search is done. Another search may now happen.")

            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")