from flask import render_template, request
from Sovellus import app, db
from Sovellus.users.models import User

def home():

    token = request.form.get("token")
    print(token)
    if (token == None or token == ""):
        return render_template("login/logout.html")
    
    user = db.session.query(User).filter_by(token=token).first()

    if (user == None):
        return render_template("login/logout.html")

    return render_template("home/index.html", username=user.username, token=token, admin=user.admin)