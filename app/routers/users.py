from fastapi import Depends, HTTPException, APIRouter
from utils.user.get_user import get_current_user
from dependencies import get_token_header
from models.users import users_db
from utils.permissions.get_permissions import check_permission

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/me")
async def user_me():
    check_permission(router)
    current_user = get_current_user()
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.get("/all")
async def get_users():
    check_permission(router)
    return users_db 
