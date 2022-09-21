from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class QueitTimeNote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100000))
    data = db.Column(db.DataTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Stirng(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('QueitTimeNote')


# class students(db.Model):
#     id = db.Column('student_id', db.Integer, primary_key = True)
#     name = db.Column(db.String(100))
#     city = db.Column(db.String(50))
#     addr = db.Column(db.String(200)) 
#     pin = db.Column(db.String(10))

#     def __init__(self, name, city, addr, pin):
#         self.name = name
#         self.city = city
#         self.addr = addr
#         self.pin = pin