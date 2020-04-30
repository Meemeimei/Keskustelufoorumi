from flask import render_template, request, redirect, url_for
from Sovellus import app, db
from flask_login import current_user
from Sovellus.areas.forms import AreaForm
from Sovellus.groups.forms import GroupForm
from Sovellus.areas.models import Area
from Sovellus.users.models import User
from Sovellus.groups.models import Group

def home():
    if (current_user.admin):
        return render_template("home/index.html", areaForm = AreaForm(), groupForm = GroupForm(), areas=Area.query.all(), groups=Group.query.all())
    return render_template("home/index.html", areaForm = AreaForm(), groupForm = GroupForm(), areas=Area.query.all(), groups=User.getGroups(current_user.id))

def homeWithCustomMessage(message):
    return redirect(url_for("home", message = message))

def homeWithCustomError(error):
    return redirect(url_for("home", error = error))