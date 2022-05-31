from datetime import datetime
from sqlalchemy import create_engine, select
from sqlalchemy import Column, ForeignKey, String, Integer, Date, DateTime, Enum
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


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
    mission = relationship('Mission', backref='astronaut', uselist=False)

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


if __name__ == '__main__':
    DATABASE_URL = 'sqlite:///:memory:'
    engine = create_engine(DATABASE_URL, future=True)
    session = sessionmaker(bind=engine)

    with engine.connect() as connection:
        DatabaseModel.metadata.create_all(connection)

        with session.begin() as transaction:
            ares1 = Mission(year=2031, name='Ares1')
            ares3 = Mission(year=2035, name='Ares3')

            mark = Astronaut(firstname='Mark', lastname='Watney')
            mark.missions = ares3

            transaction.add(ares1)
            transaction.add(ares3)
            transaction.add(mark)


            query = select(Astronaut)
            result = transaction.execute(query)

            for astro in result.scalars():
                fullname = f'{astro.firstname} {astro.lastname}'
                mission = astro.missions.name
                print(f'{fullname} -> {mission}')
