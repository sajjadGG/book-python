SQLite3 Insert Sequence
=======================


Unique
------
>>> import sqlite3
>>>
>>>
>>> DATABASE = ':memory:'
>>>
>>> SQL_CREATE_TABLE = """
...     CREATE TABLE IF NOT EXISTS astronauts (
...         id INTEGER PRIMARY KEY AUTOINCREMENT,
...         login INTEGER UNIQUE,
...         firstname TEXT,
...         lastname TEXT)"""
>>>
>>> SQL_INSERT = """
...     INSERT INTO astronauts
...     VALUES (NULL, :login, :firstname, :lastname)"""
>>>
>>> SQL_SELECT = """
...     SELECT *
...     FROM astronauts"""
>>>
>>> data = [
...     {'login': 'mwatney', 'firstname': 'Mark', 'lastname': 'Watney'},
...     {'login': 'mwatney', 'firstname': 'Melissa', 'lastname': 'Lewis'}]
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     cursor.execute(SQL_CREATE_TABLE)
...     try:
...         db.executemany(SQL_INSERT, data)
...     except sqlite3.IntegrityError:
...         print('Login need to be UNIQUE')
Traceback (most recent call last):
sqlite3.IntegrityError: UNIQUE constraint failed: astronauts.login
