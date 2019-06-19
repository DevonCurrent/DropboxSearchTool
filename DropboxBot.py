import dropbox
from dropbox.exceptions import AuthError

class DropboxBot:
    """
    Class used to initialize the dropbox
    -----
    Attributes
    -----
    dbx: string
        dropbox token
    """

    def __init__(self, gui, dropboxToken):

        try:
            self.dbx = dropbox.Dropbox(dropboxToken)
            self.dbx.users_get_current_account()
        except:
            print("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
            gui.no_dropbox_token_found()
            exit()
        
        print("Connection established with Dropbox")