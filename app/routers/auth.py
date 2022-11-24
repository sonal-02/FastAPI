from fastapi import Depends, HTTPException, APIRouter, Form
from fastapi.security import OAuth2PasswordRequestForm
from utils.user.hash_password import  verify_password
from utils.token.get_token import get_token
from utils.user.get_user import get_user
from models.users import users_db
from models.token import token_db
from pydantic import SecretStr

router = APIRouter(tags=["Authentication"])

class CustomOAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    def __init__(
            self,
            username: str = Form(...),
            password: SecretStr = Form(...),
    ):
        super().__init__(
            grant_type="",
            username=username,
            password=password,
            scope="",
            client_id="",
            client_secret="",
        )


@router.post("/login")
async def user_login(form_data: CustomOAuth2PasswordRequestForm = Depends()):
    user = get_user(users_db, form_data.username)
    if not user or not verify_password(str((form_data.password).get_secret_value()), user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    token_db.update({"username": form_data.username, "access_token": get_token(user.username)})
    return {"access_token": get_token(user.username), "token_type": "bearer"}


@router.post("/logout")
async def user_logout():
    token_db.update({"username": "", "access_token": ""})
    return {"message": "User logged out"}