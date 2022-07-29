# Database Insert Tuple
import sqlite3


SQL = """

-- replace this comment
-- with your sql query

"""


DATA = ('Mark', 'Watney')

with sqlite3.connect('sql.db') as db:
    db.execute(SQL, DATA)
