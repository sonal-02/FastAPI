import hashlib
from models.users import users_db

def get_token(username):
    token = hashlib.sha256(str(username).encode('utf-8'))
    return username + "$"  + token.hexdigest() 

def get_username(token):
    username = token.split('$')
    if username[0] in users_db:
        return username[0]
    return None