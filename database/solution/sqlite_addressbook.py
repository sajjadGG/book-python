import sqlite3




addressbook = [
    {'first_name': 'Mark', 'last_name': 'Watney', 'location': 'NASA, Johnson Space Center, FL, USA'}
]


with sqlite3.connect('database.sqlite3') as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(SQL_CREATE_TABLE)
    cursor.executemany(SQL_INSERT, ksiazka_adresowa)

    for row in cursor.execute(SQL_SELECT):
        data = dict(row)
        print(data)

        data['last_name'] = 'Иванович'

        cursor.execute(SQL_UPDATE, data)
