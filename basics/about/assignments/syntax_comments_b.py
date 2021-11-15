"""
* Assignment: Syntax Comments Multiline
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Add multiline comment
       a. first line: This is first line of a multiline comment
       b. second line: This is second line of a multiline comment
    2. Run doctests - all must succeed

Polish:
    1. Dodaj komentarz wieloliniowy
       a. pierwsza linia: This is first line of a multiline comment
       b. druga linia: This is second line of a multiline comment
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> result = open(__file__).read()

    >>> assert '# This is first line of a multiline comment' in result, \
    'Please write proper multiline comment'
    >>> assert '# This is second line of a multiline comment' in result, \
    'Please write proper multiline comment'
"""

# Solution

# This is first line of a multiline comment
# This is second line of a multiline comment
