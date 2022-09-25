"""
* Assignment: Database Show DataFrame
* Complexity: easy
* Lines of code: 0 lines
* Time: 3 min

English:
    1. Run file to show data from table in DataFrame format
    2. Run doctests - all must succeed

Polish:
    1. Uruchom plik aby wyświetlić dane z tabeli w formacie DataFrame
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    TODO: tests
"""

import sqlite3
import pandas as pd

pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)

SQL = """

SELECT *
FROM apollo11

"""


with sqlite3.connect('sql.db') as db:
    df = pd.read_sql(SQL, db)

print(df)


# Solution

SQL = """



"""
