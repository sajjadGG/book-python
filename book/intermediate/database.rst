***********
Bazy Danych
***********

SQL
===

CREATE
------
.. literalinclude:: src/db-sql-create.sql
    :language: sql
    :caption: CREATE

Constrains
----------
* NOT NULL - Ensures that a column cannot have a NULL value
* UNIQUE - Ensures that all values in a column are different
* PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
* FOREIGN KEY - Uniquely identifies a row/record in another table
* CHECK - Ensures that all values in a column satisfies a specific condition
* DEFAULT - Sets a default value for a column when no value is specified
* INDEX - Used to create and retrieve data from the database very quickly

INSERT
------
.. literalinclude:: src/db-sql-insert.sql
    :language: sql
    :caption: INSERT

SELECT
------
.. literalinclude:: src/db-sql-select.sql
    :language: sql
    :caption: SELECT

.. literalinclude:: src/db-sql-injection.py
    :language: python
    :caption: SQL Injection

UPDATE
------
.. literalinclude:: src/db-sql-update.sql
    :language: sql
    :caption: UPDATE

GROUP
-----
.. literalinclude:: src/db-sql-group.sql
    :language: sql
    :caption: GROUP

HAVING
------
.. literalinclude:: src/db-sql-having.sql
    :language: sql
    :caption: HAVING

ALTER
-----
.. literalinclude:: src/db-sql-alter.sql
    :language: sql
    :caption: ALTER

DROP
----
* https://www.youtube.com/watch?v=1aEqd4bl6Bs
* prepare your statement starting with '--'

.. literalinclude:: src/db-sql-drop.sql
    :language: sql
    :caption: DROP

DELETE
------
.. literalinclude:: src/db-sql-delete.sql
    :language: sql
    :caption: DELETE

JOIN
----
.. figure:: img/db-sql-innerjoin.gif
    :align: center
    :scale: 100%

.. figure:: img/db-sql-leftjoin.gif
    :align: center
    :scale: 100%

.. figure:: img/db-sql-rightjoin.gif
    :align: center
    :scale: 100%

.. figure:: img/db-sql-fulljoin.gif
    :align: center
    :scale: 100%

.. literalinclude:: src/db-sql-join.sql
    :language: sql
    :caption: JOIN

TRUNCATE
--------
.. literalinclude:: src/db-sql-truncate.sql
    :language: sql
    :caption: TRUNCATE

``sqlite3``
===========

Typy danych w SQLite
--------------------
- NULL. The value is a NULL value.
- INTEGER. The value is a signed integer, stored in 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.
- REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.
- TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).
- BLOB. The value is a blob of data, stored exactly as it was input.

SQLite Auto Increment
---------------------
.. literalinclude:: src/db-auto-increment.sql
    :language: sql
    :caption: Auto Increment

Połączenie
----------
.. literalinclude:: src/db-connect.py
    :language: python
    :caption: Connection

Context manager
---------------
.. literalinclude:: src/db-context-manager.py
    :language: python
    :caption: Context Manager

Cursor
------
.. literalinclude:: src/db-cursor.py
    :language: python
    :caption: Cursor

Execute Many
------------
.. literalinclude:: src/db-execute-many.py
    :language: python
    :caption: Execute many

Wyniki
------
.. literalinclude:: src/db-results.py
    :language: python
    :caption: Results

Typy i konwertery
-----------------
.. literalinclude:: src/db-converters.py
    :language: python
    :caption: Converters


Przykład praktyczny
===================
.. literalinclude:: src/database-case-study.py
    :name: listing-database-case-study
    :language: python
    :caption: Zapisywanie do bazy danych wyników pobranych z sensorów podłączonych po USB


``pyMySQL``
===========
.. code-block:: console

    $ pip install PyMySQL

.. literalinclude:: src/db-pymysql.sql
    :language: python
    :caption: PyMySQL

.. literalinclude:: src/db-pymysql.py
    :language: python
    :caption: PyMySQL


``psycopg2``
============

* http://initd.org/psycopg/
* http://initd.org/psycopg/docs/usage.html

.. code-block:: console

    $ pip install psycopg2


.. literalinclude:: src/db-psycopg2.py
    :language: python
    :caption: Psycopg2


``pymongo``
===========
* http://api.mongodb.com/python/current/tutorial.html

.. code-block:: console

    $ pip install pymongo

.. code-block:: python

    import datetime
    from pymongo import MongoClient

    client = MongoClient('mongodb://localhost:27017/')
    db = client.test_database
    posts = db.posts

    data = {
        "name": "José Jiménez",
        "catchphrase": "My name José Jiménez",
        "tags": ["astronaut", "nasa", "space"],
        "date": datetime.datetime.utcnow()
    }

    posts.insert_one(data).inserted_id
    # ObjectId('...')

.. code-block:: python

    for post in posts.find():
        print(post)

    for post in posts.find({"author": "Mike"}):
        print(post)

``SQLAlchemy``
==============

``Django ORM``
==============


Data exploration
================
* https://superset.incubator.apache.org/

.. code-block:: console

    # Install superset
    pip install superset

    # Create an admin user (you will be prompted to set username, first and last name before setting a password)
    fabmanager create-admin --app superset

    # Initialize the database
    superset db upgrade

    # Load some data to play with
    superset load_examples

    # Create default roles and permissions
    superset init

    # Start the web server on port 8088, use -p to bind to another port
    superset runserver

    # To start a development web server, use the -d switch
    # superset runserver -d

:superset_config.py:
    .. code-block:: python

        import os

        #---------------------------------------------------------
        # Superset specific config
        #---------------------------------------------------------
        ROW_LIMIT = 5000
        SUPERSET_WORKERS = 4

        SUPERSET_WEBSERVER_PORT = 8088
        #---------------------------------------------------------

        #---------------------------------------------------------
        # Flask App Builder configuration
        #---------------------------------------------------------
        # Your App secret key
        SECRET_KEY = '\2\1secretkey\1\2\e\y\y\h'

        # The SQLAlchemy connection string to your database backend
        # This connection defines the path to the database that stores your
        # superset metadata (slices, connections, tables, dashboards, ...).
        # Note that the connection information to connect to the datasources
        #you want to explore are managed directly in the web UI
        SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_GREEN_URL', None)

        # Flask-WTF flag for CSRF
        WTF_CSRF_ENABLED = True
        # Add endpoints that need to be exempt from CSRF protection
        WTF_CSRF_EXEMPT_LIST = []

        # Set this API key to enable Mapbox visualizations
        MAPBOX_API_KEY = ''


.. code-block:: console

    gunicorn \
        -w 10 \
        -k gevent \
        --timeout 120 \
        -b  0.0.0.0:6666 \
        --limit-request-line 0 \
        --limit-request-field_size 0 \
        --statsd-host localhost:8125 \
        superset:app


Zadania kontrolne
=================

Tworzenie bazy danych i proste zapytania (simple)
-------------------------------------------------
* Wykorzystaj kod z listingu :numref:``
* Nie wykorzystuj relacji, a dane adresowe zapisz zserializowane i rozdzielone średnikami ``;``
* dla ułatwienia możesz przyjąć, że zawsze jest maks jeden adres
* Wykorzystaj ``cursor``
* Dane powinny być zwracane dane w postaci listy ``dict``
* Do wpisywania danych wykorzystaj konstrukcję ``execute`` wykorzystując ``dict`` jako argument

:Założenia:
    * Nazwa pliku: ``db-simple.py``
    * Linii kodu do napisania: około 15 linii
    * Maksymalny czas na zadanie: 20 min

:Zadanie z gwiazdką:
    * Dodaj obsługę wielu adresów
    * Dodaj obsługę relacji w aplikacji

:Podpowiedź:
    .. literalinclude:: src/db-assignment-addressbook.sql
        :language: python
        :caption: Address Book SQL queries

.. literalinclude:: src/db-assignment-addressbook.py
    :language: python
    :caption: Address Book

Tworzenie bazy danych
---------------------
* https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/iris.csv

#. bazę danych Irysów przekonwertuj na tabelę w sqlite3
#. Nazwy poszczególnych kolumn:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

:Założenia:
    * Nazwa pliku: ``db-iris.py``
    * Linii kodu do napisania: około 10 linii
    * Maksymalny czas na zadanie: 20 min