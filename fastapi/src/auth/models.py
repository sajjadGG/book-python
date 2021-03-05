from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from auth.password import encrypt
from auth.password import verify
from database import Model


class User(Model):
    __tablename__ = 'auth_users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created = relationship('Blog', back_populates='creator')

    @staticmethod
    def add(username: str, email: str, password: str):
        return User.insert(username=username, password=encrypt(password),
                           email=email)

    @staticmethod
    def login(username: str, password: str):
        user = User.get(User.username == username)
        valid_password = verify(password, user.password)
        if user and valid_password:
            return user
        else:
            raise PermissionError
