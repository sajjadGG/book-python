# Database Connection Tables
import sqlite3
from pathlib import Path


file = Path('sql.db')

if not file.exists():
    print('Error with database!')
    print(f'Check if `{file}` is present in current directory')
    print('Please notify instructor')
    exit(1)


try:
    db = sqlite3.connect(file)
except Exception:
    print('Error with connection')
    print('Check if you have SQLite3 installed with your Python')
    print('Please notify instructor')
    exit(1)


try:
    result = db.execute('SELECT name FROM sqlite_master')
    tables = {row[0] for row in result}
except Exception:
    print('Error with database')
    print(f'Check if `{file}` is valid SQLite3 database')
    print('Please notify instructor')
    exit(1)


if 'apollo11' not in tables:
    print('Error with table')
    print('Check if database file is not corrupted')
    print('Please notify instructor')
    exit(1)


print('Everything is ok')
print('Please notify instructor')
