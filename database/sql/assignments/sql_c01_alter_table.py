"""
* Assignment: Database Alter Table
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to add column:
       a. table: contacts
       b. column: mission
       c. type: text
       d. default: null
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby dodać kolumnę:
       a. tabela: contacts
       b. kolumna: mission
       c. type: text
       d. wartość domyślna: null
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

ALTER TABLE contacts
ADD COLUMN mission TEXT DEFAULT NULL

"""
