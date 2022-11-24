from fastapi import Depends, HTTPException, APIRouter, Form, status
from fastapi.security import OAuth2PasswordRequestForm
from utils.user.hash_password import Password
from utils.token.get_token import Token
from utils.user.get_user import CurrentUser
from models.users import users_db
from models.token import token_db
from pydantic import SecretStr

router = APIRouter(tags=["Authentication"])


class CustomOAuth2PasswordRequestForm(OAuth2PasswordRequestForm):
    """
    This class overrides the OAuth2PasswordRequestForm class and kept only username and password
    """
    def __init__(self,  username: str = Form(...), password: SecretStr = Form(...)):
        super().__init__(grant_type="", username=username,
                         password=password, scope="", client_id="", client_secret="")


@router.post("/login")
async def user_login(form_data: CustomOAuth2PasswordRequestForm = Depends()):
    """
    This api is used for user logged in. It accepts username and password and return token
    """
    user = CurrentUser.get_user(users_db, form_data.username)
    password = Password(
        str((form_data.password).get_secret_value()), user.hashed_password)
    if not user or not password.verify_password():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
    token = Token()
    access_token = token.get_token(user.username)
    token_db.update({"username": form_data.username, "access_token": access_token})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def user_logout():
    """
    This api is used to user logging out
    """
    token_db.update({"username": "", "access_token": ""})
    return {"status_code": status.HTTP_200_OK, "message": "User logged out"}
