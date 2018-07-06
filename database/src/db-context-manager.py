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

SQL_SELECT = """
    SELECT * FROM kontakty
"""

dane = {'pesel': '61041212345', 'firstname': 'José', 'lastname': 'Jiménez'},


with sqlite3.connect(':memory:') as connection:
    connection.execute(SQL_CREATE_TABLE)
    connection.execute(SQL_INSERT, dane)

    for row in connection.execute(SQL_SELECT, dane):
        print(dict(row))
