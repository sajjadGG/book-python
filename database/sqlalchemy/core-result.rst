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


All
---
>>> query = (
...     select(astronaut.c.firstname).
...     where(astronaut.c.lastname == 'Watney')
... )
>>>
>>> with engine.begin() as db:
...     db.execute(query).all()


One
---
* Must be exactly one result, otherwise the exception is raised

>>> query = (
...     select(astronaut.c.firstname).
...     where(astronaut.c.lastname == 'Watney')
... )
>>>
>>> with engine.begin() as db:
...     db.execute(query).one()


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
