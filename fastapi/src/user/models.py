from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Model


class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created = relationship('Blog', back_populates='creator')
