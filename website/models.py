from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    accounts = db.relationship('Account')

class Account(db.Model):
    phone = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(150))
    address = db.Column(db.String(250))
    notes = db.Column(db.String(100000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))