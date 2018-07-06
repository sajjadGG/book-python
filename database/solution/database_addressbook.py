import sqlite3




ksiazka_adresowa = [
    {'firstname': 'José', 'lastname': 'Jiménez', 'adresy': 'NASA, Kennedy Space Center, FL, USA'}
]



with sqlite3.connect('database.sqlite3') as connection:
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(SQL_CREATE_TABLE)
    cursor.executemany(SQL_INSERT, ksiazka_adresowa)

    for row in cursor.execute(SQL_SELECT):
        data = dict(row)
        print(data)

        data['lastname'] = 'Ivanovic'

        cursor.execute(SQL_UPDATE, data)
