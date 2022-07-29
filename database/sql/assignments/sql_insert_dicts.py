# Database Insert list[dict]
import sqlite3


SQL = """

-- replace this comment
-- with your sql query   

"""


DATA = [
    {'firstname': 'Mark', 'lastname': 'Watney'},
    {'firstname': 'Melissa', 'lastname': 'Lewis'},
    {'firstname': 'Rick', 'lastname': 'Martinez'},
    {'firstname': 'Alex', 'lastname': 'Vogel'},
    {'firstname': 'Beth', 'lastname': 'Johanssen'},
    {'firstname': 'Chris', 'lastname': 'Beck'},
]

with sqlite3.connect('sql.db') as db:
    db.executemany(SQL, DATA)
