from flask import request
from flask_restx import Api, Resource, Namespace

from service.qt_service import get_all_qts, save_new_qt, get_a_qt
from utils.dto import QtDto

api = QtDto.api
_qt = QtDto.qt

@api.route('/')
class QtList(Resource):
    @api.doc('list_of_user_qt')
    @api.marshal_list_with(_qt, envelope='data')
    def get(self):
        return get_all_qts()


    @api.response(201, 'qt successfully created.')
    @api.doc('create a new qt')
    @api.expect(_qt, validate=True)
    def post(self):
        """Create a new qt"""
        data = request.json

        return save_new_qt(data=data)


    @api.route('/<id>')
    @api.param('id', 'The qt id number')
    @api.response(404, 'Qt not found.')
    class Qt(Resource):
        @api.doc('get a qt')
        @api.marshal_with(_qt)
        def get(self, id):
            """get a user given its id"""
            qt = get_a_qt(id)

            if not qt:
                api.abort(404)
            else:
                return qt