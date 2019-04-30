# April 11th
### In-Class 10:15am

Discussed our presentation at the student symposium
* Uploaded pictures and names of people we presented too
** Jasmine Davis, Ben Evans, Amanda Kavars; images in folder

Talked about email sent to TDG earlier in the week about integrating software onto their system, have not heard back.

Devon showed group his efficency tests of the program with TDG's full dropbox.
* Talked about possible ways to improve efficiency.
** More threads in the thread pool (Currently five)
** Compiling program
** Pulling all files to the server during downtime (Most time spent downloading)

Discussed inconsistencies with TDG's dropbox naming conventions and how we plan to address them.

Talked about testing our program on a mac, which is the enviornment it will run on at TDG.


# April 18th
### Bracken Library 2nd Floor 4:00pm

Met with The Design Gym to go over this iteration's progress, as well as handoff documentation and the project for deployment/feedback.

Heidi, Tim and TDG's CEO were present for the meeting.
In the meeting we covered:
- Discussed this iteration's progress. Improving performance, reliability of the server, generalized the search features to work for any Dropbox, and is able to parse some Files and folder that it wouldn't have been able to before (due to naming conventions like snake_case and CamelCase.
- Handed over documents and the tool, and led them through how to get started on setting up the DropboxSearchTool
- Met the CEO of the company, and explained our project and our roles for what we accomplished.
- Post-mortem was discussed for our group's performance, as well as how our project turned out. Both were met with positive feedback.

We will still need to go over with Tim for setting up the DropboxSearchTool, if any problems arise during the setup process.

# April 23rd
### Bracken Library 2:00pm

Met with Tim to discuss issues that he had run into with our instillation instructions.

* Ran into issues because of difference in operating systems.
** Native Python 2 support led to issues with InstallScript using Pip2 not Pip3.
** Found this issue and fixed install script.
* Tim was able complete the set-up using the provided documentation once the issue was fixed.
* Set-up meeting for 4:00pm Wednesday to discuss feedback from TDG, they would be testing it out during the day.

# April 24th
### Bracken Library 4:00pm

Met with Tim and Heidi to discuss their feedback after deploying the tool at TDG.

* They were the only ones who used the tool during the day.
** We had hoped to get a blind test, because they had both seen demonstrations.
** Still good feedback as neither had used the tool yet.
* Believed it was easy to use.
* Help function allowed them to understand why some of their queries did not work.
* Able to find appropriate files with their queries.
* Okay with how long the searches took.
