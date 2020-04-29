from flask import render_template, request, redirect
from flask_login import current_user
from Sovellus import db
from Sovellus.answers.forms import AnswerForm, EditForm
from Sovellus.posts.forms import PostForm
from Sovellus.answers.models import Answer
from Sovellus.posts.models import Post
from Sovellus.users.models import User
from Sovellus.home import homeController
from Sovellus.posts import postController


def createAnswer(postId):
    form = AnswerForm(request.form)
    text = form.content.data

    answer = Answer(text, current_user.id, postId)
    db.session().add(answer)
    db.session().commit()

    updatePostCounts(postId)

    return postController.openPost(postId)

def editAnswer(answerId):
    form = EditForm(request.form)
    text = form.content.data

    answer = Answer.query.filter_by(id = answerId).first()

    answer.content = text
    db.session().commit()

    return postController.openPost(answer.post_id)

def deletePost(postId):
    if not current_user.is_admin():
        return homeController.homeWithCustomError("You are missing user rights required for this operation")

    Post.query.filter_by(id=postId).delete()
    db.session().commit()

    return homeController.homeWithCustomMessage("Post removed successfully")

def updatePostCounts(postId):
    post = Post.query.filter_by(id=postId).first()
    post.messageCount = Post.getMessageCount(postId)

    user = User.query.filter_by(id=current_user.id).first()
    user.messageCount = User.getMessageCount(current_user.id)

    db.session().commit()