from flask import render_template, request
from Sovellus import app, db
from Sovellus.areas.forms import AreaForm
from Sovellus.areas.models import Area

def home():
    return render_template("home/index.html", groupForm = AreaForm(), areas=Area.query.all())