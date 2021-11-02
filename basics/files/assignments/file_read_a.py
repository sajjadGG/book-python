"""
* Assignment: File Read Str
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Read `FILE` to `result: str`
    2. Run doctests - all must succeed

Polish:
    1. Wczytaj `FILE` do `result: str`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> assert type(result) is str
    >>> assert result == DATA

    >>> result
    'hello'

    >>> remove(FILE)
"""

FILE = '_temporary.txt'
DATA = 'hello'

with open(FILE, mode='wt') as file:
    file.write(DATA)

# str: FILE content
result = ...

# Solution
with open(FILE, mode='rt') as file:
    result = file.read()
