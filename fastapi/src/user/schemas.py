from pydantic import BaseModel as Schema


class UserIn(Schema):
    username: str
    email: str
    password: str


class UserOut(Schema):
    username: str
    email: str

    class Config:
        orm_mode = True
