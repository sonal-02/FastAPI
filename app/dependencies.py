from fastapi import Header, HTTPException
from utils.token.get_token import Token


async def get_token_header(token: str = Header()):
    print("sssss", token)
    token_obj = Token()
    if not token_obj.check_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")


# async def get_item_token(token: str = Header()):
#     if check_token(token):
#         raise HTTPException(status_code=400, detail="Invalid token")
