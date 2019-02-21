# DropboxSearchTool

##### Developed by: Ryan Ahler, Devon Current, Allison Hartman

This is a capstone project for Ball State University. This search tool uses a Slack interface to search for and access files on a Dropbox. This is intended for searching through over 10,000 files that contain matches to keywords made to a Slack bot. It is created in Python using the [Slack API](https://github.com/slackapi/python-slackclient) and the [Dropbox sdk](https://github.com/dropbox/dropbox-sdk-python).

### Setting Up On A Server
A server is needed to host the Slack bot that interacts with messages, and to host a Dropbox app that contains the token to access a Dropbox. Both of these utilize OAuth2 token verification, and you can generate your own by [creating a Slack bot](https://api.slack.com/apps) as well as [creating a Dropbox app](https://www.dropbox.com/developers/apps). When running the CapstoneBotMain.py, it will request a .txt file with the tokens (Slack on the first line, Dropbox on the second, extra line), and will then run in the background. You can test it is working by inviting your Slack bot to a Slack channel on your workspace, and messaging it.

### Completed User Stories
- As a session leader, I want to message a bot in a Slack channel and receive a reply.
- When I message the bot '-fn money' the bot will return files on the Dropbox that have the keyword 'money' in the file's name.
- If I message '-fn money -c IBM Google' the bot will only return files from the google and ibm folder that match the keyword.
- If I message '-fn money -c ibm google -y 2014 2015' it will only return files from the companies inside of the 2014 and 2015 folders of Dropbox.
- I want to be able to message '-fn money -c ibm -y 2014' and '-y 2014 -fn moneY -c IbM' and receive the same files from the respective folders.
- I want the bot to tell me what it is searching for on Dropbox while I wait for feedback.
- If I enter an incorrect command, the bot will tell me how to correctly enter it.

### Future User Stories
- As a session leader, I want to message the bot '-fc money' to receive a list of all files that contain 'money' inside of the file's content.
- I want to be able to use '-fc keyword' or -'fn keyword' to search for a keyword by the file's name or content.
- I want the keywords to be weighted based on either training data, or by the amount of syllables in the word.
- When I message the bot for files, I want to be able to access the most recent file that contained a given keyword.
- (unsure) When I search for the keyword 'running', I want the keyword to be broken down to it's root when searching (ex: run) so that the search accuracy will be higher and more files can be found that match.
- (unsure) When I messag the bot, I want it to return a link to a webpage that contains the list of all files found that match the keyword.
- (unsure) I want the webpage to contain information about each file stating how many matches were found, when it was created, and where it is located in the Dropbox.
