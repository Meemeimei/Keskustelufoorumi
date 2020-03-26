from Sovellus import db

class Groupuser(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('account.id'),
        nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'),
        nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False
