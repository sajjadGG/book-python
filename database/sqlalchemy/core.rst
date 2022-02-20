SQL Alchemy Core
================
>>> from sqlalchemy import MetaData
>>> from sqlalchemy import create_engine
>>> from sqlalchemy import Table, Column
>>> from sqlalchemy import Integer, String, DateTime, Numeric, Enum
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
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

Now lets execute the statement to create database table:

>>> with engine.begin() as db:
...     astronaut.create(db)

Will generate:

.. code-block:: sql

    BEGIN
    CREATE TABLE astronaut (
        id INTEGER NOT NULL,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        born DATETIME,
        height INTEGER,
        weight NUMERIC(3, 2),
        agency VARCHAR(9),
        PRIMARY KEY (id)
    )
    COMMIT


Attributes
----------
>>> astronaut.c.firstname
Column('firstname', String(length=50), table=<astronaut>, nullable=False)


Operators
---------
>>> astronaut.c.firstname == 'Mark'
<sqlalchemy.sql.elements.BinaryExpression object at 0x123664490>

>>> x = (astronaut.c.firstname == 'Mark')
>>>
>>> x.left
Column('firstname', String(length=50), table=<astronaut>, nullable=False)
>>>
>>> x.right
BindParameter('%(4889219648 firstname)s', 'Mark', type_=String(length=50))
>>>
>>> x.operator
<built-in function eq>
>>>
>>> str(x)
'astronaut.firstname = :firstname_1'

Bound Parameters are generated from the Python expression. It prevents from
SQL injection attacks. Bound parameter sanitization and escaping is typically
done by the database driver. Bounds parameters allows also for caching.

>>> x = (astronaut.c.firstname == 'Mark')
>>> compiled = x.compile()
>>>
>>> compiled.string
'astronaut.firstname = :firstname_1'
>>>
>>> compiled.params
{'firstname_1': 'Mark'}


Criteria
========

Conjunction Options
-------------------
ColumnElements are the basic building block of SQL statement objects. To
compose more complex criteria, ``and_()`` and ``or_()`` for example provide
the basic conjunctions of AND and OR. [#ytSQLAlchemy20]_

>>> from sqlalchemy import and_, or_
>>>
>>> criteria = or_(
...     astronaut.c.firstname == 'Mark',
...     astronaut.c.firstname == 'Melissa',
... )
>>>
>>> print(criteria)
astronaut.firstname = :firstname_1 OR astronaut.firstname = :firstname_2

>>> criteria = and_(
...     astronaut.c.lastname == 'Watney',
...     or_(astronaut.c.firstname == 'Mark',
...         astronaut.c.firstname == 'Melissa')
... )
>>>
>>> print(criteria)
astronaut.lastname = :lastname_1 AND (astronaut.firstname = :firstname_1 OR astronaut.firstname = :firstname_2)

Comparison Operators
--------------------
* ``=`` - equals
* ``!=`` - not equals
* ``>`` - greater then
* ``>=`` - greater or equal to
* ``<`` - less then
* ``<=`` - less or equal to
* ``between()`` - in between two values or dates

>>> criteria = and_(
...     astronaut.c.id >= 5,
...     astronaut.c.firstname != 'Mark',
...     astronaut.c.born.between('1994-10-01', '1994-10-31'),
... )
>>>
>>> print(criteria)
astronaut.id >= :id_1 AND astronaut.firstname != :firstname_1 AND astronaut.born BETWEEN :born_1 AND :born_2


Null Checking
-------------
Compare to None produce ``IS NULL`` / ``IS NOT NULL``

>>> criteria = and_(
...     astronaut.c.firstname != None,
...     astronaut.c.agency == None,
... )
>>>
>>> print(criteria)
astronaut.firstname IS NOT NULL AND astronaut.agency IS NULL


Numerical Operators
-------------------
* Operators may also be type sensitive.
* ``+`` with numbers means 'addition'.

>>> criteria = astronaut.c.id + 5
>>>
>>> print(criteria)
astronaut.id + :id_1


String Operators
----------------
``+`` with strings means 'concatenation'.

>>> criteria = astronaut.c.firstname + 'Jr.'
>>>
>>> print(criteria)
astronaut.firstname || :firstname_1


Membership Operators
--------------------
The ``IN`` operator generates a special placeholder that will be filled in
when the statement is executed.

>>> criteria = astronaut.c.firstname.in_(['Mark', 'Melissa', 'Rick'])
>>>
>>> print(criteria)
astronaut.firstname IN (__[POSTCOMPILE_firstname_1])

When it is executed, bound parameters are generated:

>>> result = criteria.compile(compile_kwargs={'render_postcompile': True})
>>>
>>> print(result)
astronaut.firstname IN (:firstname_1_1, :firstname_1_2, :firstname_1_3)

When given an empty collection, the placeholder generates a SQL subquery
that represents an 'empty set'. This is due to that every database has a
different syntax to search for an 'empty set'.

>>> criteria = astronaut.c.firstname.in_([])
>>> result = criteria.compile(compile_kwargs={'render_postcompile': True})
>>>
>>> print(result)
astronaut.firstname IN (NULL) AND (1 != 1)


Insert
======


Statement
---------
We can insert data using the ``insert()`` construct:

>>> query = astronaut.insert().values(
...     firstname='Mark',
...     lastname='Watney',
... )
>>>
>>> with engine.begin() as db:
...     db.execute(query)
BEGIN (implicit)
INSERT INTO astronaut (firstname, lastname) VALUES (?, ?)
[generated in 0.00017s] ('Mark', 'Watney')
COMMIT

Execute
-------
The ``insert()`` statement, when not given ``values()`` will generate the
``VALUES`` clause based on the list of parameters that are passed to
``execute()``.

>>> data = {'firstname': 'Mark', 'lastname': 'Watney'}
>>>
>>> with engine.begin() as db:
...     db.execute(astronaut.insert(), data)
BEGIN (implicit)
INSERT INTO astronaut (firstname, lastname) VALUES (?, ?)
[generated in 0.00014s] ('Mark', 'Watney')
COMMIT

Executemany
-----------
This format also accepts an 'executemany' style that DBAPI can optimize

>>> data = [
...     {'firstname': 'Mark', 'lastname': 'Watney'},
...     {'firstname': 'Melissa', 'lastname': 'Lewis'},
...     {'firstname': 'Rick', 'lastname': 'Martinez'},
... ]
>>>
>>> with engine.begin() as db:
...     db.execute(astronaut.insert(), data)
BEGIN (implicit)
INSERT INTO astronaut (firstname, lastname) VALUES (?, ?)
[generated in 0.00014s] (('Mark', 'Watney'), ('Melissa', 'Lewis'), ('Rick', 'Martinez'))
COMMIT


Select
======
* Method chaining
* Note the dot ``.`` at the end of the select line


SetUp
-----
>>> from sqlalchemy import select


Select Specified Columns
------------------------
>>> query = (
...     select(astronaut.c.firstname, astronaut.c.lastname).
...     where(astronaut.c.firstname == 'Mark')
... )
>>>
>>> print(query)
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut
WHERE astronaut.firstname = :firstname_1
>>>
>>> with engine.begin() as db:
...     result = db.execute(query)
...
...     for row in result:
...         print(row)
BEGIN (implicit)
SELECT astronaut.firstname, astronaut.lastname
FROM astronaut
WHERE astronaut.firstname = ?
[generated in 0.00016s] ('Mark',)
COMMIT
('Mark', 'Watney')
('Mark', 'Watney')
('Mark', 'Watney')


Select All Columns
------------------
>>> query = select(astronaut)
>>>
>>> print(query)
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut
>>>
>>> with engine.begin() as db:
...     db.execute(query).all()
BEGIN (implicit)
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut
[generated in 0.00013s] ()
COMMIT


Order By
--------
>>> query = (
...     select(astronaut).
...     where(or_(astronaut.c.firstname == 'Mark',
...               astronaut.c.firstname == 'Melissa')).
...     order_by(astronaut.c.firstname)
... )
>>>
>>> print(query)
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut
WHERE astronaut.firstname = :firstname_1 OR astronaut.firstname = :firstname_2 ORDER BY astronaut.firstname
>>>
>>> with engine.begin() as db:
...     db.execute(query).all()
BEGIN (implicit)
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut
WHERE astronaut.firstname = ? OR astronaut.firstname = ? ORDER BY astronaut.firstname
[generated in 0.00016s] ('Mark', 'Melissa')
COMMIT

Multiple Where
--------------
* Multiple ``where()`` clauses are automatically joined by ``AND``

>>> query = (
...     select(astronaut).
...     where(astronaut.c.firstname == 'Mark').
...     where(astronaut.c.lastname == 'Watney').
...     order_by(astronaut.c.firstname)
... )
>>>
>>> print(query)
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut
WHERE astronaut.firstname = :firstname_1 AND astronaut.lastname = :lastname_1 ORDER BY astronaut.firstname
>>>
>>> with engine.begin() as db:
...     db.execute(query).all()
...
BEGIN (implicit)
SELECT astronaut.id, astronaut.firstname, astronaut.lastname, astronaut.born, astronaut.height, astronaut.weight, astronaut.agency
FROM astronaut
WHERE astronaut.firstname = ? AND astronaut.lastname = ? ORDER BY astronaut.firstname
[generated in 0.00014s] ('Mark', 'Watney')
COMMIT


Result
======
* ``.all()``
* ``.first()``
* ``.one()`` - returns exactly one row
* ``.one_or_none()``


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
...     db.execute(query).all()


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
