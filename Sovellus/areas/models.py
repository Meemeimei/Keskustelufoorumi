from Sovellus import db
from sqlalchemy.sql import text
from Sovellus.posts.models import Post

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    messageCount = db.Column(db.Integer, default=0)

    def __init__(self, name):
        self.name = name
        self.messageCount = 0

    @staticmethod
    def getMessageCount(areaId):
        stmt = text("SELECT COUNT (*) FROM Post"
            " WHERE Post.area_id = :areaId").params(areaId=areaId)
        res = db.engine.execute(stmt)

        return res
