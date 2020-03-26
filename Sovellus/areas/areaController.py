from flask import render_template, request, redirect
from Sovellus import db
from Sovellus.areas.forms import AreaForm
from Sovellus.areas.models import Area
from Sovellus.home import homeController

def createArea():
    form = AreaForm(request.form)
    name = form.name.data
    area = Area.query.filter_by(name=name).first()
    if area:
        return homeController.home()

    area = Area(name)
    db.session().add(area)
    db.session().commit()
    return homeController.home()