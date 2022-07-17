from statistics import mode
from flask import Blueprint, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_restx import Api, Resource
from flask_bcrypt import Bcrypt


# db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
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

    
    from api.user_controller import api as user_namespace

    api.add_namespace(user_namespace, path='/user')

    # app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + Config.dbfile + "?charset=utf-8"
    # print(app.config)
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = Config.secret_key

    # DB 만들기
    from models import models

    db = models.db
    db.init_app(app)
    flask_bcrypt.init_app(app)
    db.app = app

    # Init Marshmallow
    # ma = Marshmallow(app)

    # class UserSchema(ma.SQLAlchemyAutoSchema):
    #     class Meta:
    #         # print(dir(db))
    #         model = User
    #         include_fk = True
    #         # fields = ('email', 'name', 'password')


    # class QtSchema(ma.SQLAlchemyAutoSchema):
    #     class Meta:
    #         model = Qt
            # include_fk = True


    
    db.create_all()

    # user_schema = UserSchema()
    # users_schema = UserSchema(many=True)
    # qt_schema = QtSchema()
    # user = User(name='sjpark', email='sjpark@naver.com', password='12341234')
    # qt = Qt(title='test', user_id=0)
    # db.session.add(user)
    # db.session.commit()
    # user_schema.dump(user)

    # @app.route("/api/users", methods=["GET"])
    # def get_users():
    #     all_users = User.query.all()
    #     result = users_schema.dump(all_users)
    #     print(result)
    #     return result[0]

    app.register_blueprint(api_blueprint)

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
     