from flask import render_template, request
from flask_login import login_required
from Sovellus import app, db
from Sovellus.users import userController
from Sovellus.users.models import User
from Sovellus.home import homeController
from Sovellus.administration import administrationController
from Sovellus.areas import areaController
from Sovellus.posts import postController
from Sovellus.answers import answerController
from Sovellus.groups import groupController

@app.route("/")
@login_required
def index():
    return homeController.home()

@app.route("/home")
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

@app.route("/areas/delete/<areaId>", methods=["POST"])
@login_required
def deleteArea(areaId):
    return areaController.deleteArea(areaId)

@app.route("/areas/<areaId>")
@login_required
def openArea(areaId):
    return areaController.openArea(areaId)

@app.route("/areas/posts/<postId>")
@login_required
def openPost(postId):
    return postController.openPost(postId)

@app.route("/postCreation/<areaId>", methods=["POST"])
@login_required
def createPost(areaId):
    return postController.createPost(areaId)

@app.route("/groupPostCreation/<groupId>", methods=["POST"])
@login_required
def createGroupPost(groupId):
    return postController.createPost(groupId)

@app.route("/posts/delete/<postId>", methods=["POST"])
@login_required
def deletePost(postId):
    return postController.deletePost(postId)

@app.route("/posts/reply/<postId>", methods=["POST"])
@login_required
def createAnswer(postId):
    return answerController.createAnswer(postId)

@app.route("/groups/create", methods=["POST"])
@login_required
def createGroup():
    return groupController.createGroup()

@app.route("/groups/<groupId>")
@login_required
def openGroup(groupId):
    return groupController.openGroup(groupId)

@app.route("/groups/delete/<groupId>", methods=["POST"])
@login_required
def deleteGroup(groupId):
    return groupController.deleteGroup(groupId)

@app.route("/groups/createPost/<groupId>", methods=["POST"])
@login_required
def newGroupPost(groupId):
    return postController.newGroupPost(groupId)

@app.route("/auth/logout")
@login_required
def auth_logout():
    userController.logout()
    