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

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> assert result.count('\\n') == 2, \
    'There should be only two newline characters in result'

    >>> line = 'We choose to go to the Moon'
    >>> assert line in result, f'Line "{line}" is not in the result'

    >>> line = 'in this decade and do the other things.'
    >>> assert line in result, f'Line "{line}" is not in the result'

    >>> line = 'Not because they are easy, but because they are hard.'
    >>> assert line in result, f'Line "{line}" is not in the result'
"""

DATA = frozenset({
    'We choose to go to the Moon',
    'in this decade and do the other things.',
    'Not because they are easy, but because they are hard.'})

# str: with lines from DATA joined with newline (`\n`) character
result = ...

# Solution
result = '\n'.join(DATA)
