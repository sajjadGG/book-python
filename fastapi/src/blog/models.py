from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Model


class Blog(Model):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    published = Column(Boolean)
    creator_id = Column(Integer, ForeignKey('auth_users.id'))
    creator = relationship('User', back_populates='created')
