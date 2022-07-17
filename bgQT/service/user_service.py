import uuid

from models.models import db
from models.models import User

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    
    try:
        if not user:
            new_user = User(
                public_id = str(uuid.uuid4()),
                email = data['email'],
                name = data['name'],
                password = data['password']
            )
            print(new_user)
            save_changes(new_user)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }

            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.'
            }
            return response_object, 409
    except Exception as err:
        print(err)


def get_all_users():
    print(User.query.all())
    return User.query.all()


def get_a_user(id):
    return User.query.filter_by(id=id).first()