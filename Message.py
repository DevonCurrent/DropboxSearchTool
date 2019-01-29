class Message:
    text = ""
    user = ""
    msgID = ""
    channel = ""

    def __init__(self, t, u, m, c):
        self.text = t
        self.user = u
        self.msgID = m
        self.channel = c