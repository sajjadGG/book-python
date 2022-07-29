# Database Show Schema
import sqlite3


SQL = """

SELECT sql 
FROM sqlite_master 
WHERE tbl_name = 'contacts'

"""


with sqlite3.connect('sql.db') as db:
    db.row_factory = sqlite3.Row
    for schema in db.execute(SQL):
        print('\n', schema['sql'], sep='')
