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
    {'pesel': '61041212345', 'firstname': 'Jose', 'lastname': 'Jimenez'},
    {'pesel': '61041212345', 'firstname': 'Max', 'lastname': 'Peck'},
]


with sqlite3.connect(':memory:') as connection:
    connection.execute(SQL_CREATE_TABLE)

    try:
        with connection.cursor() as cursor:
            cursor.executemany(SQL_INSERT, ksiazka_adresowa)
    except sqlite3.IntegrityError:
        print('Pesel need to be UNIQUE')
