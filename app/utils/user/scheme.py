from fastapi.security import OAuth2PasswordBearer

oauth2_user_scheme = OAuth2PasswordBearer(tokenUrl="token")