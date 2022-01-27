SQLAlchemy Connection
=====================


Rationale
---------


Engine
------
* Engine component provides a facade over the Python DBAPI
* ``create_engine()`` builds a factory for database connections
* Debugging
* Parameters: https://docs.sqlalchemy.org/en/14/core/engines.html#sqlalchemy.create_engine.params.connect_args
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
>>> connection = engine.connect()
>>> connection


Session
-------
* 1.0 style
* 2.0 style with context managers

First import required dependencies:

>>> from sqlalchemy.orm import sessionmaker

Factory function ``sessionmaker()`` will return a **class**. In order to create
a session this class has to be called. There are several ways how to do that.
You can either capture the class from session maker, instantiate it and then
assign to identifier (variable) or you can do it step by step having
intermediate objects.

>>> Session = sessionmaker(bind=engine)
>>> session = Session()

Or you can simplify the expression by calling class right away:

>>> session = sessionmaker(bind=engine)()

Or using a bit more verbose, but explicit syntax:

>>> session = sessionmaker(bind=engine).__call__()


Base
----
* Used for reflecting database tables in our program
* Allows to manage and alter database tables
* Declarative base
* Imperative base

First import required dependencies:

>>> from sqlalchemy.ext.declarative import declarative_base

Then create an engine:

>>> Base = declarative_base()


Use Case - 0x01
---------------
>>> from sqlalchemy import create_engine
>>> from sqlalchemy.ext.declarative import declarative_base
>>> from sqlalchemy.orm import sessionmaker
>>>
>>>
>>> DATABASE = 'sqlite:///tmp/myfile.db'
>>>
>>> engine = create_engine()
>>> session = sessionmaker(bind=engine).__call__()
>>> Base = declarative_base()
