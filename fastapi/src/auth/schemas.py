from typing import Optional
from pydantic import BaseModel as Schema


class UserIn(Schema):  # CreateUserRequest
    username: str
    email: str
    password: str


class UserOut(Schema):  # CreateUserResponse
    username: str
    email: str

    class Config:
        orm_mode = True


class LoginRequest(Schema):
    username: str
    password: str


class Token(Schema):
    access_token: str
    token_type: str


class TokenData(Schema):
    username: Optional[str] = None
