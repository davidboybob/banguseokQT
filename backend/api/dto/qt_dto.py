from flask_restx import Namespace, fields


class QtDto:
    api = Namespace(name='qt', description='Qt 정보 관련 API')
    qt = api.model(
        'qt',
        {
            # 'id': fields.Integer(readonly=True, description= "Qt 고유 id"),
            'blog_url': fields.String(description="블로그 URL"),
            'title': fields.String(description="QT 제목"),
            'contents': fields.String(description="QT 내용"),

            # 'user_id': fields.List(fields.Integer, description="Qt 작성한 User 정보"),
            # 'comments_id': fields.List(fields.Integer, description="Qt에 작성된 Commencts"),
            # 'challenges_id': fields.List(fields.Integer, description="Qt가 속한 Challenges"),
        }
    )
    # print(UserDto.user.get('name'))