"""
* Assignment: Database Show Data
* Complexity: easy
* Lines of code: 0 lines
* Time: 3 min

English:
    1. Run file to show all data in a table:
       a. table: apollo11
    2. Run doctests - all must succeed

Polish:
    1. Uruchom plik aby wyświetlić wszystkie dane w tabeli:
       b. table: apollo11
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


SQL = """

SELECT *
FROM apollo11

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(SQL)):
        print(result)


# Solution

SQL = """

SELECT *
FROM contacts

"""
