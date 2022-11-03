from datetime import timedelta
from flask import request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restx import Resource

from api.service.auth_service import Auth
from api.dto.auth_dto import AuthDto
from utils.utils import res_object

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
        """
            logout
        """
        # get auth token
        auth_header = request.headers.get('Authorization')
        return Auth.logout_user(data=auth_header)


@api.route('/refresh')
class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        """
            create access_token from refresh token 
        """
        identity = get_jwt_identity()
        # access_token = create_access_token(identity=identity, fresh=False)
        access_token = create_access_token(identity=identity, fresh=timedelta(minutes=30))
        return res_object('success', 'create a access_token.', 201, access_token)


@api.route('/protected')
class RefreshTokenProtected(Resource):
    @jwt_required(fresh=True)
    def get(self):
        """
        check the validator of refresh token.
        """
        current_user_id = get_jwt_identity()
        print(current_user_id)
        return current_user_id