Database Insert Mappings
========================


SQL Syntax
----------
.. code-block:: sql

    INSERT INTO astronauts
    VALUES ("Mark", "Watney");

    INSERT INTO astronauts (firstname, lastname)
    VALUES ("Mark", "Watney");

    INSERT INTO astronauts (id, firstname, lastname)
    VALUES (NULL, "Mark", "Watney");

.. code-block:: sql

    INSERT INTO astronauts (firstname, lastname) VALUES (?, ?);
    INSERT INTO astronauts VALUES (NULL, :firstname, :lastname);


Execute
-------
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

    DATA = {'pesel': '61041200001',
            'firstname': 'Mark',
            'lastname': 'Watney'}


    with sqlite3.connect(DATABASE) as db:
        db.execute(SQL_CREATE_TABLE)


Executemany ``list[tuple]``
---------------------------
.. literalinclude:: src/database-executemany-tuple.py
    :language: python
    :caption: Execute many


Execute many ``list[dict]``
---------------------------
.. literalinclude:: src/database-executemany-dict.py
    :language: python
    :caption: Execute many



Assignments
-----------
.. literalinclude:: assignments/database_sqlite_a.py
    :caption: :download:`Solution <assignments/database_sqlite_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/database_sqlite_b.py
    :caption: :download:`Solution <assignments/database_sqlite_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/database_sqlite_c.py
    :caption: :download:`Solution <assignments/database_sqlite_c.py>`
    :end-before: # Solution
