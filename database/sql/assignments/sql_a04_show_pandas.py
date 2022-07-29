# Database Show Data
import sqlite3
import pandas as pd


SQL = """

SELECT *
FROM sqlite_master

"""


with sqlite3.connect('sql.db') as db:
    ...
