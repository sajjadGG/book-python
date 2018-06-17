import sqlite3

DATA = """4.3,3.0,1.1,0.1,0
5.8,4.0,1.2,0.2,0
5.7,4.4,1.5,0.4,0
5.4,3.9,1.3,0.4,0
5.1,3.5,1.4,0.3,0
5.7,3.8,1.7,0.3,0
5.1,3.8,1.5,0.3,0
5.4,3.4,1.7,0.2,0
5.1,3.7,1.5,0.4,0
4.6,3.6,1.0,0.2,0
5.1,3.3,1.7,0.5,0
4.8,3.4,1.9,0.2,0
5.0,3.0,1.6,0.2,0
5.0,3.4,1.6,0.4,0
5.2,3.5,1.5,0.2,0
5.2,3.4,1.4,0.2,0
4.7,3.2,1.6,0.2,0"""

SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS iris (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sepal_len INTEGER,
        sepal_wid REAL,
        petal_len REAL,
        petal_wid REAL
        species INTEGER,
    )
"""

SQL_INSERT = """
    INSERT INTO iris VALUES (
        NULL,
        :sepal_len,
        :sepal_wid,
        :petal_len,
        :petal_wid
    )
"""

with sqlite3.connect('iris.db') as db:
    db.execute(SQL_CREATE_TABLE)

    for line in DATA.split('\n'):
        sepal_len, sepal_wid, petal_len, petal_wid, species = line.split(',')
        db.execute(SQL_INSERT, locals())
