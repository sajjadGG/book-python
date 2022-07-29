# Database Insert list[tuple]
import sqlite3


SQL = """

-- replace this comment
-- with your sql query

"""


DATA = [
    ('Mark', 'Watney'),
    ('Melissa', 'Lewis'),
    ('Rick', 'Martinez'),
    ('Alex', 'Vogel'),
    ('Beth', 'Johanssen'),
    ('Chris', 'Beck'),
]

with sqlite3.connect('sql.db') as db:
    db.executemany(SQL, DATA)
