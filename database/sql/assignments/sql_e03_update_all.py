# Database Update All
import sqlite3


SQL = """

-- replace this comment
-- with your sql query

"""


with sqlite3.connect('sql.db') as db:
    db.execute(SQL)