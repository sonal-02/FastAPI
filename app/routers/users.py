from fastapi import Depends, HTTPException, APIRouter
from utils.user.scheme import oauth2_user_scheme
from utils.user.get_user import get_current_user
from dependencies import get_token_header
from utils.basemodel.user import User
from models.users import users_db


router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/me")
async def user_me(current_user: User = Depends(get_current_user)):
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.get("/all")
async def get_users(token: str = Depends(oauth2_user_scheme)):
    return users_db