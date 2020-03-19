from flask import render_template, request
from Sovellus import app, db
from Sovellus.users import userController
from Sovellus.users.models import User
from Sovellus.home import homeController

@app.route("/")
def index():
    return homeController.home()

@app.route("/home", methods=["POST"])
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
def changePasswordPage():
    return userController.changePasswordPage()

@app.route("/changePassword", methods=["POST"])
def changePassword():
    return userController.changePassword()
