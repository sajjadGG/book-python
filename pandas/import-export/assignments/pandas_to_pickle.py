"""
* Assignment: DataFrame Export Pickle
* Filename: pandas_to_pickle.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` as ``result: pd.DataFrame``
    3. Select 146 head rows, and last 11 from it
    3. Export to file ``FILE`` data in Pickle format

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    3. Wybierz pierwszych 146 wierszy, a z nich ostatnie 11
    3. Wyeksportuj do pliku ``FILE`` dane w formacie Pickle

Tests:
    TODO: Doctests
"""


# Given
import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/html/apollo11.html'
FILE = r'_temporary.csv'


# Solution
result = pd.read_html(DATA, header=0)[0]
result = result.head(146).tail(11)
result.to_pickle(FILE)

