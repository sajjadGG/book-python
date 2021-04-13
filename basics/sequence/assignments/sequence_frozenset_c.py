"""
* Assignment: Sequence Frozenset Join
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Define `result: str`
    3. Use `str.join()` to join lines of text with newline (`\n`) character
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj `result: str`
    3. Użyj `str.join()` aby połączyć linie tekstu znakiem końca linii (`\n`)
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hint:
    * `str.join()`

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assignment solution must be in `result` instead of ... (Ellipsis)'

    >>> type(result)
    <class 'str'>
    >>> len(result)
    150
    >>> result.count('\\n')
    2

    >>> 'We choose to go to the Moon.' in result
    True
    >>> 'We choose to go to the Moon in this decade and do the other things.' in result
    True
    >>> 'Not because they are easy, but because they are hard.' in result
    True
"""

# Given
DATA = frozenset({
        'We choose to go to the Moon.',
        'We choose to go to the Moon in this decade and do the other things.',
        'Not because they are easy, but because they are hard.'})

result = ...  # frozenset with lines from DATA joined with newline (`\n`) character

# Solution
result = '\n'.join(DATA)
