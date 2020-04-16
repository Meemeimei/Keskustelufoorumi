from flask import render_template, request, redirect, url_for
from Sovellus import app, db
from Sovellus.areas.forms import AreaForm
from Sovellus.areas.models import Area

def home():
    return render_template("home/index.html", areaForm = AreaForm(), areas=Area.query.all())

def homeWithCustomMessage(message):
    return redirect(url_for("home", message = message))

def homeWithCustomError(error):
    return redirect(url_for("home", error = error))