# DropboxSearchTool

##### Developed by: Ryan Ahler, Devon Current, Allison Hartman

This is a capstone project for Ball State University. This search tool uses a Slack interface to search for and access files on a Dropbox. This is intended for searching through over 10,000 files that contain matches to keywords made to a Slack bot. It is created in Python using the [Slack API](https://github.com/slackapi/python-slackclient) and the [Dropbox sdk](https://github.com/dropbox/dropbox-sdk-python).

### Setting Up On A Server
A server is needed to host the Slack bot that interacts with messages, and to host a Dropbox app that contains the token to access a Dropbox. Both of these utilize OAuth2 token verification, and you can generate your own by [creating a Slack bot](https://api.slack.com/apps) as well as [creating a Dropbox app](https://www.dropbox.com/developers/apps). When running the CapstoneBotMain.py, it will request a search for a .txt file with the re and will then run in the background. You can test it is working by inviting your Slack bot to a Slack channel on your workspace, and messaging it.

### Completed User Stories
#### Iteration 1
- As a session leader, I want to message a bot in a Slack channel and receive a reply.
- When I message the bot '-fn money' the bot will return files on the Dropbox that have the keyword 'money' in the file's name.
- If I message '-kn money -c IBM Google' the bot will only return files from the google and ibm folder that match the keyword.
- If I message '-kn money -c ibm google -y 2014 2015' it will only return files from the companies inside of the 2014 and 2015 folders of Dropbox.
- I want to be able to message '-kn money -c ibm -y 2014' and '-y 2014 -fn moneY -c IbM' and receive the same files from the respective folders.
- I want the bot to tell me what it is searching for on Dropbox while I wait for feedback.
- If I enter an incorrect command, the bot will tell me how to correctly enter it.

#### Iteration 2
- I want to be able to ask the Slack bot for help where it explains the options for using this search tool.
- As a session leader, I want to message the bot '-fc money' to receive a list of all files that contain 'money' inside of the file's content.
- I want to be able to use '-fn keyword' or -'fc keyword' to search for a keyword by the file's name or content.
- When I message the bot for files, I want to be able to access the most recent file that contained a given keyword.
- I want to be able to search through Dropbox for PDF, Excel, Word, PPT, and other Microsoft files by content and file name.
- I want the keywords to be weighted based on either training data, or by the amount of syllables in the word.
- When I search for the keyword 'running', I want the keyword to be broken down to it's root when searching (ex: run) so that the search accuracy will be higher and more files can be found that match.
- I want to have an option to search for files based on both their name and their content weighted together.

### Iteration 3
- I want to be able to make filename search, file content search, or a file content and name search.
- When I type in the Slack query "-r", I expect to see the top N most recent files that have been created/changed on dropbox
- I want FileSearches to be able to search for files weighted by both their name and content.
- When I type in the Slack query "-f money -t doc ppt" I want to be able to search for files related to 'money' that are only of the file types 'doc' or 'ppt'
- I want to be able to search through Dropbox files as quickly as possible, since there are many files to potentially search through

### Iteration 4
- I want to be able to run this system without it crashing, or having errors that cause someone to have to restart the server.
- I want feedback that tells me how much longer I have to wait on a search until I get a result.
- I want to be able to run this DropboxSearchTool on a MacOS computer, and search through the intended Dropbox from TDG.
- When I run on an Apple or Windows OS, I expect to be able to easily install this tool with instructions to follow.
- When future developers take over this project, they should find commented code detailing what each class is doing, as well as developer documentation explaining a hierarchical overview of the code structure.
- If I am stuck and do not understand how to use this tool, I can refer to documentation that explains the functionality.
- When I make a search query on Slack, it should be formatted to use '-l' for folders (which are more general), instead of '-c' or '-y' for companies and years (which is too specific).
