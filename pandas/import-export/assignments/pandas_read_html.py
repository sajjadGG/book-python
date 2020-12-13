"""
* Assignment: Pandas Read HTML
* Filename: pandas_read_html.py
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Read data from ``DATA`` as ``result: pd.DataFrame``
    3. Print ``result`` with active European Space Agency astronauts

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Wczytaj dane z ``DATA`` jako ``result: pd.DataFrame``
    3. Wypisz ``result`` z aktywnymi astronautami Europejskiej Agencji Kosmicznej

Hints:
    * Might require ``lxml`` and ``html5lib``: ``pip install --upgrade lxml html5lib``
    * 3rd table

Tests:
    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> result['Name']
    0    Samantha Cristoforetti
    1           Alexander Gerst
    2          Andreas Mogensen
    3            Luca Parmitano
    4             Timothy Peake
    5            Thomas Pesquet
    6           Matthias Maurer
    Name: Name, dtype: object
"""


# Given
import pandas as pd

DATA = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'


# Solution
tables = pd.read_html(DATA)
result = tables[3]
