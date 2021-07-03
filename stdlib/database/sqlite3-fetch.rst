SQLite3 Fetch
=============


Fetch Sequences
---------------
>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> SQL_CREATE_TABLE = """
...     CREATE TABLE IF NOT EXISTS astronauts (
...         id INTEGER PRIMARY KEY AUTOINCREMENT,
...         firstname TEXT,
...         lastname TEXT)"""
>>>
>>> SQL_INSERT = """
...     INSERT INTO astronauts
...     VALUES (NULL, ?, ?)"""
>>>
>>> SQL_SELECT = """
...     SELECT *
...     FROM astronauts"""
>>>
>>> data = [{'firstname': 'Mark', 'lastname': 'Watney'},
...         {'firstname': 'Melissa', 'lastname': 'Lewis'},
...         {'firstname': 'Rick', 'lastname': 'Martinez'},
...         {'firstname': 'Alex', 'lastname': 'Vogel'},
...         {'firstname': 'Beth', 'lastname': 'Johansen'},
...         {'firstname': 'Chris', 'lastname': 'Beck'}]
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     db.execute(SQL_CREATE_TABLE)
...     db.executemany(SQL_INSERT, data)
...     for row in db.execute(SQL_SELECT):
...         print(row)
(1, 'Mark', 'Watney')
(2, 'Melissa', 'Lewis')
(3, 'Rick', 'Martinez')
(4, 'Alex', 'Vogel')
(5, 'Beth', 'Johansen')
(6, 'Chris', 'Beck')


Fetch Mappings
--------------
>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> SQL_CREATE_TABLE = """
...     CREATE TABLE IF NOT EXISTS astronauts (
...         id INTEGER PRIMARY KEY AUTOINCREMENT,
...         firstname TEXT,
...         lastname TEXT)"""
>>>
>>> SQL_INSERT = """
...     INSERT INTO astronauts
...     VALUES (NULL, ?, ?)"""
>>>
>>> SQL_SELECT = """
...     SELECT *
...     FROM astronauts"""
>>>
>>> data = [{'firstname': 'Mark', 'lastname': 'Watney'},
...         {'firstname': 'Melissa', 'lastname': 'Lewis'},
...         {'firstname': 'Rick', 'lastname': 'Martinez'},
...         {'firstname': 'Alex', 'lastname': 'Vogel'},
...         {'firstname': 'Beth', 'lastname': 'Johansen'},
...         {'firstname': 'Chris', 'lastname': 'Beck'}]
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     cursor = db.cursor()
...     cursor.execute(SQL_CREATE_TABLE)
...     cursor.executemany(SQL_INSERT, data)
...     for row in cursor.execute(SQL_SELECT):
...         print(row)
{'id': 1, 'firstname': 'Mark', 'lastname': 'Watney'}
{'id': 2, 'firstname': 'Melissa', 'lastname': 'Lewis'}
{'id': 3, 'firstname': 'Rick', 'lastname': 'Martinez'}
{'id': 4, 'firstname': 'Alex', 'lastname': 'Vogel'}
{'id': 5, 'firstname': 'Beth', 'lastname': 'Johansen'}
{'id': 6, 'firstname': 'Chris', 'lastname': 'Beck'}


Assignments
-----------
.. literalinclude:: assignments/sqlite3_fetch_a.py
    :caption: :download:`Solution <assignments/sqlite3_fetch_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/sqlite3_fetch_b.py
    :caption: :download:`Solution <assignments/sqlite3_fetch_b.py>`
    :end-before: # Solution
