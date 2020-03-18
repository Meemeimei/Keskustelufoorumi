from Sovellus import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    messageCount = db.Column(db.Integer, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.messageCount = 0
        if (username == "eemi"):
            self.admin = True
        else:
            self.admin = False
        
