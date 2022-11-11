"""
* Assignment: Database Show Schema
* Complexity: easy
* Lines of code: 0 lines
* Time: 3 min

English:
    1. Run file to show schema for a table:
       a. table: apollo11
    2. Run doctests - all must succeed

Polish:
    1. Uruchom plik aby wyświetlić schemat tabeli:
       a. table: apollo11
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3


SQL = """

SELECT sql
FROM sqlite_master
WHERE tbl_name = 'apollo11'

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for schema in db.execute(SQL):
        print('\n', schema['sql'], sep='')


# Solution

SQL = """

SELECT sql
FROM sqlite_master
WHERE tbl_name = 'apollo11'

"""
