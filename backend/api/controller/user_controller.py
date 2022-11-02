from os import access
from flask import request
from flask_jwt_extended import create_access_token
from flask_restx import Api, Resource, Namespace
from api.service.user_service import get_a_user, get_all_users, save_new_user, delete_a_user
from utils.dto import UserDto

from utils.decorator import token_required, admin_token_required

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    # @token_required
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    
    @api.response(201, 'Users successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Create a new user"""
        data = request.json
        
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The user identifier')
@api.response(404, 'User not found.')
class User(Resource):
    # @token_required
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user

@api.route('/<public_id>/delete')
@api.param('public_id', 'The user identifier')
@api.response(404, 'User not found.')
class UserDelete(Resource):
    @api.doc('delete a user')
    @api.marshal_with(_user)
    def delete(self, public_id, password):
        return delete_a_user(public_id)