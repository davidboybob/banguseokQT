from models.models import User

class Auth:
    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_obejct = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        # 'Authorization': auth_token.decode()
                        'Authorization': auth_token
                    }
                    return response_obejct, 200
            else:
                response_obejct = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_obejct, 401

        except Exception as err:
            print(err)
            response_obejct = {
                'status': 'fail',
                'message': 'Try again.'
            }
            return response_obejct, 500


    @staticmethod
    def logout_user(data):
        if data:
            print(data)
            # auth_token = data.split(" ")[1]
            auth_token = data
        else:
            auth_token = ''

        if auth_token:
            response = User.decode_auth_token(auth_token)
            response_object = {
                'status': 'fail',
                'message': response
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

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