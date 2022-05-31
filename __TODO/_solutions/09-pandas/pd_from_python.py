import sqlite3
import pandas as pd

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)


DATABASE = 'space.db'

SQL = """

    SELECT *
    FROM astronauts

"""


with sqlite3.connect(DATABASE) as db:
    df = pd.read_sql(SQL, db)

print(df)
