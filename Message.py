class Message:
    """
    Class used to initialize the message attributes
    -----
    Attributes
    -----
    text: string
        text entered
    user: string
        user
    msgID: string
        the message id
    channel: string
        the channel the message is on
    """

    text = ""
    user = ""
    msgID = ""
    channel = ""

    def __init__(self, t, u, m, c):
        self.text = t
        self.user = u
        self.msgID = m
        self.channel = c