Connection Session
==================


Rationale
---------
* 1.0 style (legacy)
* 2.0 style (with context managers)

.. glossary::

    session
        Manages persistence operations for ORM-mapped objects


SetUp
-----
>>> from sqlalchemy import create_engine
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>> engine = create_engine(DATABASE)


Sessionmaker
------------
* ``Session`` manages persistence operations for ORM-mapped objects

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

In order to use ``sessionmaker()`` you have to import it:

>>> from sqlalchemy.orm import sessionmaker


1.x Style
---------
To crate a session object simply use the ``sessionmaker()`` factory passing
(binding) an engine instance:

>>> Session = sessionmaker(bind=engine)
>>> session = Session()

Or you can simplify the expression by calling class right away:

>>> session = sessionmaker(bind=engine)()

Or using a bit more verbose, but explicit syntax:

>>> session = sessionmaker(bind=engine).__call__()


2.x Style
---------
>>> Session = sessionmaker(engine)
>>>
>>> with Session() as session:
...     # do something

Context manager on ``with`` block exit will commit transaction and close the
session automatically:

>>> Session = sessionmaker(engine)
>>>
>>> with Session.begin() as session:
...     # do something


Example
-------
>>> from sqlalchemy import create_engine
>>> from sqlalchemy.orm import sessionmaker
>>>
>>>
>>> DATABASE = 'sqlite:///:memory:'
>>>
>>> engine = create_engine(DATABASE)
>>> session = sessionmaker(bind=engine).__call__()
>>>
>>> with session.begin() as db:
...     db.execute('SELECT * FROM users')
