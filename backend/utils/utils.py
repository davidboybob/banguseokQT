from models.models import db

def save_changes(data):
    db.session.add(data)
    db.session.commit()


def res_object(status: str, message: str, statuscode: int = 500, *args: dict):
    return {
        'status': status,
        'message': message,
        'data': args

    }, statuscode