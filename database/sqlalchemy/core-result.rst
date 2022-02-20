Core Result
===========


Rationale
---------
* ``.all()``
* ``.first()``
* ``.one()`` - returns exactly one row
* ``.one_or_none()``


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
>>> from sqlalchemy import Integer, String, DateTime, Numeric, Enum
>>> from sqlalchemy import select
>>>
>>>
>>> engine = create_engine('sqlite:///:memory:', future=True)
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


List[tuple]
-----------
* It will download all the data from database
* This technique is not particularly efficient for large databases

>>> query = select(astronaut.c.firstname, astronaut.c.lastname)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Watney'),
 ('Melissa', 'Lewis'),
 ('Rick', 'Martinez')]


List[dict]
----------
* It will download all the data from database
* This technique is not particularly efficient for large databases

>>> query = select(astronaut.c.firstname, astronaut.c.lastname)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> list(result.mappings())  # doctest: +NORMALIZE_WHITESPACE
[{'firstname': 'Mark', 'lastname': 'Watney'},
 {'firstname': 'Melissa', 'lastname': 'Lewis'},
 {'firstname': 'Rick', 'lastname': 'Martinez'}]


All
---
>>> query = select(astronaut.c.firstname, astronaut.c.lastname)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query).all()
>>>
>>> result  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Watney'),
 ('Melissa', 'Lewis'),
 ('Rick', 'Martinez')]

One
---
* Must be exactly one result, otherwise the exception is raised
* Exception ``MultipleResultsFound``

>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where(astronaut.c.lastname == 'Watney')
... )
>>>
>>> with engine.begin() as db:
...     db.execute(query).one()


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
