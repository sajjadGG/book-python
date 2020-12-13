"""
* Assignment: DataFrame Export JSON
* Filename: pandas_to_json.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` as ``result: pd.DataFrame``
    3. Select 146 head rows, and last 11 from it
    3. Export to file ``FILE`` data in JSON format

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    3. Wybierz pierwszych 146 wierszy, a z nich ostatnie 11
    3. Wyeksportuj do pliku ``FILE`` dane w formacie JSON

Tests:
    >>> result = open(FILE).read()
    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE

    TODO: Doctests

    >>> from os import remove
    >>> remove(FILE)
"""


# Given
import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/html/apollo11.html'
FILE = r'_temporary.csv'


# Solution
data = pd.read_html(DATA, header=0)[1]
result = data.head(146).tail(11).to_json(FILE)

