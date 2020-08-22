import sqlite3


DATABASE = ':memory:'

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        first_name TEXT,
        last_name TEXT)"""

SQL_INSERT_DICT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :first_name, :last_name)'


DATA = [
    {'pesel': '61041212345', 'first_name': 'José', 'last_name': 'Jiménez'},
    {'pesel': '61041212346', 'first_name': 'Jan', 'last_name': 'Twardowski'},
    {'pesel': '61041212347', 'first_name': 'Melissa', 'last_name': 'Lewis'},
    {'pesel': '61041212348', 'first_name': 'Alex', 'last_name': 'Vogel'},
    {'pesel': '61041212349', 'first_name': 'Ryan', 'last_name': 'Stone'},
]


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)

    try:
        db.executemany(SQL_INSERT_DICT, DATA)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
