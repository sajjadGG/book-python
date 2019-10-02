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
    #. Read data from file (don't use ``csv`` or ``pandas`` library)
    #. Connect to the ``sqlite3`` using context manager (``with``)
    #. Create table ``iris``, column names are specified in output data (see below)
    #. Replace ``int`` to ``str`` according to ``SPECIES`` conversion table (see input data)
    #. Save data to database table
    #. Print results using ``SELECT * FROM iris ORDER BY datetime DESC``

:Polish:
    #. Zapisz dane wejściowe do pliku ``sqlite_iris.csv``
    #. Wczytaj dane z pliku (nie używaj biblioteki ``csv`` lub ``pandas``)
    #. Połącz się do bazy danych ``sqlite3`` używając context managera (``with``)
    #. Stwórz tabelę ``iris`` o kolumnach podanych w sekcji dane wyjściowe (patrz poniżej)
    #. Podmień ``int`` na ``str`` zgodnie z tabelą podstawień ``SPECIES`` (patrz dane wejściowe)
    #. Zapisz dane do tabeli w bazie danych
    #. Wypisz wyniki z bazy danych ``SELECT * FROM iris ORDER BY datetime DESC``

:Non functional requirements:
    * Use context manager (``with``) for connection and for opening file
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
    .. code-block:: text

        4.3,3.0,1.1,0.1,0
        5.8,4.0,1.2,0.2,0
        5.7,4.4,1.5,0.4,1
        5.4,3.9,1.3,0.4,2
        5.1,3.5,1.4,0.3,1
        5.7,3.8,1.7,0.3,0
        5.1,3.8,1.5,0.3,0
        5.4,3.4,1.7,0.2,1
        5.1,3.7,1.5,0.4,0
        4.6,3.6,1.0,0.2,0
        5.1,3.3,1.7,0.5,2
        4.8,3.4,1.9,0.2,0
        5.0,3.0,1.6,0.2,1
        5.0,3.4,1.6,0.4,2
        5.2,3.5,1.5,0.2,1
        5.2,3.4,1.4,0.2,2
        4.7,3.2,1.6,0.2,0

    .. code-block:: python
        :caption: Input Species substitution ``dict``

        SPECIES = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica',
        }

    .. code-block:: sql

        CREATE TABLE IF NOT EXISTS iris (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            species TEXT,
            datetime DATETIME,
            sepal_length REAL,
            sepal_width REAL,
            petal_length REAL,
            petal_width REAL
        );

    .. code-block:: sql

        INSERT INTO iris VALUES (
            NULL,
            :species,
            :datetime,
            :sepal_length,
            :sepal_width,
            :petal_length,
            :petal_width
        );

    .. code-block:: sql

        SELECT * FROM iris ORDER BY datetime DESC

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
    .. code-block:: text

        José, Jiménez
            2101 E NASA Pkwy, 77058, Houston, Texas, USA
            , Kennedy Space Center, 32899, Florida, USA

        Mark, Watney
            4800 Oak Grove Dr, 91109, Pasadena, California, USA
            2825 E Ave P, 93550, Palmdale, California, USA

        Иван, Иванович
            Kosmodrom Bajkonur, Bajkonur, Kazachstan

        Melissa Lewis,
            <NO ADDRESS>

        Alex Vogel
            Linder Hoehe, 51147, Köln, Germany

:Hint:
    .. code-block:: sql
        :caption: Hint

        CREATE TABLE IF NOT EXISTS contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created DATETIME,
            modified DATETIME,
            first_name TEXT,
            last_name TEXT,
            date_of_birth DATE
        );

        CREATE UNIQUE INDEX IF NOT EXISTS last_name_index ON contact (last_name);
        CREATE INDEX IF NOT EXISTS modified_index ON contact (modified);

        CREATE TABLE IF NOT EXISTS address (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contact_id INTEGER,
            street TEXT,
            city TEXT,
            state TEXT,
            code INT,
            country TEXT
        );

        INSERT INTO contact VALUES (
            NULL,
            :created,
            :modified,
            :first_name,
            :last_name,
            :date_of_birth
        );

        INSERT INTO address VALUES (
            NULL,
            :contact_id
            :street,
            :city,
            :state,
            :code,
            :country
        );

        UPDATE contact SET
            first_name=:firstname,
            last_name=:lastname,
            modified=:modified
        WHERE id=:id;

        SELECT * FROM contact;

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
    .. code-block:: text

        José, Jiménez
            2101 E NASA Pkwy, 77058, Houston, Texas, USA
            , Kennedy Space Center, 32899, Florida, USA

        Mark, Watney
            4800 Oak Grove Dr, 91109, Pasadena, California, USA
            2825 E Ave P, 93550, Palmdale, California, USA

        Иван, Иванович
            Kosmodrom Bajkonur, Bajkonur, Kazachstan

        Melissa Lewis,
            <NO ADDRESS>

        Alex Vogel
            Linder Hoehe, 51147, Köln, Germany
