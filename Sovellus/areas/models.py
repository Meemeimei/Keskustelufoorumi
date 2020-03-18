from Sovellus import db

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    messageCount = db.Column(db.Integer, nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False
