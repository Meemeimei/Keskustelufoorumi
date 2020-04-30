from Sovellus import db
from sqlalchemy.sql import text
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

    @staticmethod
    def deleteUnconnectedAnswers():
        stmt = text("SELECT Answer.id, Answer.post_id FROM Answer")            
        res = db.engine.execute(stmt)
        
        for row in res:
            stmt = text("SELECT * FROM Post where Post.id = :postId").params(postId=row[1])
            result = db.engine.execute(stmt)
            if (result == ""):
                stmt = text("Delete FROM Answer where Answer.id = :answerId").params(answerId=row[0])
                db.engine.execute(stmt)

        return True

