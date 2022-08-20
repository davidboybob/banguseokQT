from flask_restx import Namespace, fields

class UserQtSchema:
    api = Namespace(name='userqtschema', description='User에서 qt를 참조하는 데이터 API')
    userqtschema = api.model(
        'userqtschema',
        {'qt_id': fields.List(fields.Integer)}
        
    )

class UserDto:
    api = Namespace(name='user', description='User 정보 관련 API')
    user = api.model(
        'user',
        {
            # 'id': fields.Integer(readonly=True, description="사용자 고유 id"),
            'name': fields.String(required=True, description="사용자 이름"),
            'email': fields.String(required=True, description="사용자 이메일, 아이디로 사용"),
            'password': fields.String(required=True, description="사용자 암호화된 비밀번호"),
            'public_id': fields.String(description="사용자 Identifier(Id)"),
            'own_donations_mount': fields.Integer(description="사용자 후원금"),
            'created_at': fields.DateTime(description="사용자 생성 일자"),
            'updated_at': fields.DateTime(description="사용자 생성 일자"),
            # 'qt_id': fields.List(fields.Nested(QtDto.qt))
            'qt_id': fields.Nested(UserQtSchema.userqtschema),
            # 'commnets_id': fields.List(fields.Integer, description="Relationship of comments_id"),
            # 'challenges_id': fields.List(fields.Integer, description="Relationship of challenges"),
            # 'donation_id': fields.List(fields.Integer, description="Relationship of donation_id"),
        }
    )

class QtDto:
    api = Namespace(name='qt', description='Qt 정보 관련 API')
    qt = api.model(
        'qt',
        {
            # id: fields.Integer(readonly=True, description= "Qt 고유 id"),
            'blog_url': fields.String(description="블로그 URL"),
            'title': fields.String(description="QT 제목"),
            'contents': fields.String(description="QT 내용"),
            'user_id': fields.List(fields.Nested(UserDto.user))
        }
    )
    # print(UserDto.user.get('name'))

class CommentsDto:
    api = Namespace(name='comments', description="댓글 관련 API")
    comments = api.model(
        'comments',
        {
            'contents': fields.String(requried=True, description="댓글 내용")
        }
    )

class Challenges:
    api = Namespace(name='challenges', description="챌린지 관련 API")
    challenges = api.model(
        'challenges',
        {
            'state': fields.Boolean(required=True, description="챌린지 진행 여부 상태"),
            'title': fields.String(required=True, description="챌린지 제목"),
            'contents': fields.String(required=True, description="챌린지 내용"),
            'from_date': fields.DateTime(required=True, description="챌린지 시작 일자"),
            'to_date': fields.DateTime(required=True, description="챌린지 종료 일자"),
        }
    )