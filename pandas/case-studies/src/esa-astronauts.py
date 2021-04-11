"""
>>> result
Timedelta('1687 days 03:29:00')
"""

import pandas as pd


DATA = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'

tables = pd.read_html(DATA)
current = tables[3]
former = tables[4]

c = pd.to_timedelta(current['Time in space'])
f = pd.to_timedelta(former['Time in space'])

result = (c+f).sum()
