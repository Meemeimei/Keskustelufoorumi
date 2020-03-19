from flask import render_template, request
from Sovellus import app, db
from Sovellus.userController import userController
from Sovellus.users.models import User

@app.route("/")
def index():
    return render_template("home/index.html")

@app.route("/home")
def home():
    return render_template("home/index.html")

@app.route("/login", methods=["GET"])
def loginIndex():
    return userController.loginIndex()

@app.route("/register", methods=["GET"])
def registerIndex():
    return userController.registerIndex()

@app.route("/register", methods=["POST"])
def register():
    return userController.register()

@app.route("/login", methods=["POST"])
def login():
    return userController.login()
    
@app.route("/logout")
def logout():
    return userController.logout()

@app.route("/changePassword")
def changePassword():
    return userController.changePassword()

