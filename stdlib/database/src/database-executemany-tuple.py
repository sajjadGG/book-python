import sqlite3


DATABASE = ':memory:'

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        first_name TEXT,
        last_name TEXT)"""

SQL_INSERT_TUPLE = 'INSERT INTO astronauts VALUES (NULL, ?, ?, ?)'


DATA = [
    (61041212345, 'José', 'Jiménez'),
    (61041212346, 'Jan', 'Twardowski'),
    (61041212347, 'Melissa', 'Lewis'),
    (61041212348, 'Alex', 'Vogel'),
    (61041212349, 'Ryan', 'Stone'),
]


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)

    try:
        db.executemany(SQL_INSERT_TUPLE, DATA)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
