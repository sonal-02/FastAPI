from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from utils.user.hash_password import  verify_password
from utils.token.get_token import get_token
from utils.user.get_user import get_user
from models.users import users_db


router = APIRouter()


@router.post("/token", tags=["token"])
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(users_db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": get_token(user.username), "token_type": "bearer"}
