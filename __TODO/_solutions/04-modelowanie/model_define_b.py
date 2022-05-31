"""
* Assignment: Model Define UserAddress
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
    2. Stwórz model `Address` z polami:
        a. type - rodzaj adresu: rozliczeniowy, dostawy
        b. street - ulica, numer domu, numer mieszkania
        c. postcode - kod pocztowy
        d. city - miasto
        e. region - województwo lub stan
        f. country - kraj
    3. Wymagania funkcjonalne:
        a. Adres może nie mieć ulicy lub kodu pocztowego
    4. Wymagania niefunkcjonalne:
        a. Użyj SQLAlchemy ORM do stworzenia modeli
        b. Dodaj pola `id` jeżeli są potrzebne
        c. Możesz użyć dowolnego modułu z biblioteki standardowej
        d. Możesz użyć SQLAlchemy i Alembic
        e. Nie instaluj ani nie używaj dodatkowych pakietów
"""

from sqlalchemy import Table, Column, MetaData, create_engine
from sqlalchemy import String, Integer, Date, BigInteger, Enum


Model = MetaData()

address = Table('addresses', Model,
    Column('id', Integer, primary_key=True),
    Column('type', Enum('shipment', 'billing'), nullable=False),
    Column('street', String(100), nullable=True),
    Column('postcode', String(10), nullable=True),
    Column('city', String(100), nullable=True),
    Column('region', String(100), nullable=True),
    Column('country', String(100), nullable=True)
)

engine = create_engine('sqlite:///tmp1.db')

with engine.connect() as db:
    Model.create_all(db)
