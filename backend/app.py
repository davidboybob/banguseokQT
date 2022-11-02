from datetime import datetime, timedelta, timezone
from statistics import mode
from flask import Blueprint, Flask, jsonify
from flask_jwt_extended import JWTManager, create_access_token, get_jwt, get_jwt_identity, set_access_cookies
from flask_sqlalchemy import SQLAlchemy
from utils.global_error_handler import create_error_handler
from config.config import CONFIG
from flask_restx import Api, Resource
from flask_bcrypt import Bcrypt

from flask_cors import CORS

# db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    CORS(app)
    api_blueprint = Blueprint('api', __name__)
    # flask-restx 
    
    api = Api(
            api_blueprint,
            version='1.0',
            title='banguseokQT Api',
            description='This is Challenges QT Projects.',
            terms_url= '/terms',
            contact='davidboy7780@gmail.com',
            license='MIT'
            )

    
    from api.controller.user_controller import api as user_namespace
    from api.controller.qt_controller import api as qt_namespace
    from api.controller.comments_controller import api as comments_namespace
    from api.controller.challenges_controller import api as challenges_namespace
    from api.controller.budget_controller import api as budget_namespace
    from api.controller.donation_controller import api as donation_namespace
    from api.controller.auth_controller import api as auth_namespace

    base_api = "/api/v1"

    api.add_namespace(user_namespace, path=f'{base_api}/user')
    api.add_namespace(qt_namespace, path=f'{base_api}/qt')
    api.add_namespace(comments_namespace, path=f'{base_api}/comments')
    api.add_namespace(challenges_namespace, path=f'{base_api}/challenges')
    api.add_namespace(budget_namespace, path=f'{base_api}/budget')
    api.add_namespace(donation_namespace, path=f'{base_api}/donation')
    api.add_namespace(auth_namespace, path=f'{base_api}/auth')
    create_error_handler(api)
    # app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + CONFIG.dbfile + "?charset=utf-8"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = CONFIG.SECRET_KEY
    # jwt Token Config
    app.config['JWT_SECRET_KEY'] = CONFIG.SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = CONFIG.expired_time_access_token
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = CONFIG.expired_time_refresh_token

    jwt = JWTManager(app)
    # jwt 검증
    @app.after_request
    def refresh_expiring_jwts(response):
        try:
            print(get_jwt())
            exp_timestamp = get_jwt()["exp"]
            print(exp_timestamp)
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original response
            return response

    # DB 만들기
    from models import models

    db = models.db
    db.init_app(app)
    flask_bcrypt.init_app(app)
    db.app = app
    
    db.create_all()

    app.register_blueprint(api_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5001, debug=True)
     