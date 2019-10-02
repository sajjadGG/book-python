import sqlite3
from datetime import datetime, timezone

DATABASE = r':memory:'
FILE = r'sqlite_iris.csv'

SPECIES = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica',
}

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime DATETIME,
        species TEXT,
        sepal_length REAL,
        sepal_width REAL,
        petal_length REAL,
        petal_width REAL
    );"""

SQL_CREATE_INDEX = """
    CREATE INDEX IF NOT EXISTS
        iris_datetime_index ON iris (datetime);
"""

SQL_INSERT = """
    INSERT INTO iris VALUES (
        NULL,
        :datetime,
        :species,
        :sepal_length,
        :sepal_width,
        :petal_length,
        :petal_width
    );"""

SQL_SELECT = 'SELECT * FROM iris ORDER BY datetime DESC'

DATA = []

with open(FILE) as file:
    for line in file:
        line = line.strip().split(',')
        DATA.append({
            'datetime': datetime.now(tz=timezone.utc),
            'sepal_length': float(line[0]),
            'sepal_width': float(line[1]),
            'petal_length': float(line[2]),
            'petal_width': float(line[3]),
            'species': SPECIES[int(line[4])],
        })


with sqlite3.connect(DATABASE) as db:
    db.execute(SQL_CREATE_TABLE)
    db.execute(SQL_CREATE_INDEX)
    db.executemany(SQL_INSERT, DATA)

    db.row_factory = sqlite3.Row

    for row in db.execute(SQL_SELECT):
        print(dict(row))
