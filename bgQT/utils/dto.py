from flask_restx import Namespace, fields

class UserDto:
    api = Namespace(name='user', description='User 정보 관련 API')
    user = api.model(
        'user',
        {
            'id': fields.String(readonly=True, description="사용자 고유 id"),
            'email': fields.String(required=True, description="사용자 이메일, 아이디로 사용"),
            'name': fields.String(required=True, description="사용자 이름"),
            'own_donations_mount': fields.Integer(description="사용자 후원금"),
            'password': fields.String(required=True, description="사용자 암호화된 비밀번호"),
            'public_id': fields.String(description="사용자 Identifier(Id)")

        }
    )