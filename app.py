#!/usr/bin/env python3
"""Basic Hello World App"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from database import User

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/aboutme")
def about():
    me = {
        "first_name": "Felipe",
        "last_name": "Botero",
        "hobbies": "Horse Racing and coding"
    }
    return render_template("about.html", user=me)

@app.route("/aboutme/<int:uid>")
def about_user(uid):
    user = User.query.filter_by(id=uid).first()
    return render_template("about.html", user=user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404