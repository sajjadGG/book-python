from datetime import datetime
from sqlalchemy import (Column, ForeignKey, String, Integer, Date, DateTime,
                        Enum, Float, Numeric, Boolean)
from sqlalchemy.orm import declarative_base, relationship


DatabaseModel = declarative_base()


class Astronaut(DatabaseModel):
    __tablename__ = 'astronaut'

    # Atrybuty systemowe
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now)
    modified = Column(DateTime, default=datetime.now)

    # Atrybuty biometryczne
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False, index=True)
    born = Column(Date, nullable=True)
    gender = Column(Enum('male', 'female'), nullable=True)

    # Atrybuty kontaktu
    email = Column(String(50), nullable=True, unique=True)
    phone = Column(String(50), nullable=True)

    # Relationships
    missions = relationship('Mission', backref='astronauts', uselist=False)

    def __repr__(self):
        firstname = self.firstname
        lastname = self.lastname
        return f'Astronaut({firstname=}, {lastname=})'


class Mission(DatabaseModel):
    __tablename__ = 'mission'

    # Atrybuty systemowe
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now)
    modified = Column(DateTime, default=datetime.now)

    # Atrybuty misji
    year = Column(Integer, nullable=True)
    name = Column(String(50), nullable=False, unique=True, index=True)

    # Relationships
    astronaut_id = Column(Integer, ForeignKey('astronaut.id'))

    def __repr__(self):
        year = self.year
        name = self.name
        return f'Mission({year=}, {name=})'

# one-to-one
# one-to-many
# many-to-one
# many-to-many
