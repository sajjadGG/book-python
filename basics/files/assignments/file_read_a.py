"""
* Assignment: File Read Str
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    2. Write `DATA` to file `FILE`
    3. Read `FILE` to `result: str`
    4. Print `result`
    5. Run doctests - all must succeed

Polish:
    1. Zapisz `DATA` do pliku `FILE`
    2. Wczytaj `FILE` do `result: str`
    3. Wypisz `result`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str
    >>> assert result == DATA

    >>> result
    'hello'

    >>> from os import remove; remove(FILE)
"""

FILE = '_temporary.txt'
DATA = 'hello'

with open(FILE, mode='wt') as file:
    file.write(DATA)

result = ...  # str: FILE content

# Solution
with open(FILE, mode='rt') as file:
    result = file.read()
