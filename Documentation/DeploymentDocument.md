# Setting up and Maintenance Documentation

## Section 1 Here are the steps to install the program:

> This is assuming that you are running on a Mac. If you are running on Windows/Linux, it is very similar but there may be some differences in Section 1 when accessing the "terminal". Windows uses the "command prompt" and should use the same commands as what is described below. The system requirements are minimum, and any average computer should be able to run as a server for this application.

- **Step 1:** Download and install [Python 3](https://www.python.org/ftp/python/3.7.3/python-3.7.3-macosx10.9.pkg)
  
- **Step 2:** Download this [InstallScript.txt](https://drive.google.com/file/d/18SZDFPS7dWwunsWj8ZjjepuhtKa4dteN/view?usp=sharing) file onto your computer. This link should give give you access to the document that you can install. It is a simple script that will install the DropboxSearchTool, as well as any dependencies that are needed for this tool to run.
  
- **Step 3:** Use Command+Space to open the terminal. You will be using this to run the script that was just installed in step 2. If you are not familiar with having used the terminal before, [here is a very helpful guide](https://mac.appstorm.net/how-to/utilities-how-to/how-to-use-terminal-the-basics/) to explaining the basics for moving around in the terminal. It is important that you at least know how to use the 'ls' and 'cd' commands.

    You will want to move into the directory that InstallScript.txt was downloaded to (most likely the Downloads folder). You may also want to move InstallScript.txt to the folder that you will want the DropboxSearchTool to be at.

- **Step 4:** Type in "sudo chmod +x ./InstallScript.txt" and press enter. This will convert the script into an executable file that can be used for the next step.
  
    > It is also important to note that your computer may deny you permissions to do certain tasks. The term "sudo" is used to grant admin privileges to certain tasks, as shown in this step.

- **Step 5:** Type in "sudo ./InstallScript.txt" and press enter. This should start installing the DropboxSearchTool and its dependencies onto the computer. 
  
    > This might ask for you to download Git onto your computer. If it does, install it since the DropboxSearchTool is stored on Github. After Git is installed, type in "./InstallScript.txt" again to install the script.

    To make sure that it is installed correctly, type 'ls' into the terminal and see if the folder "DropboxSearchTool" is there. If it is, then it should be downloaded correctly. If you run into any errors during this part, try copy-pasting them into google and see if there are any easy fixes to resolve the issues.
  
- **Step 6:** After the script has run, go into the DropboxSearchTool folder by typing "cd DropboxSearchTool" and pressing enter.
  
- **Step 7:** Type in "vim DropboxSearchTokens.txt" and this should bring up a text editor. It is here that we will place the token for the Slack bot for users to communicate with. Also it will contain the Dropbox token for the tool to search through. 
  
    > IMPORTANT: These are both secret tokens, so make sure to SHARE THESE WITH NO ONE! The Dropbox may not be safe if these tokens are made public!
  
- **Step 8:** Refer to section 2 and Section 3 for how to get the tokens. To start writing to the file, you will need to press the 'i' key to enable writing to the file. You will then copy the Slack Bot token on the first line of this text editor. Then you will copy the Dropbox token onto the second line. When finished with this, you can hit the escape key, then type ':wq' to save and exit the file back to the terminal.
  
- **Step 9:** When in the DropboxSearchTool folder, type in "python DropboxSearchTool.py" This should run the application.
  
- **Step 10:** You can refer to the User documentation on our [Github](https://github.com/DevonCurrent/DropboxSearchTool/blob/master/Documentation/UserDocumentation.md) to know more about using this application. 
  

## Section 2 Here are the steps to install the Slack bot:

- **Step 1:** Go [here](https://api.slack.com/apps) and create new app. You may need to sign in first to your Slack account.
  
- **Step 2:** After naming the bot and setting its workplace to your company's Slack, click on "Bot Users" on the left-hand side. Create a bot user.
  
- **Step 3:** Click on "Install App" on the left-hand side, and authorize it to your Slack workspace. 
  
- **Step 4:** Copy the Bot User OAuth Access Token (NOT THE OAuth Access Token above it!) and paste it to the first line of "DropboxSearchTokens.txt" from Section 1.

> at this point the Slack bot should be installed on your Slack. You can check that it is running correctly by going to your Slack and clicking on the '+' icon under Apps. The name of your Slack bot should be listed in your workspace.
  

## Section 3 Here are the steps to install the Dropbox App (that will run the Dropbox portion of our program):

- **Step 1:** Go to [here](https://www.dropbox.com/developers/apps) and click "create app". You may need to sign into the Dropbox account that you plan to have this DropboxSearchTool be used for.
  
- **Step 2:** Choose "Dropbox API" -> "Full Dropbox" -> and give it a name. Then, click "create app".
  
- **Step 3:** Click "generate access token" and copy this to the second line of "DropboxSearchTokens.txt" from Section 1.
  


## Section 4 Maintenance and running the tool

> By this point, the program should be able to run in the background. This can be tested that it works properly by making a query on Slack (while it is running on the terminal). You can find how to make a query [here](https://github.com/DevonCurrent/DropboxSearchTool/blob/master/Documentation/UserDocumentation.md), and to learn more about using this application.

- **Step 1:** If it is not currently running, start the DropboxSearchTool. This can be done by going to the terminal (Command + space). You can use [this guide](https://mac.appstorm.net/how-to/utilities-how-to/how-to-use-terminal-the-basics/) to change your directory to wherever the DropboxSearchTool is stored.

- **Step 2:** Once inside the DropboxSearchTool folder, type "python DropboxSearchTool.py" and press enter. This should start the search tool.

- **Step 3:** To stop the search tool from running on the computer, either exit out of the terminal, or press "ctrl + c" to stop the process from running in the terminal.