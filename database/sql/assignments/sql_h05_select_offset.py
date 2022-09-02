# Database Select Offset
import sqlite3


SQL = """

SELECT datetime AS dt, category AS lvl, event
FROM apollo11
LIMIT 30

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(SQL)):
        print(result)
