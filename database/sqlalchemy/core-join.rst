Core Update
===========


Rationale
---------
>>> from sqlalchemy import update


SetUp
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
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
...     Column('agency', Enum('NASA', 'ESA', 'Roscosmos')),
...     Column('born', DateTime),
...     Column('age', Integer),
...     Column('height', Numeric(3,2)),
...     Column('weight', Numeric(3,2)),
... )
>>>
>>> mission = Table('mission', metadata,  # one to many relationship
...     Column('id', Integer, primary_key=True),
...     Column('astronaut_id', ForeignKey('astronaut.id'), nullable=False),
...     Column('year', Integer, nullable=False),
...     Column('name', String(50), nullable=False),
... )
>>>
>>> ASTRONAUTS = [
...     {'firstname': 'Mark', 'lastname': 'Watney'},
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'firstname': 'Rick', 'lastname': 'Martinez'},
... ]
>>>
>>> MISSIONS = [
...     {'astronaut_id': 1, 'year': 2035, 'name': 'Ares3'},
...     {'astronaut_id': 2, 'year': 2030, 'name': 'Ares1'},
...     {'astronaut_id': 2, 'year': 2035, 'name': 'Ares3'},
...     {'astronaut_id': 3, 'year': 2035, 'name': 'Ares3'},
... ]
>>>
>>> with engine.begin() as db:
...     metadata.create_all(db)
...     db.execute(astronaut.insert(), ASTRONAUTS)
...     db.execute(mission.insert(), MISSIONS)


Select Multiple Tables
----------------------
* ``SELECT`` from more than one table
* This will render CARTESIAN JOIN
* This can crash systems if tables are big
* Since SQLAlchemy 1.4 library will warn on cartesian products

The ``select()`` construct will include in the ``FROM`` clause all those
tables that we mention in the columns clause or ``WHERE`` clause. By default,
they are separated by a coma.

>>> query = select(astronaut.c.firstname, mission.c.name)
>>>
>>> print(query)
SELECT astronaut.firstname, mission.name
FROM astronaut, mission

Selecting from multiple tables without relating them to each other produces
an effect known as 'cartesian product'. SQLAlchemy will usually warn when this
is detected during statement execution [#ytSQLAlchemy20]_.

>>> query = select(astronaut.c.firstname, mission.c.name)
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
... # SAWarning: SELECT statement has a cartesian product between FROM
... # element(s) "astronaut" and FROM element "mission".  Apply join
... # condition(s) between each element to resolve.
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Ares3'),
 ('Mark', 'Ares1'),
 ('Mark', 'Ares3'),
 ('Mark', 'Ares3'),
 ('Melissa', 'Ares3'),
 ('Melissa', 'Ares1'),
 ('Melissa', 'Ares3'),
 ('Melissa', 'Ares3'),
 ('Rick', 'Ares3'),
 ('Rick', 'Ares1'),
 ('Rick', 'Ares3'),
 ('Rick', 'Ares3')]

Using warnings filter can turn Warning to Error. This is useful for a CI/CD
and a pre-production tests.


Join From
---------
* New in SQLAlchemy 1.4
* Have some additional features than ``join()``
* More explicitly
* Is better to start chain of joins

When we have more than one table mentioned, we want to relate them together,
which is most easily achieved using ``join_from()`` [#ytSQLAlchemy20]_.

>>> query = (
...     select(astronaut.c.firstname, mission.c.name).
...     join_from(astronaut, mission)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Ares3'),
 ('Melissa', 'Ares1'),
 ('Melissa', 'Ares3'),
 ('Rick', 'Ares3')]


Join
----
* ``join()`` will infer the left hand side automatically
* Is better for continuing chain of joins

>>> query = (
...     select(astronaut.c.firstname, mission.c.name).
...     join(mission)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Ares3'),
 ('Melissa', 'Ares1'),
 ('Melissa', 'Ares3'),
 ('Rick', 'Ares3')]


Join On
-------
* You can specify the column on which to perform a join
* Useful when there is several ``ForeignKey`` columns
* If SQLAlchemy cannot find join column automatically it throws an error

The ``ON`` clause of the ``JOIN`` is also inferred automatically from the
foreign key relationship of the involved tables. We may chose to express
this join condition explicitly, as would be needed if the join condition
were otherwise ambiguous [#ytSQLAlchemy20]_.

>>> query = (
...     select(astronaut.c.firstname, mission.c.name).
...     join(mission, astronaut.c.id == mission.c.astronaut_id)
... )
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
>>>
>>> result.all()  # doctest: +NORMALIZE_WHITESPACE
[('Mark', 'Ares3'),
 ('Melissa', 'Ares1'),
 ('Melissa', 'Ares3'),
 ('Rick', 'Ares3')]


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
