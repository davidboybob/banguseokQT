from datetime import datetime
from flask_jwt_extended import create_access_token, create_refresh_token

import jwt
from config.config import CONFIG
from models.models import RefreshToken
from utils.utils import res_object, save_changes


class JwtToken:
    @staticmethod
    def save_new_refresh_tokens(refresh_token, user_id):
        new_refresh = RefreshToken(
                        refresh=refresh_token,
                        user_id=user_id
                    )
        save_changes(new_refresh)
    
    @classmethod
    def create_tokens(cls, user_id):
        access_token=create_access_token(identity=user_id, fresh=True)
        refresh_token=create_refresh_token(identity=user_id)
        tokens = {'accees_token': access_token, 'refresh_token': refresh_token}
        cls.save_new_refresh_tokens(refresh_token, user_id)
        return res_object('success', 'Create access,refresh tokens.', 201, tokens)


def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            CONFIG.SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as err:
        return err