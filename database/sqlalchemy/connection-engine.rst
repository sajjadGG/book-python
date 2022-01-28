Connection Engine
=================


Rationale
---------
.. glossary::

    engine
        Provides a facade over the Python DBAPI. Used to create a lazy
        connection to the database.



Create Engine
-------------
* ``create_engine()`` builds a factory for database connections

>>> from sqlalchemy import create_engine
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)


Parameters
----------
* Parameters: https://docs.sqlalchemy.org/en/stable/core/engines.html#sqlalchemy.create_engine.params.connect_args
* ``echo=True`` - if True, the Engine will log all statements to stdout
* ``future=True`` - v2.0 compatibility mode (works only in v1.4)


1.x Style
---------
Creating engine with ``create_engine()`` factory will create it in the legacy
mode (compatible with 1.x):

>>> engine = create_engine(DATABASE)

The underlying object is the same as in the previous versions:

>>> type(engine)
<class 'sqlalchemy.engine.base.Engine'>


2.x Style
---------
In order to turn on the future compatibility mode, set the ``future=True`` flag
to the ``create_engine()`` factory:

>>> engine = create_engine(DATABASE, future=True)

This will change the underlying object to the ``future.engine``:

>>> type(engine)
<class 'sqlalchemy.future.engine.Engine'>


Establishing Connection
-----------------------
* Engine is lazily connected (does not connect on creating engine right away)

>>> with engine.connect() as db:
...     # do something


Example
-------
>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
>>>
>>> with engine.connect() as db:
...     db.execute('SELECT * FROM users')
