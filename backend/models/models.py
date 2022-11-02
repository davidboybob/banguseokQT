# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from app import flask_bcrypt
from config.config import CONFIG
import jwt
import datetime

db = SQLAlchemy()

# Many to Many => User : Challenges = M : M
orders = db.Table('orders',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
            db.Column('challenges_id', db.Integer, db.ForeignKey('challenges.id')),
            db.Column('achivement_rate', db.Float)
        )


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    own_donations_mount = db.Column(db.Integer, default=0)
    password_hash = db.Column(db.String(128), nullable=False)
    public_id = db.Column(db.String(128), unique=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    
    admin = db.Column(db.Boolean, nullable=False, default=False)

    # qt : user = N : 1
    qt_id = db.relationship('Qt', backref='user', lazy=True)

    # comments : User = N : 1
    comments_id = db.relationship('Comments', backref='user', lazy=True)

    # challenges : user = M : M 
    challenges_id = db.relationship('Challenges', secondary=orders, lazy='subquery',
                                    backref=db.backref('users', lazy=True)
                                )

    # donation : User = N : 1
    donation_id = db.relationship('Donation', backref='user', lazy=True)

    # refresh_token : User = N : 1
    refresh_id = db.relationship('RefreshToken', backref='user', lazy=True)


    @property
    def password(self):
        raise AttributeError('password is not readable attribute!')


    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')


    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User %r>' %self.name


class Qt(db.Model):
    __tablename__ = 'qt'

    id = db.Column(db.Integer, primary_key=True)
    blog_url = db.Column(db.String(256), default=True)
    title = db.Column(db.String(256))
    contents = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # user : qt = 1: N
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # comments : qt = N : 1
    comments_id = db.relationship('Comments', backref='qt', lazy=True)

    # challenges : qt = 1 : N
    challenges_id = db.Column(db.Integer, db.ForeignKey('challenges.id')) #, nullable=False)


    def __repr__(self):
        return '<Qt %r>' %self.title


class Comments(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # Comments : user = N : 1
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#, nullable=False)

    # Commnets : qt = N : 1
    qt_id = db.Column(db.Integer, db.ForeignKey('qt.id'))#, nullable=False)

    def __repr__(self):
        return '<Comments %r>' %self.contents


class Challenges(db.Model):
    __tablename__ = 'challenges'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean, default=False) # state 추가하기 
    title = db.Column(db.String(256)) # bible + title
    contents = db.Column(db.Text)
    from_date = db.Column(db.DateTime())
    to_date = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # challengs : user = M : M
    user_id = db.relationship('User', secondary=orders, lazy='subquery',
                                    backref=db.backref('challenges', lazy=True, overlaps="challenges_id,users"), overlaps="challenges_id,users")


    # challenges : qt = 1 : N
    qt_id = db.relationship('Qt', backref='challenges', lazy=True)

    # challenges : budget = N : 1
    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'))

    def __repr__(self):
        return '<Challenges %r>' %self.title


class Budget(db.Model):
    __tablename__ = 'budget'

    id = db.Column(db.Integer, primary_key=True)
    mount = db.Column(db.Integer)
    # donation : budget = N : 1
    donation_id = db.relationship('Donation', backref='budget',lazy=True)

    # challenges : budget = N : 1
    challenges_id = db.relationship('Challenges', backref='budget', lazy=True)


    def __repr__(self):
        return '<budget %r>' %self.mount


class Donation(db.Model):
    __tablename__ = 'donation'

    id = db.Column(db.Integer, primary_key=True)
    mount = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # user : donation = 1 : N
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#, nullable=False)

    # budget : donation = 1 : N
    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'))#, nullable=False)


class RefreshToken(db.Model):
    __tablename__ = "refresh_token"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    refresh = db.Column(db.String(500))
