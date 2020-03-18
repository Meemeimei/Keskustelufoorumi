from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from Sovellus import views

from Sovellus.answers import models
from Sovellus.areas import models
from Sovellus.groups import models
from Sovellus.groupUsers import models
from Sovellus.posts import models
from Sovellus.users import models

db.create_all()
