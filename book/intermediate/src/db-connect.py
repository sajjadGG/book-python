import sqlite3

with sqlite3.connect('example.db') as connection:
    connection.execute('SELECT * FROM users')
