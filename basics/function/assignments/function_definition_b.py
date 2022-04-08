"""
* Assignment: Function Definition Call
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 2 min

English:
    1. Call function `beetlejuice` three times
    2. Run doctests - all must succeed

Polish:
    1. Wywołaj funkcję `beetlejuice` trzy razy
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(beetlejuice)

    >>> result
    ['Beetlejuice', 'Beetlejuice', 'Beetlejuice']
"""

result = []

def beetlejuice():
    result.append('Beetlejuice')


# Solution
beetlejuice()
beetlejuice()
beetlejuice()
