"""
* Assignment: Sequence Slice Substr
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Use `str.find()` and slicing
    3. Print `TEXT` without text in `REMOVE`
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Użyj `str.find()` oraz wycinania
    3. Wypisz `TEXT` bez tekstu z `REMOVE`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is str, 'Variable `result` has invalid type, should be str'

    >>> result
    'We choose the Moon!'
"""

# Given
TEXT = 'We choose to go to the Moon!'
REMOVE = 'to go to '

result = ...  # str TEXT without REMOVE part

# Solution
a = TEXT.find(REMOVE)  # 10
b = a + len(REMOVE)  # 19
result = TEXT[:a] + TEXT[b:]
