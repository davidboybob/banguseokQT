from flask_restx import Namespace, fields

class CommentsDto:
    api = Namespace(name='comments', description="Comments 관련 API")
    comments = api.model(
        'comments',
        {
            # 'id': fields.Integer(readonly=True, description= "Comments 고유 id"),
            'contents': fields.String(requried=True, description="댓글 내용"),

            # 'user_id': fields.List(fields.Integer, description="Comments를 작성한 User"),
            # 'qt_id': fields.List(fields.Integer, description="Comments가 속한 Qt "),
        }
    )