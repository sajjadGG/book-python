# Database Insert Dict
import sqlite3


SQL = """

-- replace this comment
-- with your sql query

"""


DATA = {
    'firstname': 'Mark',
    'lastname': 'Watney',
}

with sqlite3.connect('sql.db') as db:
    db.execute(SQL, DATA)
