from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from settings import DATABASE_URL
from models import Astronaut, Mission


engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)


query = select(Astronaut)


with session.begin() as db:
    result = db.execute(query)

    for astro in result.scalars():
        fullname = f'{astro.firstname} {astro.lastname}'
        mission = astro.missions.name
        print(f'{fullname} -> {mission}')
