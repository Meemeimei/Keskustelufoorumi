from Sovellus import db

class Task(db.Model):
    id = db.AutoField(primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    messageCount = db.Column(db.Integer, nullable=False)
    admin = dbColumn(db.boolean, nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False
