from flask import request
from flask_restx import Api, Resource, Namespace

from service.commetns_service import get_all_comments
from utils.dto import CommentsDto

api = CommentsDto.api
_comments = CommentsDto.comments

@api.route('/')
class CommentsList(Resource):
    @api.doc('list_of_qt_comments')
    @api.marshal_list_with(_comments, envelope='data')
    def get(self):
        return get_all_comments()
