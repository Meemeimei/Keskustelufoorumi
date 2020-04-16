from flask import render_template, request, redirect
from flask_login import current_user
from Sovellus import db
from Sovellus.answers.forms import AnswerForm
from Sovellus.posts.forms import PostForm
from Sovellus.answers.models import Answer
from Sovellus.posts.models import Post
from Sovellus.home import homeController


def createPost(areaId):
    form = PostForm(request.form)
    name = form.name.data
    text = form.text.data

    post = Post(name, text, current_user.id, areaId)
    db.session().add(post)
    db.session().commit()
    return openPost(post.id)

def openPost(postId):
    post = Post.query.filter_by(id=postId).first()
    if not post:
        return homeController.homeWithCustomError("Post not found")

    return render_template("area/post.html", post = post, answers=Answer.query.filter(Answer.post_id == postId), answerForm = AnswerForm())

def deletePost(postId):

    if not current_user.is_admin():
        return homeController.homeWithCustomError("You are missing user rights required for this operation")

    Post.query.filter_by(id=postId).delete()
    db.session().commit()

    return homeController.homeWithCustomMessage("Post removed successfully")