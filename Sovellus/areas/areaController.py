from flask import render_template, request, redirect
from Sovellus import db
from Sovellus.areas.forms import AreaForm
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

    return render_template("area/index.html", posts=Post.query.filter(Post.area_id == areaId))