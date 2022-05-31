SQLAlchemy
==========


Co to jest
----------
* SQLAlchemy to tzw. ORM
* Object-Relation Mapper
* Obsługuje wiele baz danych (SQLite3, MySQL, PostgreSQL, ORACLE, MSSQL, ...)
* Ułatwia przenoszenie kodu, pomiędzy bazami danych
* Dzieli się na dwie główne części: core, orm

DBAPI
-----
DBAPI (każdy driver w Python, do każdej relacyjnej bazy danych):

* ``driver.connect()`` -> ``connection``
* ``connection.cursor()`` -> ``cursor``
* ``connection.backup()`` -> ``result``
* ``connection.rollback()`` -> ``result``
* ``connection.commit()`` -> ``result``
* ``connection.execute(SQL)`` -> ``result``
* ``connection.executemany(SQL, data)`` -> ``result``
* ``connection.executescript(FILE)`` -> ``result``
* ``result.fetchone()`` -> ``tuple``
* ``result.fetchmany(size=5)`` -> ``list[tuple]``
* ``result.fetchall()`` -> ``list[tuple]``
* ``connection.close()``
* ``cursor.lastrowid`` -> int
* ``cursor.rowcount`` -> int

SQLite3:

* ``cursor.row_factory = sqlite3.Row`` -> ``list[Row] -> list[dict]``
* ``connection.row_factor`` -> ``list[Row] -> list[dict]``


Drivers
-------
* ``sqlite3`` - wbudowany w Python i nie trzeba go instalować
* ``aiosqlite`` - do asynchronicznej komunikacji z SQLite3
* ``psycopg2-binary`` - do PostgreSQL
* ``asyncpg`` - do PostgreSQL obsługuje asynchroniczne wywołania
* ``pymysql`` - do MySQL
* ``pyodbc`` - do MSSQL
* ``cx`` - do Oracle

* ``psycopg2`` -> źródła i trzeba to skompilować, tzn. mieć gcc/g++, plus headery do libpostgres-dev
* ``psycopg2-binary`` -> nie trzeba kompilować


SQLAlchemy
----------
* Korzysta z wzorca projektowego Unit of Work
* Składa się z Core i ORM
* Rozpoczęcie context managera (blok ``with``) robi ``BEGIN TRANSACTION``
* Zakończenie context managera (blok ``with``) robi ``COMMIT``

Unit of Work:

>>> query = select(...).where(...)
>>>
>>> with session.begin() as db:
...     Table.metadata.create_all(db)
...     db.add(...)
...     db.add(...)
...     db.add(...)
...     result = db.execute(query).all()


Core
----
Zalety:

* służy do generowania zapytań SQL, za pomocą Pythonowych obiektów
* Zamiennik do SQL
* Pythonowe obiekty i klasy łatwiej się refaktorują niż stringi (SQL):
* SQLAlchemy zapewni nam również przenaszalność między bazami danych
* Pozwalają na testowanie zapytań do bazy danych
* Często zapytania SQL, które ułoży SQLAlchemy są lepsze niż nasze (np. cte, transakcje, savepointy)
* Nie musisz mieć aż takiej kontroli nad wszystkim
* Możliwość wykorzstania ORM oraz migracji

Wady:

* Dodatkowa warstwa abstrakcji -> większa złożoność kodu, więcej możliwości błędów i przeoczeń
* Zapytania SQL są często bardzie optymalne
* Często niektóre elementy są nadmiarowe (np. cte, transakcje, savepoint)
* Przy czystym SQL, macie większą kontrolę
* Nie ma wersjonowania schemy i zapytań

Pythonowe obiekty i klasy łatwiej się refaktorują niż stringi (SQL):

>>> query = 'SELECT DISTINCT(lastname) FROM astronaut'
>>> query = 'SELECT DISTINCT(lname) FROM astronaut'

>>> class Astronaut(...):
...     firstname = ...
...     lastname = ...
>>>
>>>
>>> query = select(Astronaut.firstname, Astronaut.lastname).distinct()

>>> class Astronaut(...):
...     fname = ...
...     lname = ...
>>>
>>>
>>> query = select(Astronaut.fname, Astronaut.lname).distinct()

SQLAlchemy zapewni nam również przenaszalność między bazami danych:

>>> query = 'SELECT DISTINCT(lname) FROM astronaut'
>>> query = 'SELECT DISTINCT lname FROM astronaut'

Pozwalają na testowanie zapytań do bazy danych:

>>> from sqlalchemy import create_mock_engine
>>>
>>>
>>> class Astronaut(...):
...     firstname = ...
...     lastname = ...
>>>
>>>
>>> engine = create_mock_engine()
>>> query = select(Astronaut.firstname, Astronaut.lastname).distinct()
>>>
>>> with engine.connect() as db:
...     ...


Wersjonowanie schemy
--------------------
* Zapisywanie jak wyglądała tabela przez i po modyfikacji
* Najczęściej dotyczy ``CREATE TABLE`` - co się zmieniło od oryginalnego stanu
* Zapisywanie wszystkich ``ALTER TABLE`` i zmian które zrobiły, np. dodawanie kolumn, usuwanie kolumn, zmiana nazw kolumn, w szczególnych przypadkach zmiana typu kolumny (ale z tym są problemy)
* Dzięki wersjonowaniu możemy zapisać schemat bazy danych do systemu kontroli wersji (VCS) np. GIT i później sprawdzać, kto i co zmienił

Framework:

* ``liquidbase`` - popularne w świecie Javy, migracje piszemy w SQL
* ``flywaydb`` - popularne w świecie Javy, migracje piszemy w SQL
* ``alembic`` - popularne w świecie Python w połączeniu z SQLAlchemy
* ``django-migrations`` - popularne w świecie Python w połączeniu z Django
* ``rails migrations`` - popularne w świecie Ruby


Engine
------
* Tworzy fabrykę połączeń do bazy danych
* Działa lazy, tzw. nie łączy się do bazy danych od razu
* Łączy się do bazy danych najpóźniej jak to tylko możliwe

>>> from sqlalchemy import create_engine
>>>
>>> DATABASE = 'postgresql://user:password@host:port/database?encoding=utf-8&keepalive=1'
>>> engine = create_engine(DATABASE)
>>>
>>> with engine.connect() as db:
...     db.execute(SQL)


Schema / Types
--------------
* Odwzorowanie bazy danych na obiekt Python

>>> from sqlalchemy import Table, Column, MetaData
>>> from sqlalchemy import String, Integer
>>>
>>>
>>> Model = MetaData()
>>>
>>> astronaut = Table('astronaut', Model,
...     id = Column(Integer, primary_key=True),
...     firstname = Column(String(30), nullable=False),
...     lastname = Column(String(50), nullable=False, index=True),
...     email = Column(String(50), unique=True),
... )


SQL Expression Language
-----------------------
* Generowanie zapytań SQL na podstawie obiektów Pythona

>>> from sqlalchemy import select
>>>
>>>
>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where(astronaut.c.lastname == 'Watney'))
>>>
>>> with engine.connect() as db:
...     result = db.execute(query)
>>>
>>> print(query)
SELECT firstname, lastname
FROM astronaut
WHERE lastname == 'Watney'


>>> import sqlite3
>>>
>>>
>>> query = """
...
... SELECT firstname, lastname
... FROM astronaut
... WHERE lastname == 'Watney'
...
... """
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     result = db.execute(query)


Core vs ORM
-----------
Core:

* służy do generowania zapytań
* Specyfikujemy scheme wykorzystując Table i Column
* Database first approach
* Najczęściej korzystamy z niego gdy już jest baza danych, a my chcemy się do niej połączyć i wykonywać zapytania

ORM:

* wykorzystuje core do generowania zapytań
* pozwala na definiowania klasy w Python i mapowanie ich tabele
* Python first approach
* Najczęściej się wykorzystuje gdy rozpoczynamy projekt, a wszystkie operacje z bazą danych przechodzą przez niego (staje się centralnym punktem aplikacji)

Core i ORM:

* Od wersji 1.4/2.0 coraz więcej różnic się zaciera
* Bardzo dużo metod z ORM trafiło do core w wersji 1.4/2.0


1.4/2.0
-------
* duża zmiana od 2.0
* wersja 1.4 to jest wersja pomostowa, gdzie można pisać tak jak dotychczas, a także w nowym stylu (2.0)
* jest możliwość włączenia kompatybilności z 2.0 za pomocą flagi ``future=True`` do ``create_engine()``


DSN
---
>>> DATABASE = 'postgresql://myusername:mypassword@myhost:myport/mydatabase'
>>> DATABASE = 'sqlite:///mydatabase'

>>> DATABASE = 'sqlite:///myfile.db'
>>> DATABASE = 'sqlite:///:memory:'
>>> DATABASE = 'sqlite:///'  # znaczy :memory:

>>> DATABASE = 'sqlite:////path/to/myfile.db'
>>> DATABASE = 'sqlite:///C:\\path\\to\\myfile.db'
>>> DATABASE = r'sqlite:///C:\path\to\myfile.db'

>>> path = '/home/mwatney/myfile.db'
>>> DATABASE = f'sqlite:///{path}'
>>>
>>> DATABASE
'sqlite:////home/mwatney/myfile.db'


Connection
----------
* ``future=True`` - włącza kompatybilność z wersją 2.0
* ``echo=True`` - włącza pogląd zapytań SQL

>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE, future=True)
>>>
>>> with engine.connect() as db:
...     ...


Raw Queries
-----------
>>> from sqlalchemy import create_engine, text
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE, future=True)
>>>
>>> query = text('SELECT * FROM apollo11')
>>>
>>>
>>> with engine.connect() as db:
...     result = db.execute(query).all()
>>>
>>> print(result)


Session
-------
* Mechanizm Unit of Work
* Do sesji możemy coś dodawać, kasować, updatetować
* Na zakończenie sesji wszystkie te rzeczy trafiają do bazy danych


Session vs Engine
-----------------
* Engine zajmuje się połączeniami
* Pracując z Core, będziemy korzystali z Engine
* Pracując z ORM, będziemy korzystali z Session
