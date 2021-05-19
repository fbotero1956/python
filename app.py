#!/usr/bin/env python3
"""Basic Hello World App"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Felipe Botero's world!!!</h1>"

@app.route("/aboutme")
def about():
    me = {
        "first_name": "Felipe",
        "last_name": "Botero",
        "hobbies": "Soccer and bike riding"
    }
    return str(me)