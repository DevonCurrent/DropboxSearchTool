import SearchMain
from tkinter import *
import os
import time
import atexit
from threading import Event, Thread

class DropboxSearchTool(Frame):

    def __init__(self):
        super().__init__()
        self.ISRUNNING = False
        self.dropboxThread = None
        self.mainService = None
        self.slackToken = None
        self.dropboxToken = None
        self.slackTokenText = ""
        self.dropboxTokenText = ""

        def startup():
            if(os.path.isfile("./DropboxSearchTokens.txt")):
                lines = open("DropboxSearchTokens.txt").readlines()
                if(len(lines[0].strip()) > 3):
                    self.slackToken = lines[0].strip()
                try:
                    if(len(lines[1].strip()) > 3):
                        self.dropboxToken = lines[1].strip()
                except:
                    pass
            else:
                f= open("DropboxSearchTokens.txt","w+")
                f.close()
            
            if(self.slackToken == None):
                self.slackToken = ""
            if(self.dropboxToken == None):
                self.dropboxToken = ""

        def cleanup():
            if(os.path.isfile("./DropboxSearchTokens.txt")):
                with open("./DropboxSearchTokens.txt","w+") as tokensText:
                    tokensText.write(self.slackToken + "\n")
                    tokensText.write(self.dropboxToken)
                    tokensText.close()
        
        def start_app():
            self.ISRUNNING = True
            self.slackToken = self.slackTokenText.get("1.0", 'end-1c').strip()
            self.dropboxToken = self.dropboxTokenText.get("1.0", 'end-1c').strip()
            self.startButton['state'] = DISABLED
            if(self.ISRUNNING):
                print("running")
                self.dropboxThread = Thread(target=lambda gui=self, slackToken=self.slackToken, 
                    dropboxToken=self.dropboxToken: SearchMain.start_bots(self,self.slackToken,self.dropboxToken))
                self.dropboxThread.start()


        def terminate_app():
            self.ISRUNNING = False
            import time
            time.sleep(1)

            name = str(self.dropboxThread.getName)
            if(name.rfind("stopped") != -1):
                self.dropboxThread.join()
                self.startButton['state'] = "normal"
                self.dropboxThread = None
            else:
                terminate_app()


        startup()

        self.master.title("Dropbox Search Tool")
        self.pack(fill=BOTH, expand=True)

        help1 = Label(self, text="To use this tool, copy your Slack Bot token and Dropbox app token below. Then start the server.", font=("Calibri", 16), wraplength=700)
        help1.grid(row=0, column=0, columnspan=2, sticky=N+W+E+S)

        lbl1 = Label(self, text="Enter your Slack Token", font=("Calibri", 12)).grid(row=1, column=0, pady=(20, 5))
        lbl2 = Label(self, text="Enter your Dropbox Token", font=("Calibri",12)).grid(row=1, column=1, pady=(20,5))

        self.slackTokenText = Text(self, height=4, width=39)
        self.slackTokenText.insert(INSERT, self.slackToken)
        self.slackTokenText.grid(row=2, column=0, sticky=W+E+N+S, padx=3)

        self.dropboxTokenText = Text(self, height=4, width=39)
        self.dropboxTokenText.insert(INSERT, self.dropboxToken)
        self.dropboxTokenText.grid(row=2, column=1, sticky=W+E+N+S, padx=3)

        self.startButton = Button(self, text="Start Server", command=start_app, height=1, width=20, bg="light grey")
        self.startButton.grid(row=3, columnspan=2, pady=(40, 0))

        self.stopButton = Button(self, text="Stop Running", command=terminate_app, height=1, width=20, bg="light grey")
        self.stopButton.grid(row=4, columnspan=2, pady=20)

        atexit.register(cleanup)


    def no_slack_token_found(self):
        warning1 = Label(self, text="Your SLACK token does not seem to work. Please try and use a different token.", font=("Calibri", 14), fg="red", wraplength=800)
        warning1.grid(row=5, columnspan=2, sticky=W+E+N+S)
        self.startButton["state"] = "normal"
        self.dropboxThread = None

    def no_dropbox_token_found(self):
        warning1 = Label(self, text="Your DROPBOX token does not seem to work. Please try and use a different token.", font=("Calibri", 14), fg="red", wraplength=800)
        warning1.grid(row=5, columnspan=2, sticky=W+E+N+S)
        self.startButton["state"] = "normal"
        self.dropboxThread = None


if __name__ == '__main__':
    root = Tk()
    root.geometry("800x450+400+200")
    app = DropboxSearchTool()
    root.mainloop()
