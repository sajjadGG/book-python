"""
* Assignment: Pandas Read PythonDict
* Complexity: easy
* Lines of code: 8 lines
* Time: 13 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z DATA jako result: pd.DataFrame
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> result  # doctest: +NORMALIZE_WHITESPACE
      firstname  lastname mission1_year mission1_name mission2_year mission2_name
    0      Mark    Watney          2035         Ares3           NaN           NaN
    1   Melissa     Lewis          2030         Ares1          2035         Ares3
    2      Rick  Martinez           NaN           NaN           NaN           NaN
"""
import pandas as pd


DATA = [
    {"firstname": "Mark", "lastname": "Watney", "missions": [
        {"year": "2035", "name": "Ares3"}]},

    {"firstname": "Melissa", "lastname": "Lewis", "missions": [
         {"year": "2030", "name": "Ares1"},
         {"year": "2035", "name": "Ares3"}]},

    {"firstname": "Rick", "lastname": "Martinez", "missions": []}
]


# list[dict]: flatten data, each mission field prefixed with mission and number
data = ...

# pd.DataFrame: data as pd.DataFrame
result = ...


# Solution
data = []
for astronaut in DATA:
    for i, mission in enumerate(astronaut.pop('missions'), start=1):
        for field,value in mission.items():
            column_name = f'mission{i}_{field}'
            astronaut[column_name] = value
    data.append(astronaut)

result = pd.DataFrame(data)
