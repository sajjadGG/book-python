import sqlite3

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS kontakty (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pesel INTEGER UNIQUE,
        firstname TEXT,
        lastname TEXT
    )
"""

SQL_INSERT = """
    INSERT INTO kontakty VALUES (
        NULL,
        :pesel,
        :firstname,
        :lastname
    )
"""

ksiazka_adresowa = [
    {'pesel': '61041212345', 'firstname': 'José', 'lastname': 'Jiménez'},
    {'pesel': '61041212346', 'firstname': 'Matt', 'lastname': 'Kowalski'},
    {'pesel': '61041212347', 'firstname': 'Melissa', 'lastname': 'Lewis'},
    {'pesel': '61041212348', 'firstname': 'Alex', 'lastname': 'Vogel'},
    {'pesel': '61041212349', 'firstname': 'Ryan', 'lastname': 'Stone'},
]


with sqlite3.connect(':memory:') as connection:
    connection.execute(SQL_CREATE_TABLE)

    try:
        with connection.cursor() as cursor:
            cursor.executemany(SQL_INSERT, ksiazka_adresowa)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
