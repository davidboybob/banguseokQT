from models.models import db
from models.models import Qt


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def save_new_qt(data):
    try:
        print(data)
        new_qt = Qt(
            blog_url = data['blog_url'],
            title = data['title'],
            contents = data['contents'],
            user_id = data['user_id'][0]['public_id']
        )

        save_changes(new_qt)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered'
        }

        return response_object, 201
    except Exception as err:
        response_object = {
            'status': 'fail',
            'message': 'your Qt\'s register failed.',
            'err_message': err
        }
        print(err)
        return response_object, 409


def get_all_qts():
    return Qt.query.all()


def get_a_qt(id):
    return Qt.query.fileter_by(id=id).first()


