Database PostgreSQL
===================


Rationale
---------
* ``psycopg2``


Install
-------
.. code-block:: console

    $ pip install psycopg2

Execute
-------
.. code-block:: python

    import psycopg2

    # Connect to an existing database
    conn = psycopg2.connect('dbname=test user=postgres')

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute('CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);')

    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

    # Query the database and obtain data as Python objects
    cur.execute('SELECT * FROM test')
    cur.fetchone()
    # (1, 100, "abc'def")

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()


Further Reading
---------------
* http://initd.org/psycopg/
* http://initd.org/psycopg/docs/usage.html
