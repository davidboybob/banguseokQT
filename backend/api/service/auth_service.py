from flask_restx import abort
from models.models import User
from utils.jwt import JwtToken

class Auth:
    @staticmethod
    def login_user(data):
        # fetch the user data
        user = User.query.filter_by(email=data.get('email')).first()
        if not user:
            abort(401, "유저를 찾을 수 없습니다.", Error="Unauthorized.")

        if user.check_password(data.get('password')):
            tokens = JwtToken.create_tokens(user.id)
            print(tokens)
            
        else:
            abort(409, "비밀번호 또는 이메일이 일치하지 않습니다.", )


    @staticmethod
    def logout_user(data):
        pass
        # if data:
        #     print(data)
        #     # auth_token = data.split(" ")[1]
        #     auth_token = data
        # else:
        #     auth_token = ''

        # if auth_token:
        #     response = User.decode_auth_token(auth_token)
        #     response_object = {
        #         'status': 'fail',
        #         'message': response
        #     }
        #     return response_object, 401
        # else:
        #     response_object = {
        #         'status': 'fail',
        #         'message': 'Provide a valid auth token.'
        #     }
        #     return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            response = User.decode_auth_token(auth_token)
            if not isinstance(response, bool):
                user = User.query.filter_by(id=response).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'created_at': str(user.created_at)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': response
            }
            return response_object, 401
        else:
            response_object ={
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401