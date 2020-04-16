from Sovellus import db
import datetime

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(144), nullable=False)
    createdOn = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('account.id'),
        nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),
        nullable=False)

    def __init__(self, content, user_id, post_id):
        self.content = content
        self.user_id = user_id
        self.post_id = post_id

