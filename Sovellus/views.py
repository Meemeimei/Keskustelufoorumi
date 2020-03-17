from flask import render_template
from Sovellus import app

@app.route("/")
def index():
    return render_template("home/index.html")
