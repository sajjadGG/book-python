***********
Bazy Danych
***********

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
.. literalinclude:: src/db-auto-increment.py
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

    $ python -m pip install pymongo

.. code-block:: python

    >>> from pymongo import MongoClient

    >>> client = MongoClient('mongodb://localhost:27017/')
    >>> db = client.test_database

    >>> import datetime
    >>> post = {"author": "Mike",
    ...         "text": "My first blog post!",
    ...         "tags": ["mongodb", "python", "pymongo"],
    ...         "date": datetime.datetime.utcnow()}

    >>> posts = db.posts
    >>> post_id = posts.insert_one(post).inserted_id
    >>> post_id
    ObjectId('...')

.. code-block:: python

    >>> for post in posts.find():
    ...   pprint.pprint(post)

    >>> for post in posts.find({"author": "Mike"}):
    ...   pprint.pprint(post)

``SQLAlchemy``
==============


Zadania kontrolne
=================

Tworzenie bazy danych i proste zapytania
----------------------------------------
Skrypt z książką adresową z poprzednich zadań przepisz tak, aby wykorzystywał bazę danych do składowania informacji:

* Nie wykorzystuj relacji, a dane adresowe zapisz zserializowane i rozdzielone średnikami ``;``
* dla ułatwienia możesz przyjąć, że zawsze jest maks jeden adres
* Wykorzystaj ``cursor``
* Dane powinny być zwracane dane w postaci listy ``dict``
* Do wpisywania danych wykorzystaj konstrukcję ``execute`` wykorzystując ``dict`` jako argument

:Zadanie z gwiazdką:
    * Dodaj obsługę wielu adresów
    * Dodaj obsługę relacji w aplikacji

:Podpowiedź:
    .. literalinclude:: src/db-ksiazka-adresowa.py
        :language: python
        :caption: Ksiazka Adresowa zapytania SQL