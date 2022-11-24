from fastapi import HTTPException
from models.token import token_db
from models.users import users_db
from utils.user.get_user import get_user

def get_permission():
    username = token_db.get('username', None)
    user = get_user(users_db, username)
    return user.permissions

def check_permission(router):
    permissions = get_permission()
    if router.prefix not in permissions:
        raise HTTPException(status_code=400, detail="permission denied")