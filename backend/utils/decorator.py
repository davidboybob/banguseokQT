from functools import wraps
from flask import request

from api.service.auth_service import Auth

def refresh_token_verified(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        verified, status = Auth.verified_refresh_token(request)
        if not verified:
            return verified, status
        return f(*args, **kwargs)
    return decorated


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')

        if not token:
            return data, status
        return f(*args, **kwargs)

    return decorated


def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        token = data.get('data')
        if not token:
            return data, status
        admin = token.get('admin')
        if not admin:
            response_object = {
                'status': 'fail',
                'message': 'admin token required'
            }
            return response_object, 401

        return f(*args, **kwargs)

    return decorated
