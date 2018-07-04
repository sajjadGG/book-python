import datetime
import sqlite3

FILENAME = '../data/csv-iris-dataset.csv'
DATABASE = '../tmp/db_iris.sqlite3'

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime DATETIME,
        species TEXT,
        sepal_length REAL,
        sepal_width REAL,
        petal_length REAL,
        petal_width REAL
    );
"""

SQL_CREATE_INDEX = "CREATE INDEX IF NOT EXISTS datetime_index ON iris (datetime);"

SQL_INSERT = """
    INSERT INTO iris VALUES (
        NULL,
        :datetime,
        :species,
        :sepal_length,
        :sepal_width,
        :petal_length,
        :petal_width
    )
"""

SQL_SELECT = 'SELECT * FROM iris'

data = []

with open(FILENAME, encoding='utf-8') as file:
    count_all, count_params, *species = file.readline().strip().split(',')

    for line in file.readlines()[1:]:
        row = line.split(',')
        data.append({
            'datetime': datetime.datetime.utcnow(),
            'sepal_length': float(row[0]),
            'sepal_width': float(row[1]),
            'petal_length': float(row[2]),
            'petal_width': float(row[3]),
            'species': species[int(row[4])],
        })

with sqlite3.connect(DATABASE) as db:
    db.row_factory = sqlite3.Row
    db.execute(SQL_CREATE_TABLE)
    db.execute(SQL_CREATE_INDEX)
    db.executemany(SQL_INSERT, data)

    for row in db.execute(SQL_SELECT):
        print(dict(row))

