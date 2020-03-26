from flask import render_template, request
from Sovellus import app, db
from Sovellus.users.models import User
from Sovellus.auth.forms import LoginForm
from flask_login import login_user
import uuid

def loginIndex():
    return render_template("login/index.html", form = LoginForm())

def registerIndex():
    return render_template("login/register.html", form = LoginForm())

def login():
    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=str(hash(form.password.data))).first()
    if not user:
        return render_template("login/index.html", form = form,
                               error = "No such username or password")
    login_user(user)
    return render_template("home/index.html")
   

def register():
    form = LoginForm(request.form)
    username = form.username.data
    password = str(hash(form.password.data))
    
    user = User.query.filter_by(username=username).first()
    if not user:
        return render_template("login/register.html", error = "Username is already in use")
    else:
        user = User(username, password)
        db.session().add(user)
        db.session().commit()
        return render_template("login/index.html", error = "Luonti onnistui")
 
def logout():
    return render_template("login/logout.html")

def changePassword():
    oldPassword = str(hash(request.form.get("oldPassword")))
    newPassword = str(hash(request.form.get("newPassword")))
    token = request.form.get("token")
    if (token != None and token != ""):
        user = db.session.query(User).filter_by(token=token).first()
        if (user != None and str(user.password) == oldPassword):
            user.password = newPassword
            db.session().commit()
            return render_template("home/index.html", message="Password changed successfully")

    return render_template("home/index.html", message="Password change failed")

def changePasswordPage():
    return render_template("login/changePassword.html")