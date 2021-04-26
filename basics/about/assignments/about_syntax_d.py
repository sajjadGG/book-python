"""
* Assignment: About Syntax Comments
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Add first comment:
       a. line comment
       b. content: This is my first Python script
    2. Add second comment:
       a. multiline comment
       b. first line: This is first line of a multiline comment
       c. second line: This is second line of a multiline comment
    3. Add third comment:
       a. inline comment to `left_alone_on_mars` variable
       b. content: Space Pirate
    4. Run doctests - all must succeed

Polish:
    1. Dodaj pierwszy komentarz:
       a. komentarz liniowy
       b. treść: This is my first Python script
    2. Dodaj drugi komentarz:
       a. komentarz wieloliniowy
       b. pierwsza linia: This is first line of a multiline comment
       c. druga linia: This is second line of a multiline comment
    3. Dodaj trzeci komentarz:
       a. komentarz na końcu linii definicji zmiennej `left_alone_on_mars`
       b. treść: Space Pirate
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result = open(__file__).read()

    >>> assert type(left_alone_on_mars) is str, 'Variable `left_alone_on_mars` has invalid type, should be str'
    >>> assert '# This is my first Python script' in result, 'Please write proper line comment'
    >>> assert '# This is first line of a multiline comment' in result, 'Please write proper multiline comment'
    >>> assert '# This is second line of a multiline comment' in result, 'Please write proper multiline comment'
    >>> assert "left_alone_on_mars = 'Mark Watney'  # Space Pirate" in result, 'Please write proper inline comment'

    >>> left_alone_on_mars
    'Mark Watney'
"""

left_alone_on_mars = 'Mark Watney'

# Solution

# This is my first Python script

# This is first line of a multiline comment
# This is second line of a multiline comment

left_alone_on_mars = 'Mark Watney'  # Space Pirate
