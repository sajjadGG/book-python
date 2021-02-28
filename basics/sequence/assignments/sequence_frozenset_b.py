"""
* Assignment: Sequence Frozenset Split
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: frozenset`
    3. Split lines and convert result to frozenset
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: frozenset`
    3. Podziel linie i przekonwertuj wynik do frozenset
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hint:
    * `str.splitlines()`

Tests:
    >>> type(result)
    <class 'frozenset'>
    >>> len(result)
    3
    >>> 'We choose to go to the Moon.' in result
    True
    >>> 'We choose to go to the Moon in this decade and do the other things.' in result
    True
    >>> 'Not because they are easy, but because they are hard.' in result
    True
"""

# Given
DATA = """We choose to go to the Moon.
We choose to go to the Moon in this decade and do the other things.
Not because they are easy, but because they are hard."""

result: frozenset  # Split lines and convert to frozenset

# Solution
result = DATA.splitlines()
result = frozenset(result)
