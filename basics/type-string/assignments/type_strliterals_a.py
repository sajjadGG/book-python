"""
* Assignment: Type String Emoticon
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `name` with value `Mark Watney`
    2. Print `Hello World EMOTICON`, where:
    3. EMOTICON is Unicode Codepoint "\U0001F600"
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `name` z wartością `Mark Watney`
    2. Wypisz `Hello World EMOTICON`
    3. EMOTICON to Unicode Codepoint "\U0001F600"
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is str, 'Variable `result` has invalid type, should be str'

    >>> '\U0001F600' in result
    True
    >>> result
    'Hello World 😀'
"""

EMOTICON = '\U0001F600'
result = ...  # str: Hello World EMOTICON


# Solution
result = f'Hello World {EMOTICON}'
