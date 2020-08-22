import sqlite3


DATABASE = ':memory:'

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        first_name TEXT,
        last_name TEXT)"""
SQL_INSERT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :first_name, :last_name)'
SQL_SELECT = 'SELECT * FROM astronauts'


astronauts = [
    {'pesel': '61041212345', 'first_name': 'José', 'last_name': 'Jiménez'},
    {'pesel': '61041212346', 'first_name': 'Jan', 'last_name': 'Twardowski'},
    {'pesel': '61041212347', 'first_name': 'Melissa', 'last_name': 'Lewis'},
    {'pesel': '61041212348', 'first_name': 'Alex', 'last_name': 'Vogel'},
    {'pesel': '61041212349', 'first_name': 'Ryan', 'last_name': 'Stone'},
]


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, astronauts)
    cursor = db.cursor()

    for row in cursor.execute(SQL_SELECT):
        print(row)

# (1, 61041212345, 'José', 'Jiménez')
# (2, 61041212346, 'Jan', 'Twardowski')
# (3, 61041212347, 'Melissa', 'Lewis')
# (4, 61041212348, 'Alex', 'Vogel')
# (5, 61041212349, 'Ryan', 'Stone')
