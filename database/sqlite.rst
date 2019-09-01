******
SQLite
******



SQL Syntax
==========
.. note:: For SQL Syntax refer to :ref:`SQL`

Data Types
----------
.. csv-table:: SQLite data types
    :header-rows: 1
    :file: data/sql-types.csv

Constrains
----------
.. csv-table:: SQL Constraints
    :header-rows: 1
    :file: data/sql-constraints.csv


Connection
==========
.. literalinclude:: src/database-connect-memory.py
    :language: python
    :caption: Connection to in-memory database

.. literalinclude:: src/database-connect-file.py
    :language: python
    :caption: Connection to database file


Execute
=======
.. literalinclude:: src/database-execute.py
    :language: python
    :caption: Execute


Executemany
===========

``List[tuple]``
---------------
.. literalinclude:: src/database-executemany-tuple.py
    :language: python
    :caption: Execute many

``List[dict]``
--------------
.. literalinclude:: src/database-executemany-dict.py
    :language: python
    :caption: Execute many


Results
=======

Fetch as ``List[tuple]``
------------------------
.. literalinclude:: src/database-results.py
    :language: python
    :caption: Results

Fetch as ``List[dict]``
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

SQLite Iris
-----------
* Complexity level: easy
* Lines of code to write: 30 lines
* Estimated time of completion: 30 min
* Filename: :download:`solution/sqlite_iris.py`

:English:
    #. Save input data as ``sqlite_iris.csv`` file
    #. Read data from file
    #. Create ``species: Dict[int, str]`` with structure:

        * 0 - setosa
        * 1 - versicolor
        * 2 - virginica

    #. Save data to ``sqlite3`` database table
    #. Replace ``int`` to ``str`` according to ``species`` conversion table
    #. Column names:

        * id - ``int``
        * species - ``str``
        * datetime - ``datetime``
        * sepal_length - ``float``
        * sepal_width - ``float``
        * petal_length - ``float``
        * petal_width - ``float``

    #. Print results using ``SELECT * FROM iris ORDER BY datetime DESC``

:Polish:
    #. Zapisz dane wejściowe do pliku ``sqlite_iris.csv``
    #. Wczytaj dane z pliku
    #. Stwórz ``species: Dict[int, str]`` o strukturze:

        * 0 - setosa
        * 1 - versicolor
        * 2 - virginica

    #. Podmień ``int`` na ``str`` zgodnie z tabelą podstawień ``species``
    #. Zapisz dane do tabeli w bazie danych ``sqlite3``
    #. Nazwy kolumn:

        * id - ``int``
        * species - ``str``
        * datetime - ``datetime``
        * sepal_length - ``float``
        * sepal_width - ``float``
        * petal_length - ``float``
        * petal_width - ``float``

    #. Wyniki wypisz z bazy danych ``SELECT * FROM iris ORDER BY datetime DESC``

:Non functional requirements:
    * Use context manager (``with``) for connection
    * Return data as ``sqlite3.Row``
    * Add data in ``dict`` format using ``.executemany()``
    * Save date and time to database in UTC

:Extra task:
    * Create index on ``datetime`` column
    * Use cursor

:The whys and wherefores:
    * Parsing ``csv`` files
    * Using ``sqlite3`` database
    * Creating database
    * Inserting data to database
    * Selecting data from database
    * Type casting
    * Using ``datetime`` and UTC timezone
    * Creating indexes (extra task)

:Input:
    .. literalinclude:: assignment/database-iris.csv
        :language: python
        :caption: Input

Creating relations in database
------------------------------
* Complexity level: medium
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/sqlite_addressbook.py`

:English:
    #. Create database for input data
    #. Add support for many addresses
    #. Insert data to database
    #. Select data from database using JOIN relations

:Polish:
    #. Stwórz bazę danych na podstawie danych wejściowych
    #. Dodaj obsługę dla wielu adresów
    #. Zapisz dane do bazy
    #. Wypisz dane z bazy wykorzystując relację JOIN

:Input:
    .. literalinclude:: assignment/database-addressbook.txt
        :language: text
        :caption: Input

:Hint:
    .. literalinclude:: assignment/database-addressbook.sql]
        :language: sql
        :caption: Hint

Relational data in one table
----------------------------
* Complexity level: easy
* Lines of code to write: 0 lines
* Estimated time of completion: 15 min

:English:
    #. How to write input data in one table without using relations?
    #. There are at least four methods
    #. Discuss pros and cons of each method
    #. Which methods is ACID compliant?

:Polish:
    #. Jak zapisać w jednej tabeli bez wykorzystania relacji?
    #. Są przynajmniej cztery metody
    #. Przeprowadź dyskusję na temat zalet i wad każdej metody
    #. Która metody jest zgodna z ACID?

:Input:
    .. literalinclude:: assignment/database-addressbook.txt
        :language: text
        :caption: Input
