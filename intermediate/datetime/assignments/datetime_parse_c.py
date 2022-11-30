"""
* Assignment: Datetime Parse List
* Complexity: medium
* Lines of code: 8 lines
* Time: 3 min

English:
    1. Define `result: list[date]` with parsed `DATA` dates
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: list[date]` ze sparsowanymi datami `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `for ... in`
    * `try ... except`
    * ``dt.strptime()``
    * ``dt.date()``
    * ``list.append()``
    * 24-hour clock

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint
    >>> result = list(result)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, must be a list'
    >>> assert all(type(element) is date for element in result), \
    'All elements in `result` must be a date'

    >>> pprint(result, width=30)
    [datetime.date(1957, 10, 4),
     datetime.date(1961, 4, 12)]
"""

from datetime import date, datetime


DATA = [
    'October 4, 1957',  # Sputnik launch (first satellite in space)
    'Apr 12, 1961',  # Gagarin launch (first human in space)
]

# parsed DATA
# type: list[date]
result = ...


# Solution
def parse(string):
    try:
        return datetime.strptime(string, '%B %d, %Y').date()
    except ValueError:
        return datetime.strptime(string, '%b %d, %Y').date()

result = map(parse, DATA)


# Alternative
result = []

for line in DATA:
    try:
        dt = datetime.strptime(line, '%B %d, %Y')
    except ValueError:
        dt = datetime.strptime(line, '%b %d, %Y')
    result.append(dt.date())
