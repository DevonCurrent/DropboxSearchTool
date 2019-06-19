# Development Manual

## The technical aspects of the system
The source code has some technical aspects, and so it will be explained in full. Each file's documentation goes into more detail, but a general overview of the process will be explained in the order that a search is made by a user:

- DropboxSearchTool.py is the script that starts the server. It restarts the server if it is shut off for any reason.
  
- SearchMain handles each individual thread for searches made by users. This also handles instantiating the Slack bot and Dropbox bot, and returning information back through Slack.
  
- DropboxBot and SlackBot are instances of the Dropbox app and Slack bot respectively, that use the tokens provided in DropboxSearchTokens.txt
  
- When a message is sent on Slack on a channel that the Slack bot is listening to, ParseMessage will parse the message so that the bot can see if it is something it needs to respond to.
  
- Search.py will create a response to a correctly parsed message (if the tool needs to search Dropbox). Depending on the type of search requested by the Slack user, either FileContentSearch, FileNameSearch, FileSearch, or RecentFileSearch will run.
  
- If it is a recent file search, then it will return the N most recent files found on Dropbox.
  
- If it is any other search, then it will create a RelevantFileList, finding all files on Dropbox from within folders that the user requested. It also will remove any files that are not of the type requested (if no type is requested, then all files will be returned in the list).
  
- The FileContentSearch will have use a ContentParser to parse through the content within each file in the relevant file list. This is a huge list that is returned, that contains each files' full content. This list will then be passed to BagOfWords
  
- The FileNameSearch will not use the ContentParser, and will just use BagOfWords for each files' name.

- The FileSearch performs a FileContentSearch of the relevant files (which is then passed to BagOfWords), and will also do a FileNameSearch (which will be passed to another instance of BagOfWords). These two BagOfWords results are averaged together.

- BagOfWords is the most technical file in the system. It uses a StemmedCountVectorizer to stem all words down to their roots. This is to find words that are interchangeable in meaning (for example running and run). We then perform the BagOfWords algorithm - where we vectorize both the Slack user's search query, and vectorize each files names/content individually (depending on if it was a content search or name search). Each file name/content vector is then compared to the Slack user's vector, by finding the Euclidean distance between the two. We then normalize each distance (so we have a way to decide on 90% accuracy), and return the N files that have the highest accuracy. 

- The BagOfWords returns this list of accurate file hyperlinks to DropboxSearchMain, which then replies with a message of these links to the user on Slack.
  
> For a more in-depth explanation to how the algorithm works, it is posted here on [our google drive](https://docs.google.com/document/d/1Q5NSEFbU9fVL1gaqVjr9EgRihHHWIE1YURCX5Qoap2M/edit?usp=sharing)


## Replicating the dev environment
To replicate the environment, clone the [repo from here](https://github.com/DevonCurrent/DropboxSearchTool). The Slack and Dropbox OAuth tokens should already be available on the running server, and can be used. For development, though, a testing Slack bot and Dropbox should be used before integrating it into the system. It is explained in the Deployment Documentation on how to create the Slack bot and Dropbox app, but is also explained briefly below:
1. Go [here](https://api.slack.com/apps) and create new app. You may need to sign into Slack.
  
2. After naming the bot and setting its workplace to the testing Slack, click on "Bot Users" on the left-hand side. Create a bot user.
  
3. Click on "Install App" on the left-hand side, and authorize it to the testing Slack workspace.
  
4. Copy the Bot User OAuth Access Token (NOT THE OAuth Access Token above it!) and paste it to the first line of "DropboxSearchTokens.txt"
   
To create the Dropbox app, follow these instructions:

1. Go [here](https://www.dropbox.com/developers/apps) and click "create app". You may need to sign into a testing Dropbox account (or you can test on the intended Dropbox since no one will see the searches on Slack).
  
2. Choose "Dropbox API" -> "Full Dropbox" -> and give it a name. Then, click "create app"
  
3. Click "generate access token" and copy this to the second line of "DropboxSearchTokens.txt"


> When ready to integrate into the actual environment, create another Slack bot and Dropbox app and set them to the real Slack workspace and Dropbox.

Install any other dependencies that the DropboxSearchTool needs to run. Python 3 is required, and so run "python DropboxSearchTool.py" to start up the system. If it does not run, check to see what dependencies are missing.

## Folder structure
The documentation, presentations, and team meetings were a necessity for our class assignments. The documentation is useful for explaining how to replicate the environments, and how the tool works for users. The tests folder contains unit tests for most of the features.

The source code does not contain much folder structure, as we were originally unsure how to sort through the material by classification. The best structure that we have thought up would be to categorize files in the following structure:
- "SlackBot", "DropboxBot", "DropboxSearchTool", and "SearchMain" as the initialization of the tool.
- "Message", "ParseMessage", and "RelevantFileList" are the pre-processing files before making a search.
- "Search", "FileContentSearch", "FileNameSearch", "FileSearch", "ContentParser", and "SearchFeedback" would be the searching portion.
- "BagOfWords" and "StemmedCountVectorizer" would be stored under a folder for accuracy algorithm.

## Important files

- DropboxSearchTool.py is used to start the tool. It runs the SearchMain, and will check to make sure that no unforeseen error will occur that might shut down the system. This is dirty, but was the quick solution to solving the problem at the time, and there have been no known issues since implementing it.
- DropboxSearchTokens.txt store the Slack token on the first line, and then the Dropbox OAuth token on the second line. These are used so that this tool knows which Slack workspace to have the bot run on, and what Dropbox to search through. **It is important that these tokens stay secret to protect the confidentiality of the Dropbox.**
- The .gitignore is a standard gitignore file, that also includes to ignore the DropboxSearchTokens.txt file, so that the tokens are not pushed to Github.