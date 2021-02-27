from __future__ import annotations
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from auth.helpers import Password
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
        password = Password.encrypt(password)
        return User.insert(username=username, password=password, email=email)

    @staticmethod
    def login(username: str, password: str):
        user = User.get(User.username == username)
        valid_password = Password.verify(password, user.password)
        if user and valid_password:
            return user
        else:
            raise PermissionError


