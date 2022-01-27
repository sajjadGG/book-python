Connection Engine
=================


Rationale
---------


Engine
------
* Engine component provides a facade over the Python DBAPI
* ``create_engine()`` builds a factory for database connections
* Debugging
* Parameters: https://docs.sqlalchemy.org/en/stable/core/engines.html#sqlalchemy.create_engine.params.connect_args
* Parameter ``echo=True`` if True, the Engine will log all statements to stdout
* Parameter ``future=True`` - v2.0 compatibility mode
* Engine is lazily connected (does not connect on creating engine right away)

First import required dependencies and set database connection URL:

>>> from sqlalchemy import create_engine

Then create an engine:

>>> engine = create_engine(DATABASE)

Although this will create a SQLAlchemy engine in legacy mode:

>>> type(engine)
<class 'sqlalchemy.engine.base.Engine'>

You can also turn on the future compatibility mode:

>>> engine = create_engine(DATABASE, future=True)
>>>
>>> type(engine)
<class 'sqlalchemy.future.engine.Engine'>


Connection
----------
>>> with engine.connect() as db:
...     # do something


Use Case - 0x01
---------------
>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)
>>>
>>> with engine.connect() as db:
...     db.execute('SELECT * FROM users')
