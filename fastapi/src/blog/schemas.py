from typing import Optional
from pydantic import BaseModel as Schema
from auth.schemas import UserOut


class BlogIn(Schema):
    title: str
    body: str
    published: Optional[bool] = True

    class Config:
        orm_mode = True


class BlogOut(Schema):
    title: str
    body: str
    published: Optional[bool] = True
    creator: UserOut

    class Config:
        orm_mode = True
