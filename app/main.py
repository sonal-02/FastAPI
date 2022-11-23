from fastapi import FastAPI, Depends
from routers import users, items, token
# from dependencies import get_query_token

app = FastAPI()

app.include_router(token.router)
app.include_router(users.router)
app.include_router(items.router)

# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}