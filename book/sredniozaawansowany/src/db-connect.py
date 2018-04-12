import sqlite3

connection = sqlite3.connect('example.db')
connection = sqlite3.connect(":memory:")


with sqlite3.connect('example.db') as connection:
    connection.execute('SELECT * FROM users')