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

    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

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

``psycopg2``
===========

``pymongo``
===========

``SQLAlchemy``
==============


Zadania kontrolne
=================

Ksiażka adresowa
----------------

:Zadanie:
    Skrypt z książką adresową z poprzednich zadań przepisz tak, aby wykorzystywał bazę danych do składowania informacji.

Passwd
------

:Zadanie:
    Skrypt z książką adresową z poprzednich zadań przepisz tak, aby wykorzystywał bazę danych do składowania informacji:

        * Wykorzystaj ``cursor``
        * Dane powinny być zwracane dane w postaci listy ``dict``
        * Do wpisywania danych wykorzystaj konstrukcję ``prepare``
