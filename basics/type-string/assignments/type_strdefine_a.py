"""
* Assignment: Type String Emoticon
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define `name` with value `Mark Watney`
    2. Print `Hello NAME EMOTICON`, where:
        a. NAME is a name read from user
        b. EMOTICON is Unicode Codepoint "\U0001F642"
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `name` z wartością `Mark Watney`
    2. Wypisz `Hello NAME EMOTICON`, gdzie:
        a. NAME to imię wczytane od użytkownika
        b. EMOTICON to Unicode Codepoint "\U0001F642"
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is str, 'Variable `result` has invalid type, should be str'

    >>> name in result
    True
    >>> result
    'Hello Mark Watney'
"""


name = ...  # str: Mark Watney
result = ...  # str: Hello Mark Watney

# Solution
name = 'Mark Watney'
result = f'Hello {name}'
