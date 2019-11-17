import sqlite3


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


with sqlite3.connect(':memory:') as db:
    db.execute(SQL_CREATE_TABLE)
    db.executemany(SQL_INSERT, astronauts)

    db.row_factory = sqlite3.Row

    for row in db.execute(SQL_SELECT):
        print(dict(row))

# {'id': 1, 'pesel': 61041212345, 'first_name': 'José', 'last_name': 'Jiménez'}
# {'id': 2, 'pesel': 61041212346, 'first_name': 'Jan', 'last_name': 'Twardowski'}
# {'id': 3, 'pesel': 61041212347, 'first_name': 'Melissa', 'last_name': 'Lewis'}
# {'id': 4, 'pesel': 61041212348, 'first_name': 'Alex', 'last_name': 'Vogel'}
# {'id': 5, 'pesel': 61041212349, 'first_name': 'Ryan', 'last_name': 'Stone'}
