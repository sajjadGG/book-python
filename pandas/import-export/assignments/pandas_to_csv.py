"""
* Assignment: DataFrame Export CSV
* Filename: pandas_to_csv.py
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` as ``result: pd.DataFrame``
    3. Select 146 head rows, and last 11 from it
    3. Export to file ``FILE`` data in CSV format

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    3. Wybierz pierwszych 146 wierszy, a z nich ostatnie 11
    3. Wyeksportuj do pliku ``FILE`` dane w formacie CSV

Tests:
    >>> result = open(FILE).read()
    >>> print(result)  # doctest: +NORMALIZE_WHITESPACE
    ,Event,GET  (hhh:mm:ss),GMT  Time,GMT  Date
    135,LM lunar landing.,102:45:39.9,20:17:39,20 Jul 1969
    136,LM powered descent engine cutoff.,102:45:41.40,20:17:41,20 Jul 1969
    137,Decision made to proceed with EVA prior to first rest period.,104:40:00,22:12:00,20 Jul 1969
    138,Preparation for EVA started.,106:11:00,23:43:00,20 Jul 1969
    139,EVA started (hatch open).,109:07:33,02:39:33,21 Jul 1969
    140,CDR completely outside LM on porch.,109:19:16,02:51:16,21 Jul 1969
    141,Modular equipment stowage assembly deployed (CDR).,109:21:18,02:53:18,21 Jul 1969
    142,First clear TV picture received.,109:22:00,02:54:00,21 Jul 1969
    143,"CDR at foot of ladder (starts to report, then pauses to listen).",109:23:28,02:55:28,21 Jul 1969
    144,CDR at foot of ladder and described surface as “almost like a powder.”,109:23:38,02:55:38,21 Jul 1969
    145,1st step taken lunar surface (CDR). “That’s one small step for a man…one giant leap for mankind.”,109:24:15,02:56:15,21 Jul 1969
    >>> from os import remove
    >>> remove(FILE)
"""


# Given
import pandas as pd

DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/html/apollo11.html'
FILE = r'_temporary.csv'


# Solution
result = pd.read_html(DATA, header=0)[0]
result = result.head(146).tail(11)
result.to_csv(FILE)

