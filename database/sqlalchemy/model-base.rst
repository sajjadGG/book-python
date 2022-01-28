Connection Engine
=================


Rationale
---------
.. glossary::

    base
        Model responsible for mapping objects with database


Session
-------
* 1.0 style
* 2.0 style with context managers
* ``Session`` manages persistence operations for ORM-mapped objects

First import required dependencies:

>>> from sqlalchemy.orm import sessionmaker

``sessionmaker`` acts as a factory for ``Session`` objects in the same way as
an ``Engine`` acts as a factory for ``Connection`` objects. In this way it also
includes a ``sessionmaker.begin()`` method, that provides a context manager
which both begins and commits a transaction, as well as closes out the
``Session`` when complete, rolling back the transaction if any errors occur.

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

Usage:

>>> Session = sessionmaker(engine)
>>>
>>> with Session() as session:
...     session.add(object1)
...     session.add(object2)
...     session.commit()

Context manager on ``with`` block exit will commit transaction and close the
session automatically:

>>> Session = sessionmaker(engine)
>>>
>>> with Session.begin() as session:
...     session.add(object1)
...     session.add(object2)


Base
----
* Used for reflecting database tables in our program
* Allows to manage and alter database tables
* Declarative base (recommended)
* Imperative base (legacy)

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
