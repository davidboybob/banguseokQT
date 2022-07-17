from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from app import flask_bcrypt

db = SQLAlchemy()

# Many to Many => User : Challenge = M : M
orders = db.Table('orders',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
            db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id')),
            db.Column('achivement_rate', db.Float)
        )
    

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # user_id = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(10), nullable=False)
    own_donations_mount = db.Column(db.Integer, default=0)
    password_hash = db.Column(db.String(128), nullable=False)
    public_id = db.Column(db.String(128), unique=True)
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    
    # qt : user = N : 1
    qt_id = db.relationship('Qt', backref='user', lazy=True)

    # comments : User = N : 1
    comments_id = db.relationship('Comments', backref='user', lazy=True)

    # challenge : user = M : M 
    challenges = db.relationship('Challenge', secondary=orders, lazy='subquery',
                                    backref=db.backref('users', lazy=True)
                                )

    # donation : User = N : 1
    donation_id = db.relationship('Donation', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __init__(self, 
                name, 
                email,
                password,
                public_id):
                #own_donations_mount, 
                #create_at, updated_at, 
                #commnets_id, 
                #challenges, 
                #donation_id):
        self.name = name
        self.email = email
        self.password = password
        self.public_id = public_id
        # self.own_donations_mount = own_donations_mount
        # self.create_at = create_at
        # self.updated_at = updated_at
        # self.comments_id = commnets_id
        # self.challenges = challenges
        # self.donation_id = donation_id



    def __repr__(self):
        return '<User %r>' %self.name


class Qt(db.Model):
    __tablename__ = 'qt'

    id = db.Column(db.Integer, primary_key=True)
    blog_url = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(256))
    contents = db.Column(db.Text)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # user : qt = 1: N
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # comments : qt = N : 1
    comments_id = db.relationship('Comments', backref='qt', lazy=True)

    # challenge : qt = 1 : N
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id')) #, nullable=False)

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


class Challenge(db.Model):
    __tablename__ = 'challenge'

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean, default=False) # state 추가하기 
    title = db.Column(db.String(256)) # bible + title
    contents = db.Column(db.Text)
    from_date = db.Column(db.DateTime())
    to_date = db.Column(db.DateTime())
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    # challenge : qt = 1 : N
    qt_id = db.relationship('Qt', backref='challenge', lazy=True)

    # challenge : budget = N : 1
    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'))

    def __repr__(self):
        return '<Challenge %r>' %self.title


class Budget(db.Model):
    __tablename__ = 'budget'

    id = db.Column(db.Integer, primary_key=True)
    mount = db.Column(db.Integer)
    # donation : budget = N : 1
    donation_id = db.relationship('Donation', backref='budget',lazy=True)

    # challenge : budget = N : 1
    challenge_id = db.relationship('Challenge', backref='budget', lazy=True)


    def __repr__(self):
        return '<budget %r>' %self.mount


class Donation(db.Model):
    __tablename = 'donation'

    id = db.Column(db.Integer, primary_key=True)
    mount = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    # user : donation = 1 : N
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#, nullable=False)

    # budget : donation = 1 : N
    budget_id = db.Column(db.Integer, db.ForeignKey('budget.id'))#, nullable=False)