Connection Engine
=================


* ``create_engine()`` builds a factory for database connections
* ``echo=True`` - if True, the Engine will log all statements to stdout
* ``future=True`` - v2.0 compatibility mode (works only in v1.4)
* Uses Database Source Name (DSN) for connection
* Engine is lazily connected
* Supports context managers ``with`` block
* ``.connect()`` method explicitly connects to database


Rationale
---------
.. glossary::

    engine
        Provides a facade over the Python DBAPI. Used to create a lazy
        connection to the database.


Create Engine
-------------
Function ``create_engine()`` builds a factory for database connections. It
supports Database Source Name (DSN). In the following example we will
create a database connection factory to SQLite3 database using Python
builtin driver. The database works in memory, so it will not create any
files. Note that the connection is lazy, and creating an engine does not
implies connection to the database.

>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)


Parameters
----------
* ``echo=True`` - if True, the Engine will log all statements to stdout
* ``future=True`` - v2.0 compatibility mode (works only in v1.4)
* Full List: https://docs.sqlalchemy.org/en/stable/core/engines.html#sqlalchemy.create_engine.params.connect_args


1.x Style
---------
Creating engine with ``create_engine()`` factory will create it in the
legacy mode (compatible with 1.x). The underlying object is the same as in
the previous versions:

>>> from sqlalchemy import create_engine
>>>
>>>
>>> engine = create_engine(DATABASE)
>>>
>>> type(engine)
<class 'sqlalchemy.engine.base.Engine'>


2.x Style
---------
In order to turn on the future compatibility mode, set the ``future=True``
flag to the ``create_engine()`` factory. This will change the underlying
object to the ``future.engine``:

>>> from sqlalchemy import create_engine
>>>
>>>
>>> engine = create_engine(DATABASE, future=True)
>>>
>>> type(engine)
<class 'sqlalchemy.future.engine.Engine'>


Establishing Connection
-----------------------
Engine is lazily connected and does not connect on creating engine right
away. It does that in last possible moment (such as attribute access) or
on explicit ``.connect()`` method call.

>>> from sqlalchemy import create_engine
>>>
>>>
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


Further Reading
---------------
* https://docs.sqlalchemy.org/en/stable/core/engines.html#sqlalchemy.create_engine.params.connect_args
