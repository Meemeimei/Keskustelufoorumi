from flask import render_template, request, redirect
from Sovellus import app, db
from Sovellus.users.models import User
from Sovellus.auth.forms import LoginForm, ChangePasswordForm
from flask_login import login_user, logout_user, current_user
from Sovellus.home import homeController
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
    return homeController.home()
   

def register():
    form = LoginForm(request.form)
    username = form.username.data
    # By no means a secure way to save password
    # simply used to at least make the passwords non-human readable
    password = str(hash(form.password.data))
    
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template("login/register.html", form=LoginForm() , error = "Username is already in use")
    else:
        user = User(username, password)
        db.session().add(user)
        db.session().commit()
        return render_template("login/index.html", form=LoginForm(), error = "Luonti onnistui")
 
def logout():
    logout_user()
    return loginIndex() 

def changePassword():
    form = ChangePasswordForm(request.form)
    oldPassword = str(hash(form.oldPassword.data))
    newPassword = str(hash(form.password.data))

    if (current_user.password == oldPassword):
        current_user.password = newPassword
        db.session().commit()
        return render_template("home/index.html", message="Password changed successfully")

    return render_template("home/index.html", error="Password change failed")

def changePasswordPage():
    return render_template("login/changePassword.html", form = ChangePasswordForm())