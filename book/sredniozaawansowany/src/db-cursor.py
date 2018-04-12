import sqlite3


conn = sqlite3.connect('example.db')
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE stocks (
        date text,
        trans text,
        symbol text,
        qty real,
        price real
)""")

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# And this is the named style:
cur.execute("select * from stocks where trans=:trans and symbol=:symbol",
            {"symbol": 'RHAT', "trans": 'BUY'})

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()