from distutils.file_util import copy_file
from flask import Flask
from os import path

from flask_sqlalchemy import SQLAlchemy
from config import Config

from apps.models.models import User, QueitTimeNote

from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    create_database(app)

    from views.views import views
    from views.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    if not path.exists('apps/' + DB_NAME):
        db.create_all(app=app)
        print('Create Database!')
    else:
        print('Already Exist Database!')