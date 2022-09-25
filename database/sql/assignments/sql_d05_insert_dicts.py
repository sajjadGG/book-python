"""
* Assignment: Database Insert List[Dict]
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


DATA = [
    {'firstname': 'Mark', 'lastname': 'Watney'},
    {'firstname': 'Melissa', 'lastname': 'Lewis'},
    {'firstname': 'Rick', 'lastname': 'Martinez'},
    {'firstname': 'Alex', 'lastname': 'Vogel'},
    {'firstname': 'Beth', 'lastname': 'Johanssen'},
    {'firstname': 'Chris', 'lastname': 'Beck'},
]

with sqlite3.connect('sql.db') as db:
    db.executemany(SQL, DATA)


# Solution

SQL = """



"""
