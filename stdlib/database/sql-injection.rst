**********************
Database SQL Injection
**********************


Prepare query
=============
Query with SQL injection possibility:

.. code-block:: python

    SQL_QUERY = f"""

        SELECT id, username, email
        FROM users
        WHERE username='{username}' AND password='{password}'

    """

Get user input
==============
.. code-block:: python

    username = input('Username: ')
    # ' OR 1=1; DROP TABLE users --

    password = input('Password: ')
    # 123

Execute query
=============
Exploited SQL injection, will Select all users and then Drop all data from table users:

.. code-block:: python

    print(query)
    # SELECT id, username, email
    # FROM users
    # WHERE username='' OR 1=1; DROP TABLE users -- ' AND password='132'

.. figure:: img/sql-injection.jpg

    SQL Injection
