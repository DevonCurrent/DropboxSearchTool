class Message:
    text = ""
    user = ""
    msg_id = ""
    channel = ""

    def __init__(self, t, u, m, c):
        self.text = t
        self.user = u
        self.msg_id = m
        self.channel = c