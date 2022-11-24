from fastapi import Header, HTTPException
from utils.token.get_token import check_token


async def get_token_header(token: str = Header()):
    if not check_token(token):
        raise HTTPException(status_code=400, detail="Invalid token")


# async def get_item_token(token: str = Header()):
#     if check_token(token):
#         raise HTTPException(status_code=400, detail="Invalid token")
