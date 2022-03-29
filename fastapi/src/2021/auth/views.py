from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm

from auth.helpers import create_access_token
from auth.models import User
from auth.schemas import LoginRequest
from auth.schemas import UserCreate
from auth.schemas import UserOut

api = APIRouter(tags=['Auth'])


@api.post('/login.html')
def login(request: OAuth2PasswordRequestForm = Depends()):
    try:
        user = User.login(request.username, request.password)
        token = create_access_token({'sub': user.username})
        return {'access_token': token, 'token_type': 'bearer'}
    except (User.DoesNotExist, PermissionError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid credentials')


@api.post('/login.json')
def login(request: LoginRequest):
    try:
        user = User.login(request.username, request.password)
        token = create_access_token({'sub': user.username})
        return {'access_token': token, 'token_type': 'bearer'}
    except (User.DoesNotExist, PermissionError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Invalid credentials')


@api.post('/user', response_model=UserOut)
def create_user(request: UserCreate):
    return User.add(username=request.username,
                    password=request.password,
                    email=request.email)


@api.get('/user/{id}', response_model=UserOut)
def get_user(id: int):
    try:
        return User.get(User.id == id)
    except User.DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User does not exist')
