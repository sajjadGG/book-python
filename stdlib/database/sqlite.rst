***************
Database SQLite
***************


Installation
============
#. To check if Sqlite3 is already installed run in Console/Terminal/CMD:

    .. code-block:: console

        $ sqlite3 --version

#. If it's not installed, then:

    * Download from https://sqlite.org/download.html
    * Extract archive
    * Add ``sqlite`` executable to ``$PATH``:

        * \*nix systems (Linux, macOS, etc...): move ``sqlite`` executable to ``/usr/local/bin/``
        * Windows (better): Add folder with extracted ``sqlite`` executable to ``$PATH`` directory by following instruction (https://python.astrotech.io/install.html)
        * Windows (simple): If you have GIT installed, move ``sqlite`` executable to ``C:\Program Files\Git\cmd``

    * Check if Sqlite3 is installed (Point 1.)


SQL Syntax
==========
* For SQL Syntax refer to :ref:`Database SQL`

Data Types
----------
.. csv-table:: SQLite basic data types
    :widths: 10, 10, 80
    :header:  "SQLite Type", "Python Type", "Description"

    "``NULL``", "``None``", "The value is a undefined value"
    "``INTEGER``", "``int``", "The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value"
    "``REAL``", "``float``", "The value is a floating point value, stored as an 8-byte IEEE floating point number"
    "``TEXT``", "``str``", "The value is a text string, stored using the database encoding (ie. UTF-8)"
    "``BLOB``", "``bytes``", "The value is a blob of data, stored exactly as it was input"

.. csv-table:: SQLite extra data types
    :widths: 50, 50
    :header: "SQLite Type", "SQLite Alias"

    "``INTEGER``", "``INT``"
    "``INTEGER``", "``INTEGER``"
    "``INTEGER``", "``TINYINT``"
    "``INTEGER``", "``SMALLINT``"
    "``INTEGER``", "``MEDIUMINT``"
    "``INTEGER``", "``BIGINT``"
    "``INTEGER``", "``UNSIGNED BIG INT``"
    "``INTEGER``", "``INT2``"
    "``INTEGER``", "``INT8``"

    "``TEXT``", "``CHARACTER(20)``"
    "``TEXT``", "``VARCHAR(255)``"
    "``TEXT``", "``VARYING CHARACTER(255)``"
    "``TEXT``", "``NCHAR(55)``"
    "``TEXT``", "``NATIVE CHARACTER(70)``"
    "``TEXT``", "``NVARCHAR(100)``"
    "``TEXT``", "``TEXT``"
    "``TEXT``", "``CLOB``"

    "``REAL``", "``REAL``"
    "``REAL``", "``DOUBLE``"
    "``REAL``", "``DOUBLE PRECISION``"
    "``REAL``", "``FLOAT``"

    "``NUMERIC``", "``NUMERIC``"
    "``NUMERIC``", "``DECIMAL(10,5)``"
    "``NUMERIC``", "``BOOLEAN``"
    "``NUMERIC``", "``DATE``"
    "``NUMERIC``", "``DATETIME``"

Numeric
-------
A column with ``NUMERIC`` affinity may contain values using all five storage classes. When text data is inserted into a ``NUMERIC`` column, the storage class of the text is converted to INTEGER or REAL (in order of preference) if the text is a well-formed integer or real literal, respectively. If the TEXT value is a well-formed integer literal that is too large to fit in a 64-bit signed integer, it is converted to REAL.

Datetime
--------
SQLite does not have a storage class set aside for storing dates and/or times. Instead, the built-in Date And Time Functions of SQLite are capable of storing dates and times as TEXT, REAL, or INTEGER values:

* ``TEXT`` as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
* ``REAL`` as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the Gregorian calendar.
* ``INTEGER`` as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC.

Applications can chose to store dates and times in any of these formats and freely convert between formats using the built-in date and time functions.

Constrains
----------
.. csv-table:: SQL Constraints
    :header:  "Constraint", "Description"
    :widths: 15, 85

    "``NOT NULL``", "Ensures that a column cannot have a ``NULL`` value"
    "``UNIQUE``", "Ensures that all values in a column are different"
    "``PRIMARY KEY``", "A combination of a ``NOT NULL`` and ``UNIQUE``. Uniquely identifies each row in a table"
    "``FOREIGN KEY``", "Uniquely identifies a row/record in another table"
    "``CHECK``", "Ensures that all values in a column satisfies a specific condition"
    "``DEFAULT``", "Sets a default value for a column when no value is specified"
    "``INDEX``", "Used to create and retrieve data from the database very quickly"

DB API v2
=========
.. code-block:: python

    sqlite3.connect(...) -> connection

    connection.execute(...) -> result
    connection.executemany(...) -> list[result]
    connection.fetchmany(...) -> list[result]
    connection.fetchone(...) -> result
    connection.cursor(...) -> cursor
    connection.commit(...)
    connection.close()


Connection
==========
Connection to in-memory database:

.. code-block:: python

    import sqlite3

    DATABASE = ':memory:'

    with sqlite3.connect(DATABASE) as db:
        ...

Connection to database file:

.. code-block:: python

    import sqlite3

    DATABASE = r'/tmp/database.sqlite3'

    with sqlite3.connect(DATABASE) as db:
        ...


Execute
=======
Execute:

.. code-block:: python

    import sqlite3


    DATABASE = ':memory:'

    SQL_CREATE_TABLE = """
        CREATE TABLE IF NOT EXISTS astronauts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesel INTEGER UNIQUE,
            firstname TEXT,
            lastname TEXT)"""

    SQL_INSERT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :firstname, :lastname)'

    DATA = {'pesel': '61041212345',
            'firstname': 'Mark',
            'lastname': 'Watney'}


    with sqlite3.connect(DATABASE) as db:
        db.execute(SQL_CREATE_TABLE)


Executemany
===========

``list[tuple]``
---------------
.. literalinclude:: src/database-executemany-tuple.py
    :language: python
    :caption: Execute many

``list[dict]``
--------------
.. literalinclude:: src/database-executemany-dict.py
    :language: python
    :caption: Execute many


Results
=======

Fetch as ``list[tuple]``
------------------------
.. literalinclude:: src/database-results.py
    :language: python
    :caption: Results

Fetch as ``list[dict]``
-----------------------
.. literalinclude:: src/database-results-dict.py
    :language: python
    :caption: Results with ``dict``


Cursor
======
.. literalinclude:: src/database-cursor.py
    :language: python
    :caption: Results with cursor


Use cases
=========
.. literalinclude:: src/database-case-study.py
    :name: listing-database-case-study
    :language: python
    :caption: Zapisywanie do bazy danych wyników pobranych z sensorów podłączonych po USB


Assignments
===========
.. literalinclude:: assignments/database_sqlite_logs.py
    :caption: :download:`Solution <assignments/database_sqlite_logs.py>`
    :end-before: # Solution

.. literalinclude:: assignments/database_sqlite_csv.py
    :caption: :download:`Solution <assignments/database_sqlite_csv.py>`
    :end-before: # Solution

.. literalinclude:: assignments/database_sqlite_relations.py
    :caption: :download:`Solution <assignments/database_sqlite_relations.py>`
    :end-before: # Solution
