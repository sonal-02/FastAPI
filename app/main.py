from fastapi import FastAPI
from routers import users, items, auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(items.router)
