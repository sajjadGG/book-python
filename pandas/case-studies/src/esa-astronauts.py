"""
>>> result
Timedelta('1687 days 03:29:00')
"""

import pandas as pd

pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 50)


DATA = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'

tables = pd.read_html(DATA)
current = tables[3]
former = tables[4]

c = pd.to_timedelta(current['Time in space'])
f = pd.to_timedelta(former['Time in space'])


def duration(between):
    if between is pd.NaT:
        return between
    SECOND = 1
    MINUTE = 60 * SECOND
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    MONTH = 30.436875 * DAY
    YEAR = 365.2425 * DAY
    years, seconds = divmod(between.total_seconds(), YEAR)
    months, seconds = divmod(seconds, MONTH)
    days, seconds = divmod(seconds, DAY)
    hours, seconds = divmod(between.seconds, HOUR)
    minutes, seconds = divmod(seconds, MINUTE)
    return {
        'years': int(years),
        'months': int(months),
        'days': int(days),
        'hours': int(hours),
        'minutes': int(minutes),
        'seconds': int(seconds),
    }


result = []

for i, row in current.iterrows():
    if row['Time in space'] is not pd.NaT:
        between = duration(row['Time in space'])
        row['years'] = between['years']
        row['months'] = between['months']
        row['days'] = between['days']
        row['hours'] = between['hours']
        row['minutes'] = between['minutes']
        row['seconds'] = between['seconds']
    result.append(row)
