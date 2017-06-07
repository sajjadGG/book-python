***********
Bazy Danych
***********

``sqlite3``
===========

Połączenie
----------

.. code-block:: python

    import sqlite3
    conn = sqlite3.connect('example.db')

Cursor
------
.. code-block:: python

    cur = conn.cursor()

    # Create table
    cur.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    # And this is the named style:
    cur.execute("select * from stocks where trans=:trans and symbol=:symbol", {"symbol": 'RHAT', "trans": 'BUY'})

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


Execute Many
------------

.. code-block:: python

    # Never do this -- insecure!
    symbol = 'RHAT'
    c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

    # Do this instead
    t = ('RHAT',)
    c.execute('SELECT * FROM stocks WHERE symbol=?', t)
    print c.fetchone()

    # Larger example that inserts many records at a time
    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

Wyniki
------

.. code-block:: python

    for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

    (u'2006-01-05', u'BUY', u'RHAT', 100, 35.14)
    (u'2006-03-28', u'BUY', u'IBM', 1000, 45.0)
    (u'2006-04-06', u'SELL', u'IBM', 500, 53.0)
    (u'2006-04-05', u'BUY', u'MSFT', 1000, 72.0)

.. code-block:: python

    import sqlite3

    con = sqlite3.connect(":memory:")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select 'John' as name, 42 as age")

    for row in cur:
        assert row[0] == row["name"]
        assert row["name"] == row["nAmE"]
        assert row[1] == row["age"]
        assert row[1] == row["AgE"]


Typy i konwertery
-----------------

.. code-block:: python

    import sqlite3
    import datetime

    con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
    cur = con.cursor()
    cur.execute("create table test(d date, ts timestamp)")

    today = datetime.date.today()
    now = datetime.datetime.now()

    cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
    cur.execute("select d, ts from test")
    row = cur.fetchone()
    print(today, "=>", row[0], type(row[0]))
    print(now, "=>", row[1], type(row[1]))

    cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
    row = cur.fetchone()
    print("current_date", row[0], type(row[0]))
    print("current_timestamp", row[1], type(row[1]))

Context manager
---------------

.. code-block:: python

    import sqlite3

    con = sqlite3.connect(":memory:")
    con.execute("create table person (id integer primary key, firstname varchar unique)")

    # Successful, con.commit() is called automatically afterwards
    with con:
        con.execute("insert into person(firstname) values (?)", ("Joe",))

    # con.rollback() is called after the with block finishes with an exception, the
    # exception is still raised and must be caught
    try:
        with con:
            con.execute("insert into person(firstname) values (?)", ("Joe",))
    except sqlite3.IntegrityError:
        print("couldn't add Joe twice")


``pyMySQL``
===========

.. code-block:: console

    $ pip install PyMySQL

.. code-block:: sql

    CREATE TABLE `users` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `email` varchar(255) COLLATE utf8_bin NOT NULL,
        `password` varchar(255) COLLATE utf8_bin NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
    AUTO_INCREMENT=1 ;

.. code-block:: python

    import pymysql.cursors

    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='user',
                                 password='passwd',
                                 db='db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()


``psycopg2``
============

* http://initd.org/psycopg/
* http://initd.org/psycopg/docs/usage.html

.. code-block:: console

    $ pip install psycopg2

.. code-block:: python

    >>> import psycopg2

    # Connect to an existing database
    >>> conn = psycopg2.connect("dbname=test user=postgres")

    # Open a cursor to perform database operations
    >>> cur = conn.cursor()

    # Execute a command: this creates a new table
    >>> cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    >>> cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
    ...      (100, "abc'def"))

    # Query the database and obtain data as Python objects
    >>> cur.execute("SELECT * FROM test;")
    >>> cur.fetchone()
    (1, 100, "abc'def")

    # Make the changes to the database persistent
    >>> conn.commit()

    # Close communication with the database
    >>> cur.close()
    >>> conn.close()

.. code-block:: python

    conn = psycopg2.connect(DSN)

    with conn:
        with conn.cursor() as curs:
            curs.execute(SQL1)

    with conn:
        with conn.cursor() as curs:
            curs.execute(SQL2)

    conn.close()


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
Skrypt z książką adresową z poprzednich zadań przepisz tak, aby wykorzystywał bazę danych do składowania informacji.

Bardziej zaawansowane operacje na bazie
---------------------------------------
Skrypt z książką adresową z poprzednich zadań przepisz tak, aby wykorzystywał bazę danych do składowania informacji:

* Wykorzystaj ``cursor``
* Dane powinny być zwracane dane w postaci listy ``dict``
* Do wpisywania danych wykorzystaj konstrukcję ``PreparedStatement`` wykorzystując ``dict`` jako argument
