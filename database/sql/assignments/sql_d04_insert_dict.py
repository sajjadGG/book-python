"""
* Assignment: Database Insert Dict
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Write SQL query to insert data
    2. Run doctests - all must succeed

Polish:
    1. Napisz zapytanie SQL aby wstawić dane
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


SQL = """

-- replace this comment
-- with your sql query

"""


DATA = {
    'firstname': 'Mark',
    'lastname': 'Watney',
}

with sqlite3.connect('sql.db') as db:
    db.execute(SQL, DATA)


# Solution

SQL = """



"""
