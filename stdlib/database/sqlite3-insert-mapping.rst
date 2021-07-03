SQLite3 Insert Mapping
======================


Insert One
----------
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
>>>
>>> data = {'firstname': 'Mark',
...         'lastname': 'Watney'}]
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     cursor.execute(SQL_CREATE_TABLE)
...     cursor.executemany(SQL_INSERT, data)


Insert Many
-----------
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
...     cursor.execute(SQL_CREATE_TABLE)
...     cursor.executemany(SQL_INSERT, data)
