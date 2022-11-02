from venv import create
from flask import request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restx import Resource

from api.service.auth_service import Auth
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
        """
        Login
        """
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


@api.route('/protected')
class RefreshTokenProtected(Resource):
    @jwt_required()
    def get(self):
        """
        check the validator of refresh token.
        """
        current_user_id = get_jwt_identity()
        return 