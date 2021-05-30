#!usr/bin/env python3

from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return "<product %r>" % self.name


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    reviewText = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return "<review %r>" % self.reviewText

class ProdReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String, nullable=False)
    reviewText = db.Column(db.Text, nullable=True)
    active = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return "<review %r>" % self.reviewText