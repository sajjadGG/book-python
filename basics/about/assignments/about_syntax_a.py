"""
* Assignment: About Syntax HelloWorld
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result` with text 'Hello World'

Polish:
    1. Zdefiniuj zmienną `result` z tekstem 'Hello World'

Hint:
    * Either quotes (") or apostrophes (') will work

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> 'Hello' in result
    True
    >>> 'World' in result
    True
"""

# Given

result = ...  # str: with Hello and World

# Solution
result = 'Hello World'
