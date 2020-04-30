from flask import render_template, request, redirect
from flask_login import current_user
from Sovellus import db
from Sovellus.areas.forms import AreaForm
from Sovellus.posts.forms import PostForm
from Sovellus.areas.models import Area
from Sovellus.posts.models import Post
from Sovellus.home import homeController


def createArea():
    form = AreaForm(request.form)
    name = form.name.data
    area = Area.query.filter_by(name=name).first()
    if area:
        return homeController.homeWithCustomError("Area name must be unique")

    area = Area(name)
    db.session().add(area)
    db.session().commit()
    return homeController.homeWithCustomMessage("Area created successfully")

def openArea(areaId):
    area = Area.query.filter_by(id=areaId).first()
    if not area:
        return homeController.homeWithCustomError("Area not found")

    return render_template("area/index.html", areaId = areaId, posts=Post.query.filter(Post.area_id == areaId), postForm = PostForm())

def deleteArea(areaId):

    if not current_user.is_admin():
        return homeController.homeWithCustomError("You are missing user rights required for this operation")

    Area.query.filter_by(id=areaId).delete()
    db.session().commit()

    Post.deleteAreaPosts(areaId)

    return homeController.homeWithCustomMessage("Area removed successfully")