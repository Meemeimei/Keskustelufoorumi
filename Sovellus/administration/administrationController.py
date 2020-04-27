from flask import render_template, request, redirect
from Sovellus import app, db
from Sovellus.users.models import User
from flask_login import current_user, logout_user
from Sovellus.home import homeController

def administration():
    if (current_user.is_admin()):
        return render_template("administration/index.html", users = User.query.all())
    return homeController.homeWithCustomError("This page is restricted")

def deleteUser(userId):
    if (current_user.is_admin()):
        User.query.filter(User.id == userId).delete()
        db.session().commit()
        if (userId == current_user.id):
            logout_user()
            return redirect("/")
  
    return render_template("administration/index.html", users = User.query.all())

def addAdminRights(userId):
    if (current_user.is_admin()):
        User.query.filter(User.id == userId).first().admin = True
        db.session().commit()
  
    return render_template("administration/index.html", users = User.query.all())

def removeAdminRights(userId):
    if (current_user.is_admin()):
        User.query.filter(User.id == userId).first().admin = False
        db.session().commit()
  
    return render_template("administration/index.html", users = User.query.all())