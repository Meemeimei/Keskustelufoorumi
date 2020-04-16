from Sovellus import db
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
    area_id = db.Column(db.Integer, db.ForeignKey('area.id'),
        nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'))

    def __init__(self, title, content, user_id, area_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.area_id = area_id

    def setGroup(self, group_id):
        self.group_id = group_id

    @staticmethod
    def getMessageCount(postId):
        return Answer.query.filter(Answer.post_id == postId).count()

    @staticmethod
    def getRelatedAnswers(postId):
        return Answer.query.filter(Answer.post_id == postId).order_by(Answer.createdOn.asc())
