from Sovellus import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
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


    @staticmethod
    def countMessages(accountId):
        statement = text("SELECT "
                        "(SELECT COUNT(*) FROM Post WHERE User_id = :id) + "
                        "(SELECT COUNT (*) FROM Answer WHERE User_id = :id)"
        ).params(id=accountId)
        return db.engine.execute(statement)

