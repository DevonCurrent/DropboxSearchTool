#How to search Dropbox files on Slack
Dropbox is great for storing files, but it is difficult to search through for the content that you need. This document will go over how to use the Dropbox Search Tool that allows you to search through Dropbox using Slack. This tool uses a bot to communicate with to make searches (similar to making a search on the internet). After making a search query to the bot, the bot will search through Dropbox and find the files that you need.

#####How to message the bot
Once on Slack, there are two ways you can message the bot to search for files (assuming the bot has been invited to the Slack server). You can join a channel that it has access to and message it from the channel. Alternatively, you can direct message the bot.

#####Enter the search you want to make for Dropbox
There are 4 types of searches you can make to search through dropbox for files:
    > -fn
    > -fc
    > -f
    > -r

Files searches are slow if you are searching through all of Dropbox. You can shorten the time if you have an idea where on dropbox you want to search:
    > -t for file type. The bot is able to search through .doc, .docx, .pdf, .pptx, .xlsx, as well as try to look through others.
    >-l to search through specific folders only (this can be a folder that also contains other folders in it). If there are spaces in the folder name, use '_' to replace the spaces. Multiple folders can be searched through at a time.
    
#####If you forget the names for these searches, -h will remind you what they all are


#####There is a chance the bot may not return your results!
Normally, the bot will return the top 5 most accurate search results that it could find on the Dropbox. If it does not return anything at all, it may not have heard you and may be offline/you are on the wrong channel. If it does reply but returns 0 results, then it could not find anything on Dropbox accurate enough for your search.
