from fastapi import HTTPException, status
from models.token import token_db
from models.users import users_db
from utils.user.get_user import CurrentUser


class Permission:
    """
    The permission class is used to get permissions of user also check the user have specific permission or not
    """

    def __init__(self, router=None):
        self.router = router

    @staticmethod
    def get_permission():
        username = token_db.get('username', None)
        user = CurrentUser.get_user(users_db, username)
        return user.permissions

    def check_permission(self):
        permissions = Permission.get_permission()
        if self.router.prefix not in permissions:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Permission denied")
