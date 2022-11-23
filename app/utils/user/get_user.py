from fastapi import Depends, HTTPException, status
from utils.user.scheme import oauth2_user_scheme
from utils.basemodel.user import User
from models.users import users_db
from utils.token.get_token import get_username


class UserInDB(User):
    username: str
    name: str
    surname: str
    active: str
    email: str
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


async def get_current_user(token: str = Depends(oauth2_user_scheme)):
    username = get_username(token)
    if username:
        user = get_user(users_db, username)
        if user:
            return user
    raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )





