# March 10th 2019
### Bracken Library 1st floor 2:00pm

Discussed what we will cover in this iteration and reviewed our previous meeting with Tim from TDG:  
  * We should keep the UI simple like it is for Slack users
  * Tim would like to see a model of how the current search procedures run and how they find files to return
  * We still need to create more tests for the search features, so that the integration into TDG's Dropbox will be easier
  * We need to obtain TDG's Dropbox information, so that we can make sure that our application will run as intended
  * Add another optional search parameter based on the type of file extensions (.ppt, .doc, .txt, .pdf, .xlsx, .pptx, .docx)
  * Allow the system to receive multiple search queries at the same time by multiple Slack users
  * Replace Tika with a better file parser that is more lightweight and reliable
  * Find any other ways to optimize the search procedure for finding files

# March 14th 2019
### Robert Bell 4th Floor 10:30am

Distributed user stories to work on, and covered what we are currently working on:
 * Devon is working on creating models to show TDG, ask to ask TDG for access to the Dropbox. Also working on optimizing the search algorithms for finding files.
 * Allison working on making the poster for the presentation. Creating integration tests, and adding the optional file type search.
 * Ryan is working on finding a better file parser than tika. Also working to refactor the RelevantFileList to be more intuitive.

We have yet to plan the next meeting with TDG, but will try to setup a meeting with them around the end of next week (3/23/19)
