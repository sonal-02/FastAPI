from fastapi import HTTPException, status
from utils.basemodel.user import User
from models.users import users_db
from models.token import token_db


class UserInDB(User):
    username: str
    name: str
    surname: str
    active: str
    email: str
    hashed_password: str
    permissions: list


class CurrentUser:
    """
    The CurrentUser class is used to get current user. If user not found in 
    db then produce unauthorized error
    """

    @staticmethod
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username]
            return UserInDB(**user_dict)

    @staticmethod
    def get_current_user():
        username = token_db.get('username', None)
        if username:
            user = CurrentUser.get_user(users_db, username)
            if user:
                return user
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
