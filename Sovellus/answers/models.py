from Sovellus import db

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(144), nullable=False)
    createdOn = db.Column(db.Date, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),
        nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False
