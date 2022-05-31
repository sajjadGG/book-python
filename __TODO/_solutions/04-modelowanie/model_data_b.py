"""
* Assignment: Model Data AstronautAgency
* Complexity: easy
* Lines of code: 11 lines
* Time: 8 min

English:
    1. Create propper classes to model the data:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. Create instances (watney, nasa) filling it with data
    3. Non-functional requirements:
        a. Use SQLAlchemy ORM to create models
        b. Do not convert data, just model it
        c. You can use any Python standard library module
        d. You can use SQLAlchemy and Alembic
        e. Do not install or use 3rd party modules
    4. Run doctests - all must succeed

Polish:
    1. Stwórz odpowiednie klasy aby zamodelować dane:
       a. Watney, USA, 1969-07-21
       b. NASA, USA, 1958-07-29
    2. Stwórz instancje (watney, nasa) wypełniając je danymi
    3. Wymagania niefunkcjonalne:
        a. Użyj SQLAlchemy ORM do stworzenia modeli
        b. Nie konwertuj danych, tylko je zamodeluj
        c. Możesz użyć dowolnego modułu z biblioteki standardowej
        d. Możesz użyć SQLAlchemy i Alembic
        e. Nie instaluj ani nie używaj dodatkowych pakietów
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
"""


from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, String


Model = MetaData()

# object: Model from data: 'Watney', 'USA', '1969-07-21'
astronaut = Table('astronauts', Model,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    Column('country', String(20)),
    Column('date', String(20)),
)

# object: Model from data: 'NASA', 'USA', '1958-07-29'
agency = Table('agencies', Model,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    Column('country', String(20)),
    Column('date', String(20)),
)


# class Astronaut:
#     name: str
#     country: str
#     date: str
#
#
# class Agency:
#     name: str
#     country: str
#     date: str
#
#
# watney = Astronaut()
# nasa = Agency()
