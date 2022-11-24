import hashlib
from models.token import token_db

def get_token(username):
    token = hashlib.sha256(str(username).encode('utf-8'))
    return token.hexdigest() 

def check_token(token):
    access_token = token_db.get('access_token', None)
    return access_token == token
