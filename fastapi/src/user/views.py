from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import database
from user.helpers import Password
from user.models import User
from user.schemas import UserIn, UserOut


api = APIRouter(tags=['User'])


@api.post('/user', response_model=UserOut)
def create_user(request: UserIn, db: Session = Depends(database)):
    new_user = User(username=request.username,
                    password=Password.encrypt(request.password),
                    email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@api.get('/user/{id}', response_model=UserOut)
def get_user(id: int, db: Session = Depends(database)):
    if user := db.query(User).filter(User.id == id).first():
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User does not exist')
