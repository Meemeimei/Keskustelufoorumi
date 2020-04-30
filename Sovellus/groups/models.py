from Sovellus import db
from sqlalchemy.sql import text

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def isEmpty(groupId):
        stmt = text("SELECT COUNT (*) FROM Post"
            " WHERE Post.group_id = :groupId").params(groupId=groupId)
        res = db.engine.execute(stmt)

        if (res == 0):
            return True

        return False

    @staticmethod
    def getUsers(userId):
        stmt = text("SELECT g.id, g.name "
            " FROM \"group\" g, account u, groupuser gu"
            " WHERE gu.user_id = :userId AND g.id = gu.group_id").params(userId=userId)
            
        res = db.engine.execute(stmt)
        return [{"id": row[0], "name": row[1]} for row in res]
        