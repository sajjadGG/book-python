import sqlite3


SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS astronauts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        first_name TEXT,
        last_name TEXT)"""
SQL_INSERT = 'INSERT INTO astronauts VALUES (NULL, :pesel, :first_name, :last_name)'

data = {'pesel': '61041212345', 'first_name': 'José', 'last_name': 'Jiménez'}


with sqlite3.connect(':memory:') as db:
    db.execute(SQL_CREATE_TABLE)

    try:
        db.execute(SQL_INSERT, data)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
