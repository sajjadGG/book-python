SQLAlchemy About
================


Rationale
---------
* Converts Python objects to database rows
* Converts database rows to Python objects
* Provides abstraction over database layer
* Allows for object like interaction with database
* Provides ability to migrate database schema

.. todo:: Percent of market share


Database Support
----------------
* SQLite3
* PostgreSQL
* Oracle
* MySQL
* MSSQL


Installation
------------
.. code-block:: console

    $ pip install sqlalchemy

>>> import sqlalchemy
>>>
>>>
>>> sqlalchemy.__version__ > '1.4'
True


Nomenclature
------------
.. glossary::

    engine
        Database connection

    session
        Allows for transactions

    base
        Model responsible for mapping objects with database


Architecture
------------
* Core
* ORM
* Plugin structure with injection points


.. figure:: sqlalchemy-architecture.png

    SQLAlchemy architecture. Source: [#ytSQLAlchemy20]_

.. figure:: img/sqlalchemy-onion.png

    SQLAlchemy onion chart depicts layers. Source: [#ytSQLAlchemy20]_


Project Structure
-----------------
* What is the SQLAlchemy project layout
* Where to store configuration (host, port, schema, username, password)


Good Practices
--------------


References
----------
.. [#ytSQLAlchemy20] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
