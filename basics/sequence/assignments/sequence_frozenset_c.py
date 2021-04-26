"""
* Assignment: Sequence Frozenset Join
* Required: no
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: str`
    2. Use `str.join()` to join lines of text with newline (`\n`) character
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: str`
    2. Użyj `str.join()` aby połączyć linie tekstu znakiem końca linii (`\n`)
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * `str.join()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is str, 'Variable `result` has invalid type, should be str'
    >>> assert len(result) == 150, 'Variable `result` length should be 150'
    >>> assert result.count('\\n') == 2, 'There should be only two newline characters in result'

    >>> 'We choose to go to the Moon.' in result
    True
    >>> 'We choose to go to the Moon in this decade and do the other things.' in result
    True
    >>> 'Not because they are easy, but because they are hard.' in result
    True
"""

DATA = frozenset({
        'We choose to go to the Moon.',
        'We choose to go to the Moon in this decade and do the other things.',
        'Not because they are easy, but because they are hard.'})

result = ...  # str: with lines from DATA joined with newline (`\n`) character

# Solution
result = '\n'.join(DATA)
