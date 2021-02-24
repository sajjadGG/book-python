from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from auth.models import User
from auth.schemas import UserIn, UserOut
from auth.helpers import create_access_token

api = APIRouter(tags=['Auth'])


@api.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends()):
    try:
        user = User.login(request.username, request.password)
        return {'access_token': create_access_token({'sub': user.username}),
                'token_type': 'bearer'}
    except (User.DoesNotExist, PermissionError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')


@api.post('/user', response_model=UserOut)
def create_user(request: UserIn):
    return User.add(username=request.username,
                    password=request.password,
                    email=request.email)


@api.get('/user/{id}', response_model=UserOut)
def get_user(id: int):
    try:
        return User.get(User.id == id)
    except User.DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User does not exist')
