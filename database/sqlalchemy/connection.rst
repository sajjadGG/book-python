SQLAlchemy Connection
=====================


Rationale
---------
* JDBC connection strings


Engine
------
* Debugging
* Parameter ``echo=True``

First import required dependencies:

>>> from sqlalchemy import create_engine

Then create an engine:

>>> engine = create_engine('sqlite:///tmp/myfile.db')

Note, that the good practice will suggest to split configuration parameter
from its actual call. Therefore you can place configuration in separate file
which can be imported.

>>> DATABASE = 'sqlite:///tmp/myfile.db'
>>> engine = create_engine(DATABASE)


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

Or using a bit more verbose syntax:

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
