#!/usr/bin/env python3

"""database models"""

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    hobbies = db.Column(db.String, nullable=True)

    def __repr__(self):
        return "<User %r>" % (self.first_name, self.last_name)
        