from fastapi import Header, HTTPException, Depends
from utils.user.get_user import get_current_user
from utils.basemodel.user import User
from utils.token.get_token import get_token

async def get_token_header(token: str = Header(), current_user: User = Depends(get_current_user)):
    get_user_token = get_token(current_user.username)
    print("====", get_user_token, token)
    if token != get_user_token:
        raise HTTPException(status_code=400, detail="Invalid token")


async def get_item_token(token: str = Header(), current_user: User = Depends(get_current_user)):
    get_user_token = get_token(current_user.username)
    if token == get_user_token:
        raise HTTPException(status_code=400, detail="Invalid token")