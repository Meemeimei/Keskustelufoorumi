from flask import render_template, request
from Sovellus import app, db
from Sovellus.users.models import User

def administration():
    return render_template("administration/index.html", users = User.query.all())

def deleteUser(userId):
    User.query.filter(User.id == userId).delete()
    db.session().commit()
  
    return render_template("administration/index.html", users = User.query.all())