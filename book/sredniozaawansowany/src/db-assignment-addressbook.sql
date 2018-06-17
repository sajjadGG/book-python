SQL_CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS kontakty (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT,
        adresy TEXT
    )
"""

SQL_INSERT = """
    INSERT INTO kontakty VALUES (
        NULL,
        :firstname,
        :lastname,
        :adresy
    )
"""

SQL_UPDATE = """
    UPDATE kontakty SET
        firstname=:firstname,
        lastname=:lastname,
        adresy=:adresy  
    WHERE id=:id
"""

SQL_SELECT = """
    SELECT * FROM kontakty
"""