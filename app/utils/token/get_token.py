import uuid
from models.token import token_db

class Token:
    """
    Token class is used to generate token and check the token is valid or not
    """
    @staticmethod
    def get_token(username):
        return uuid.uuid4().hex

    @staticmethod
    def check_token(token):
        access_token = token_db.get('access_token', None)
        print("==a=a", access_token, token)
        return access_token == token
