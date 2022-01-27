Model Relation
==============


Rationale
---------
* Foreign Key
* Primary Key
* Relation 1 do 1
* Relation 1 do ∞
* Relation ∞ do ∞


Use Case - 0x01
---------------
>>> class Astronaut(Model):
...     __tablename__ = 'astronauts'
...     id = Column(Integer, primary_key=True, index=True)
...     firstname = Column(String)
...     lastname = Column(String)
...     active = Column(Boolean, nullable=True)
...     creator_id = Column(Integer, ForeignKey('users.id'))
...     creator = relationship('User', back_populates='created')
>>>
>>>
>>> class User(Model):
...     __tablename__ = 'users'
...     id = Column(Integer, primary_key=True, index=True)
...     username = Column(String)
...     email = Column(String)
...     password = Column(String)
...     created = relationship('Astronaut', back_populates='creator')
