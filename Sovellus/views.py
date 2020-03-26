from flask import render_template, request
from flask_login import login_required
from Sovellus import app, db
from Sovellus.users import userController
from Sovellus.users.models import User
from Sovellus.home import homeController
from Sovellus.administration import administrationController
from Sovellus.areas import areaController

@app.route("/")
@login_required
def index():
    return homeController.home()

@app.route("/home", methods=["POST"])
@login_required
def home():
    return homeController.home()

@app.route("/login", methods=["GET"])
def loginIndex():
    return userController.loginIndex()

@app.route("/login", methods=["POST"])
def login():
    return userController.login()

@app.route("/logout")
def logout():
    return userController.logout()

@app.route("/register", methods=["GET"])
def registerIndex():
    return userController.registerIndex()

@app.route("/register", methods=["POST"])
def register():
    return userController.register()

@app.route("/changePassword", methods=["Get"])
@login_required
def changePasswordPage():
    return userController.changePasswordPage()

@app.route("/changePassword", methods=["POST"])
@login_required
def changePassword():
    return userController.changePassword()

@app.route("/administration", methods=["GET"])
@login_required
def administration():
    return administrationController.administration()

@app.route("/administration/delete/<userId>/", methods=["POST"])
@login_required
def deleteUser(userId):
    return administrationController.deleteUser(userId)

@app.route("/areaCreation", methods=["POST"])
@login_required
def createArea():
    return areaController.createArea()

@app.route("/auth/logout")
@login_required
def auth_logout():
    userController.logout()
    