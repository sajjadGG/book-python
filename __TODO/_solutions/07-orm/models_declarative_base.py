from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Date, DateTime, Enum, Float, Numeric, Boolean
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///tmp2.db')
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


with engine.connect() as db:
    DatabaseModel.metadata.create_all(db)
