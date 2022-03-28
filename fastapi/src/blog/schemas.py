from pydantic import BaseModel as Schema
from auth.schemas import UserOut


class BlogIn(Schema):
    title: str
    body: str
    published: bool | None = True

    class Config:
        orm_mode = True


class BlogOut(Schema):
    title: str
    body: str
    published: bool | None = True
    creator: UserOut

    class Config:
        orm_mode = True
