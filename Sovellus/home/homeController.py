from flask import render_template, request
from Sovellus import app, db
from Sovellus.areas.forms import AreaForm
from Sovellus.areas.models import Area

def home():
    return render_template("home/index.html", groupForm = AreaForm(), areas=Area.query.all())

def homeWithCustomMessage(message):
    return render_template("home/index.html", message = message, groupForm = AreaForm(), areas=Area.query.all())

def homeWithCustomError(error):
    return render_template("home/index.html", error = error, groupForm = AreaForm(), areas=Area.query.all())