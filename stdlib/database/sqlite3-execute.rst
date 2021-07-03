SQLite3 Execute
===============


Create Table
------------
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
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     db.execute(SQL_CREATE_TABLE)


Create Index
------------
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
>>> SQL_CREATE_INDEX = """
...     CREATE INDEX
...     IF NOT EXISTS
...     astronauts_lastname_index
...     ON astronaut (lastname);"""
>>>
>>>
>>> with sqlite3.connect(DATABASE) as db:
...     db.execute(SQL_CREATE_TABLE)
...     db.execute(SQL_CREATE_INDEX)
