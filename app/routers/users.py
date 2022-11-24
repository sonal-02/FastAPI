from fastapi import Depends, HTTPException, APIRouter, status
from utils.user.get_user import CurrentUser
from dependencies import get_token_header
from models.users import users_db
from utils.permissions.get_permissions import Permission

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/me")
async def user_me():
    """
     This api is used to return current user information
    """
    permission = Permission(router)
    permission.check_permission()
    current_user = CurrentUser.get_current_user()
    if not current_user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")
    return current_user


@router.get("/all")
async def get_users():
    """
     This api is used to return all user details
    """
    permission = Permission(router)
    permission.check_permission()
    return users_db
