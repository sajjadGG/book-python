Core Model
==========


Rationale
---------
* Models represents database entities (tables)


SetUp
-----
Prepare connection:

>>> from sqlalchemy import create_engine
>>>
>>> engine = create_engine('sqlite:///:memory:', future=True)

Note, that we will use future flag to turn on the 2.0 compatibility mode.


Metadata
--------
* Metadata represents connection between Python object and a database

Create Metadata object:

>>> from sqlalchemy import MetaData
>>>
>>> metadata = MetaData()


Database Model
--------------
Imports:

>>> from sqlalchemy import  Table, Column
>>> from sqlalchemy import Integer, String, DateTime, Numeric, Enum

Astronaut table specification:

>>> astronaut = Table('astronaut', metadata,
...     Column('id', Integer, primary_key=True),
...     Column('firstname', String(50), nullable=False),
...     Column('lastname', String(50), nullable=False),
...     Column('born', DateTime),
...     Column('height', Integer),
...     Column('weight', Numeric(3,2)),
...     Column('agency', Enum('NASA', 'ESA', 'Roscosmos')),
... )


Execute
-------
Execute the statement to create database table:

>>> with engine.begin() as db:
...     astronaut.create(db)

SQLAlchemy core will generate and execute the following SQL statement. Note,
that the ``CREATE TABLE`` statement is inside of the transaction. This will
ensure database consistency and rollback if any problem occur (for example
database table with the same name already exists):

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


Recap
-----
>>> from sqlalchemy import create_engine, MetaData, Table, Column
>>> from sqlalchemy import Integer, String, DateTime, Numeric, Enum
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
>>> with engine.begin() as db:
...     astronaut.create(db)
