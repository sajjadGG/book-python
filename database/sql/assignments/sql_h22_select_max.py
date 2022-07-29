# Database Select Max
import sqlite3


SQL = """

SELECT *
FROM apollo11

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(SQL)):
        print(result)
