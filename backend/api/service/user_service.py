import uuid

from flask_restx import abort

from utils.utils import res_object

from models.models import db
from models.models import User

from utils.utils import save_changes


def delete_data(data):
    db.session.delete(data)
    db.session.commit()


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id = str(uuid.uuid4()),
            email = data['email'],
            name = data['name'],
            password = data['password']
        )

        save_changes(new_user)
        return res_object('success', 'Successfully registered.', 201 )            
    else:
        # return res_object('fail', 'User already exists. Please Log in.', 409)
        abort(409, 'Successfully registered.')


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def delete_a_user(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    # user = User.query.get(public_id)

    # Password 확인 절차 필요
    delete_a_user(user)

    response_object = {
        'status': 'success',
        'message': 'Successfully deleted.'
    }

    return response_object, 204
