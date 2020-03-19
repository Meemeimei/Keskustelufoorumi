from flask import render_template, request
from Sovellus import app, db
from Sovellus.users.models import User

def loginIndex():
    return render_template("login/index.html")

def registerIndex():
    return render_template("login/register.html")

def register():
    username = request.form.get("username")
    password = str(hash(request.form.get("password")))
    
    user = User.query.filter_by(username=username).first()
    if (user != None):
        return render_template("login/index.html", message="K\u00e4ytt\u00e4j\u00e4tunnus on jo k\u00e4yt\u00f6ss\u00e4")
    else:
        user = User(username, password)
        db.session().add(user)
        db.session().commit()
        return render_template("login/index.html", message="Luonti onnistui")

def login():
    user = db.session.query(User).filter_by(username=request.form.get("username")).first()

    if (user != None and str(user.password) == str(hash(request.form.get("password")))):
        return render_template("login/postLoginSuccess.html")
    else:
        return render_template("login/postLoginFail.html")
    
def logout():
    return render_template("login/logout.html")

def changePassword():
    # TODO: return a message whether change succeeded

    oldPassword = str(hash(request.form.get("oldPassword")))
    newPassword = str(hash(request.form.get("newPassword")))
    username = request.form.get("newPassword")

    user = User.query.filter_by(username=username).first()
    if (user != None and str(user.password) == oldPassword):
        user.password = newPassword
        db.session().commit()
        return render_template("home/index.html")

    return render_template("home/index.html")