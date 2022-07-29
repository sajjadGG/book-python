# Database Show Data
import sqlite3


SQL = """

SELECT *
FROM sqlite_master

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for result in map(dict, db.execute(SQL)):
        print(result)
