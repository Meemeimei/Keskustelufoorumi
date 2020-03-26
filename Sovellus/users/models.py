from Sovellus import db

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    messageCount = db.Column(db.Integer, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    token = db.Column(db.String(36))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.messageCount = 0
        if (username == "admin"):
            self.admin = True
        else:
            self.admin = False


    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        return self.admin    
