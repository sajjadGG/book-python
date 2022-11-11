"""
* Assignment: Database Create Index
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to create index:
       a. name: idx_contacts_lastname
       b. table: contacts
       c. column: lastname
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby stworzyć indeks:
       a. nazwa: idx_contacts_lastname
       b. tabela: contacts
       c. kolumna: lastname
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

CREATE INDEX IF NOT EXISTS idx_contacts_lastname
ON contacts(lastname)

"""
