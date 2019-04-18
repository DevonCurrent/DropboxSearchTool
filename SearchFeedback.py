import time
from Message import Message

class SearchFeedback:

    def search_feedback(ContentParser, fileListLength, slackBot, m):
        """
        Sends feedback to the Slack user that made the request, so they know how long they will have to wait for their search

        Parameters
        ----------
        contentParser : Object
            the parser that parses all relevant files' content, to be used for comparing to the slack user's search to find
            relevant search results. Tracks the number of parsed files so far.
        fileListLength : int
            the number of files that must be parsed
        slackBot : Object
            the slack bot that interfaces with the Slack user
        m : Object
            contains the original message that the user sent to the slack bot. This contains the channel to send feedback to,
            as well as the user that requested the search.
        """
        percentParsed = 0
        prevTimestamp = None
        while percentParsed < 100:
            numParsed = ContentParser.numberParsed
            percentParsed = (numParsed/fileListLength)*100
            if percentParsed != 100:
            
                feedbackProgress = "The search is at " + str(int(percentParsed)) + "%"
                
                try:
                    slackBot.slackClient.api_call(
                        "chat.delete",
                        channel=m.channel,
                        ts=prevTimestamp
                    )
                except Exception as exc:
                    pass

                feedbackMsg = slackBot.slackClient.api_call(
                    "chat.postMessage",
                    channel=m.channel,
                    text=feedbackProgress
                )

                prevTimestamp = feedbackMsg.get('ts')
            
                time.sleep(10)