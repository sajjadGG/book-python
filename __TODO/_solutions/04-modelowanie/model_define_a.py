"""
* Assignment: Model Define User
* Complexity: medium
* Lines of code: 20 lines
* Time: 13 min

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Stwórz model `User` z polami:
        a. firstname - imię
        b. lastname - nazwisko
        c. born - data urodzenia
        d. ssn - PESEL
        e. email - adres email
        f. phone - telefon z numerem kierunkowym kraju
    2. Wymagania funkcjonalne:
        a. Użytkownik ma tylko jeden email i jeden telefon
    3. Wymagania niefunkcjonalne:
        a. Użyj SQLAlchemy ORM do stworzenia modeli
        b. Dodaj pola `id` jeżeli są potrzebne
        c. Możesz użyć dowolnego modułu z biblioteki standardowej
        d. Możesz użyć SQLAlchemy i Alembic
        e. Nie instaluj ani nie używaj dodatkowych pakietów
"""

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, MetaData
from sqlalchemy import String, Integer, Date, BigInteger


Model = MetaData()

user = Table('users', Model,
    Column('id', Integer, primary_key=True),
    Column('firstname', String(50), nullable=False),
    Column('lastname', String(50), nullable=True, index=True),
    Column('born', Date),
    Column('ssn', BigInteger),
    Column('email', String(100), index=True),
    Column('phone_original', String(20)),
    Column('phone_normalized', BigInteger),
)



engine = create_engine('sqlite:///tmp1.db')

with engine.connect() as db:
    Model.create_all(db)
