from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import DATABASE_URL
from models import Astronaut, Mission


engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)


with session.begin() as db:
    ares1 = Mission(year=2031, name='Ares1')
    ares3 = Mission(year=2035, name='Ares3')

    mark = Astronaut(firstname='Mark', lastname='Watney')
    mark.missions = ares3

    db.add(ares1)
    db.add(ares3)
    db.add(mark)
