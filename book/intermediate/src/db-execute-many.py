import sqlite3

conn = sqlite3.connect('example.db')

# Never do this -- insecure!
symbol = 'RHAT'
conn.execute("SELECT * FROM stocks WHERE symbol='%s'" % symbol)

# Do this instead
symbol = ['RHAT']
conn.execute('SELECT * FROM stocks WHERE symbol=?', symbol)
conn.fetchone()

# Larger example that inserts many records at a time
purchases = [
    ('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
    ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
    ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
]

conn.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)