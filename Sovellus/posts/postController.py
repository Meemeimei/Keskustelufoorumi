from flask import render_template, request, redirect
from flask_login import current_user
from Sovellus import db
from Sovellus.answers.forms import AnswerForm, EditForm
from Sovellus.posts.forms import PostForm
from Sovellus.answers.models import Answer
from Sovellus.posts.models import Post
from Sovellus.areas.models import Area
from Sovellus.users.models import User
from Sovellus.home import homeController
from Sovellus.groups import groupController


def createPost(areaId):
    form = PostForm(request.form)
    name = form.name.data
    text = form.text.data

    post = Post(name, text, current_user.id, areaId, None)
    db.session().add(post)
    db.session().commit()

    updatePostCounts(areaId)

    return openPost(post.id)

def createGroupPost(groupId):
    form = PostForm(request.form)
    name = form.name.data
    text = form.text.data

    post = Post(name, text, current_user.id, None, groupId)
    db.session().add(post)
    db.session().commit()

    return openPost(post.id)

def openPost(postId):
    post = Post.query.filter_by(id=postId).first()
    if (post.group_id is not None):
        if not groupController.canSeeGroupPost(post.group_id, current_user.id):
            return homeController.homeWithCustomError("Unauthorized")
    if not post:
        return homeController.homeWithCustomError("Post not found")

    return render_template("area/post.html", post=post, answers=Post.getRelatedAnswers(postId), answerForm = AnswerForm(), editForm = EditForm())

def deletePost(postId):

    if not current_user.is_admin():
        return homeController.homeWithCustomError("You are missing user rights required for this operation")
    post = Post.query.filter_by(id=postId).first()
    if post.area_id:
        updatePostCounts(post.area_id)
    else:
        updatePostCounts(-1)
    
    Post.query.filter_by(id=postId).delete()
    db.session().commit()
    
    Answer.deleteUnconnectedAnswers()

    return homeController.homeWithCustomMessage("Post removed successfully")

def updatePostCounts(areaId):
    if (areaId != -1):
        area = Area.query.filter_by(id=areaId).first()
        area.messageCount = Area.getMessageCount(areaId)

    user = User.query.filter_by(id=current_user.id).first()
    user.messageCount = User.getMessageCount(current_user.id)

    db.session().commit()

def newGroupPost(groupId):
    form = PostForm(request.form)
    name = form.name.data
    text = form.text.data

    post = Post(name, text, current_user.id, None, groupId)
    db.session().add(post)
    db.session().commit()

    return openPost(post.id)