"""
* Assignment: Sequence Frozenset Split
* Required: no
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: frozenset`
    2. Split lines and convert result to frozenset
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: frozenset`
    2. Podziel linie i przekonwertuj wynik do frozenset
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `str.splitlines()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is frozenset, 'Variable `result` has invalid type, should be frozenset'
    >>> assert len(result) == 3, 'Variable `result` length should be 3'

    >>> 'We choose to go to the Moon.' in result
    True
    >>> 'We choose to go to the Moon in this decade and do the other things.' in result
    True
    >>> 'Not because they are easy, but because they are hard.' in result
    True
"""

DATA = """We choose to go to the Moon.
We choose to go to the Moon in this decade and do the other things.
Not because they are easy, but because they are hard."""

result = ...  # frozenset[str]: with DATA split by lines

# Solution
result = frozenset(DATA.splitlines())
