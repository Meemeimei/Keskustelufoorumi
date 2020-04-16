from flask import render_template, request, redirect
from flask_login import current_user
from Sovellus import db
from Sovellus.answers.forms import AnswerForm
from Sovellus.posts.forms import PostForm
from Sovellus.answers.models import Answer
from Sovellus.posts.models import Post
from Sovellus.home import homeController
from Sovellus.posts import postController


def createAnswer(postId):
    form = AnswerForm(request.form)
    text = form.content.data

    answer = Answer(text, current_user.id, postId)
    db.session().add(answer)
    db.session().commit()
    return postController.openPost(postId)

def deletePost(postId):

    if not current_user.is_admin():
        return homeController.homeWithCustomError("You are missing user rights required for this operation")

    Post.query.filter_by(id=postId).delete()
    db.session().commit()

    return homeController.homeWithCustomMessage("Post removed successfully")