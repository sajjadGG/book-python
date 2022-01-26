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


Project Structure
-----------------
* What is the SQLAlchemy project layout
* Where to store configuration (host, port, schema, username, password)


Good Practices
--------------


References
----------
.. [#yt] Bayer, Mike. SQLAlchemy 2.0 - The One-Point-Four-Ening 2021. Year: 2022. Retrieved: 2022-01-26. URL: https://www.youtube.com/watch?v=1Va493SMTcY
