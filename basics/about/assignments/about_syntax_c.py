"""
* Assignment: About Syntax Interpolation
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Define variable `name` and set its value to 'Mark Watney'
    2. Define `result` with text 'Hello World {name}',
       where "Mark Watney" is the value of `name` variable
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniiuj zmienną `name` i ustaw jej wartość na 'Mark Watney'
    2. Zdefiniiuj `result` z tekstem 'Hello World {name}',
       gdzie "Mark Watney" jest wartością zmiennej `name`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * Either quotes (") or apostrophes (') will work
    * Use f-string

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(name) is str, \
    'Variable `name` has invalid type, should be str'

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> 'Mark Watney' in result
    True

    >>> name
    'Mark Watney'

    >>> result
    'Hello World Mark Watney'
"""

name = ...  # str: with Mark Watney
result = ...  # str: with Hello World {name}

# Solution
name = 'Mark Watney'
result = f'Hello World {name}'
