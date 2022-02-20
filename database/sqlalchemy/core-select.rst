Core Select
===========


Rationale
---------
* Method chaining
* Note the dot ``.`` at the end of the select line

>>> from sqlalchemy import select


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
>>> from sqlalchemy import Integer, String, DateTime, Numeric, Enum
>>>
>>>
>>> engine = create_engine('sqlite:///:memory:')
>>> metadata = MetaData()
>>>
>>> astronaut = Table('astronaut', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('firstname', String(50), nullable=False),
...     Column('lastname', String(50), nullable=False),
...     Column('born', DateTime),
...     Column('height', Integer),
...     Column('weight', Numeric(3,2)),
...     Column('agency', Enum('NASA', 'ESA', 'Roscosmos')),
... )
>>>
>>> data = [
...     {'firstname': 'Mark', 'lastname': 'Watney'},
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'firstname': 'Rick', 'lastname': 'Martinez'},
... ]
>>>
>>> with engine.begin() as db:
...     astronaut.create(db)
...     db.execute(astronaut.insert(), data)


Select Specified Columns
------------------------
Define the database query:

>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where(astronaut.c.firstname == 'Mark')
... )

Inspect statement:

>>> print(query)
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut
WHERE astronaut.firstname = :firstname_1

Execute statement to the database:

>>> with engine.begin() as db:
...     result = db.execute(query)
...
...     for row in result:
...         print(row)



Select All Columns
------------------
Define the database query:

>>> query = select(astronaut)

Inspect statement:

>>> print(query)
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut

Execute statement to the database:

>>> with engine.begin() as db:
...     db.execute(query).all()


Order By
--------
Define the database query:

>>> query = (
...     select(astronaut).
...     where(or_(astronaut.c.firstname == 'Mark',
...               astronaut.c.firstname == 'Melissa')).
...     order_by(astronaut.c.firstname)
... )

Inspect statement:

>>> print(query)
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut
WHERE astronaut.firstname = :firstname_1 OR astronaut.firstname = :firstname_2 ORDER BY astronaut.firstname

Execute statement to the database:

>>> with engine.begin() as db:
...     db.execute(query).all()


Multiple Where
--------------
* Multiple ``where()`` clauses are automatically joined by ``AND``

Define the database query:

>>> query = (
...     select(astronaut).
...     where(astronaut.c.firstname == 'Mark').
...     where(astronaut.c.lastname == 'Watney').
...     order_by(astronaut.c.firstname)
... )

Inspect statement:

>>> print(query)
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut
WHERE astronaut.firstname = :firstname_1 AND astronaut.lastname = :lastname_1 ORDER BY astronaut.firstname

Execute statement to the database:

>>> with engine.begin() as db:
...     db.execute(query).all()


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
