from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from auth.schemas import TokenData, UserIn, UserOut
from settings import AUTH_ALGORITHM, AUTH_SECRET_KEY, AUTH_ACCESS_TOKEN_EXPIRE_MINUTES

# Route where FastAPI will get token /login in this case
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


class Password:
    context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    def encrypt(cls, plaintext_password):
        return cls.context.hash(plaintext_password)

    @classmethod
    def verify(cls, plaintext_password, hashed_password):
        return cls.context.verify(plaintext_password, hashed_password)


def create_access_token(data: dict):
    now = datetime.now(tz=timezone.utc)
    expire = timedelta(minutes=AUTH_ACCESS_TOKEN_EXPIRE_MINUTES)
    token_expiration = now + expire
    to_encode = data.copy()
    to_encode.update({'exp': token_expiration})
    return jwt.encode(claims=to_encode, key=AUTH_SECRET_KEY, algorithm=AUTH_ALGORITHM)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserOut(**user_dict)


def verify_token(token: str):
    UnauthorizedException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-=Authenticate': 'Bearer'})

    try:
        payload = jwt.decode(token, AUTH_SECRET_KEY, algorithms=[AUTH_ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise UnauthorizedException
        return TokenData(username=username)
    except JWTError:
        raise UnauthorizedException


def get_current_user(token: str = Depends(oauth2_scheme)):
    return verify_token(token)


def get_current_active_user(current_user: UserIn = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail='Inactive user')
    return current_user
