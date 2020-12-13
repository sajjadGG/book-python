"""
* Assignment: DataFrame Export SQL
* Filename: pandas_to_sql.py
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` as ``result: pd.DataFrame``
    3. Select 146 head rows, and last 11 from it
    4. Export data to database ``FILE`` to table ``apollo11``

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    3. Wybierz pierwszych 146 wierszy, a z nich ostatnie 11
    4. Wyeksportuj dane do bazy danych ``FILE`` do tabeli ``apollo11``

Tests:
    TODO: Doctests
"""

# Given
import sqlite3
import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/html/apollo11.html'
FILE = r'_temporary.csv'


# Solution
result = pd.read_html(DATA, header=0)[0]
result = result.head(146).tail(11)

with sqlite3.connect(FILE) as db:
    result.to_sql('apollo11', db)
