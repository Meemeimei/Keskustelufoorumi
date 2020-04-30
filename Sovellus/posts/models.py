from Sovellus import db
from sqlalchemy.sql import text
from Sovellus.answers.models import Answer
import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(144), nullable=False)
    content = db.Column(db.String(144), nullable=False)
    createdOn = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    messageCount = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey('account.id'),
        nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'))
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    def __init__(self, title, content, user_id, area_id, group_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.area_id = area_id
        self.group_id = group_id

    @staticmethod
    def getMessageCount(postId):
        stmt = text("SELECT COUNT (*) FROM Answer"
                     " WHERE Answer.post_id = :postId").params(postId=postId)
        res = db.engine.execute(stmt).fetchone()

        return int(res[0])

    @staticmethod
    def getRelatedAnswers(postId):
        stmt = text("SELECT * FROM Answer"
            " WHERE (Answer.post_id = :postId) ORDER BY Answer.createdOn ASC").params(postId=postId)
        res = db.engine.execute(stmt)
        
        return res

    @staticmethod
    def deleteGroupPosts(groupId):
        stmt = text("DELETE FROM Post"
            " WHERE (Post.group_id = :groupId)").params(groupId=groupId)
        db.engine.execute(stmt)
        Answer.deleteUnconnectedAnswers()

        return True

    @staticmethod
    def deleteAreaPosts(areaId):
        stmt = text("DELETE FROM Post"
            " WHERE (Post.area_id = :areaId)").params(areaId=areaId)
        db.engine.execute(stmt)
        Answer.deleteUnconnectedAnswers()
        
        return True
