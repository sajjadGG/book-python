import sqlite3

con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row


for row in con.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

# ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
# ('2006-03-28', 'BUY', 'IBM', 1000, 45.0)
# ('2006-04-06', 'SELL', 'IBM', 500, 53.0)
# ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)



cur = con.cursor()
cur.execute("select 'John' as name, 42 as age")

for row in cur:
    assert row[0] == row["name"]
    assert row["name"] == row["nAmE"]
    assert row[1] == row["age"]
    assert row[1] == row["AgE"]