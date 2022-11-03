from flask_restx import Namespace, fields

class AuthDto:
    api = Namespace(name='auth', description='인증 관련 작업')
    auth = api.model(
        'auth_details', 
        {
            'email': fields.String(required=True, description='사용자 이메일 주소'),
            'password': fields.String(required=True, description='사용자 패스워드')  
    })