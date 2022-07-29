# Database Show Tables
import sqlite3


SQL = """

SELECT name 
FROM sqlite_master 
WHERE type='table'

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for table in db.execute(SQL):
        print(table['name'])
