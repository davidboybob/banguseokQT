from flask import request
from flask_restx import Resource

from service.auth_helper_service import Auth
from utils.dto import AuthDto

api = AuthDto.api
_auth = AuthDto.auth

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(_auth, validate=True)
    def post(self):
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a user')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)
