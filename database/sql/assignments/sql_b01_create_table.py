"""
* Assignment: Database Create Table
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Write SQL query to create table:
       a. table: contacts
       b. column: id, integer, primary key, autoincrement
       c. column: firstname, text
       d. column: lastname, text
       e. column: birthday, date, default null
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby stworzyć tabelę:
       a. tabela: contacts
       b. kolumna: id, integer, primary key, autoincrement
       c. kolumna: firstname, text
       d. kolumna: lastname, text
       e. kolumna: birthday, date, default null
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


SQL = """

-- replace this comment
-- with your sql query

"""


with sqlite3.connect('sql.db') as db:
    db.execute(SQL)


# Solution

SQL = """

CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT,
    lastname TEXT,
    birthday DATE DEFAULT NULL
)

"""
