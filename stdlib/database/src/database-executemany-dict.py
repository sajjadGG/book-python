import sqlite3


DATABASE = ':memory:'
DATA = [{'pesel': '61041200001', 'firstname': 'José', 'lastname': 'Jiménez'},
        {'pesel': '61041200002', 'firstname': 'Jan', 'lastname': 'Twardowski'},
        {'pesel': '61041200003', 'firstname': 'Melissa', 'lastname': 'Lewis'},
        {'pesel': '61041200004', 'firstname': 'Alex', 'lastname': 'Vogel'},
        {'pesel': '61041200005', 'firstname': 'Ryan', 'lastname': 'Stone'}]

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        firstname TEXT,
        lastname TEXT)"""

SQL_INSERT = """
    INSERT INTO astronauts
    VALUES (NULL, :pesel, :firstname, :lastname)"""


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)

    try:
        db.executemany(SQL_INSERT, DATA)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
