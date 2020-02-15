***************
Database SQLite
***************



SQL Syntax
==========
.. note:: For SQL Syntax refer to :ref:`Database SQL`

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
* Solution: :download:`solution/sqlite_iris.py`

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
    #. Stwórz tabelę ``iris`` o kolumnach podanych w sekcji dane wyjściowe (patrz sekcja output)
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
* Solution: :download:`solution/sqlite_addressbook.py`

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

Log parsing
-----------
* Complexity level: medium
* Lines of code to write: 25 lines
* Estimated time of completion: 20 min
* Solution: :download:`solution/sqlite_logs.py`

:English:
    #. Save input data to file ``apollo11-timeline.log``
    #. Extract ``datetime`` object, level name and message from each line
    #. Collect data to ``INPUT: List[dict]`` (see below)
    #. Create database schema for logs
    #. Add all logs to database
    #. Select only ``WARNING`` logs between 1969-07-20 and 1969-07-21
    #. Order logs by datetime descending
    #. Print ``OUTPUT: List[dict]``

:Polish:
    #. Zapisz dane wejściowe do pliku ``apollo11-timeline.log``
    #. Wyciągnij obiekt ``datetime``, poziom logowania oraz wiadomość z każdej linii
    #. Zbierz dane do ``INPUT: List[dict]`` (patrz sekcja input)
    #. Stwórz schemat bazy danych dla logów
    #. Dodaj wszystkie linie do bazy danych
    #. Wybierz tylko logi ``WARNING`` z przedziału 1969-07-20 i 1969-07-21
    #. Posortuj logi w kolejności datetime malejąco
    #. Wyświetl ``OUTPUT: List[dict]``

:Input:
    .. code-block:: text
        :caption: Apollo 11 timeline https://history.nasa.gov/SP-4029/Apollo_11i_Timeline.htm

        1969-07-14T21:00:00 [INFO] Terminal countdown started
        1969-07-16T13:31:53 [WARNING] S-IC engine ignition (#5)
        1969-07-16T13:33:23 [DEBUG] Maximum dynamic pressure (735.17 lb/ft^2)
        1969-07-16T13:34:44 [WARNING] S-II ignition
        1969-07-16T13:35:17 [DEBUG] Launch escape tower jettisoned
        1969-07-16T13:39:40 [DEBUG] S-II center engine cutoff
        1969-07-16T16:22:13 [INFO] Translunar injection
        1969-07-16T16:56:03 [INFO] CSM docked with LM/S-IVB
        1969-07-16T17:21:50 [INFO] Lunar orbit insertion ignition
        1969-07-16T21:43:36 [INFO] Lunar orbit circularization ignition
        1969-07-20T17:44:00 [INFO] CSM/LM undocked
        1969-07-20T20:05:05 [WARNING] LM powered descent engine ignition
        1969-07-20T20:10:22 [ERROR] LM 1202 alarm
        1969-07-20T20:14:18 [ERROR] LM 1201 alarm
        1969-07-20T20:17:39 [WARNING] LM lunar landing
        1969-07-21T02:39:33 [DEBUG] EVA started (hatch open)
        1969-07-21T02:56:15 [WARNING] 1st step taken lunar surface (CDR) "That's one small step for [a] man... one giant leap for mankind"
        1969-07-21T03:05:58 [DEBUG] Contingency sample collection started (CDR)
        1969-07-21T03:15:16 [INFO] LMP on lunar surface
        1969-07-21T05:11:13 [DEBUG] EVA ended (hatch closed)
        1969-07-21T17:54:00 [WARNING] LM lunar liftoff ignition (LM APS)
        1969-07-21T21:35:00 [INFO] CSM/LM docked
        1969-07-22T04:55:42 [WARNING] Transearth injection ignition (SPS)
        1969-07-24T16:21:12 [INFO] CM/SM separation
        1969-07-24T16:35:05 [WARNING] Entry
        1969-07-24T16:50:35 [WARNING] Splashdown (went to apex-down)
        1969-07-24T17:29 [INFO] Crew egress

:Output:
    .. code-block:: python

        OUTPUT: List[dict] = [

            {'date': datetime.datetime(1969, 7, 21, 17, 54, 00, tzinfo=datetime.timezone.utc),
             'level': 'WARNING',
             'message': 'LM lunar liftoff ignition (LM APS)'},

            {'date': datetime.datetime(1969, 7, 21, 2, 56, 15, tzinfo=datetime.timezone.utc),
             'level': 'WARNING',
             'message': '1st step taken lunar surface (CDR) "That\'s one small step for [a] man... one giant leap for mankind"'},

            {'date': datetime.datetime(1969, 7, 20, 20, 17, 39, tzinfo=datetime.timezone.utc),
             'level': 'WARNING',
             'message': 'LM lunar landing'},

        ...]
