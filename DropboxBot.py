import dropbox
from dropbox.exceptions import AuthError
    
class DropboxBot:

    def __init__(self, t):
        self.token = t
        self.dbx = dropbox.Dropbox(t)

        try:
            self.dbx.users_get_current_account()
        except AuthError as err:
            print(err)
            print("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")
            exit()
        
        print("Connection established with Dropbox")