# Database Show Data
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
