from flask_restx import Namespace, fields

class UserDto:
    api = Namespace(name='user', description='User 정보 관련 API')
    user = api.model(
        'user',
        {
            # 'id': fields.Integer(readonly=True, description="User 고유 id"),
            'name': fields.String(required=True, description="User 이름"),
            'email': fields.String(required=True, description="User 이메일, 아이디로 사용"),
            'password': fields.String(required=True, description="User 암호화된 비밀번호"),
            'public_id': fields.String(description="User Identifier(Id)"),
            'own_donations_mount': fields.Integer(description="User 후원금"),
            # 'created_at': fields.DateTime(description="User 생성 일자"),
            # 'updated_at': fields.DateTime(description="User 생성 일자"),
            
            # 'qt_id': fields.List(fields.Integer, description="User Qt 리스트"),
            # 'commnets_id': fields.List(fields.Integer, description="User 댓글 리스트"),
            # 'challenges_id': fields.List(fields.Integer, description="User 챌린지 리스트"),
            # 'donation_id': fields.List(fields.Integer, description="User 도네이션 리스트"),
        }
    )