"""
* Assignment: Type Int Bits
* Required: no
* Complexity: medium
* Lines of code: 4 lines
* Time: 3 min

English:
    1. File size is 1337 megabits [Mb]
    2. Calculate size in bits [b]
    3. Calculate size in kilobits [kb]
    4. In Calculations use floordiv (`//`)
    5. Run doctests - all must succeed

Polish:
    1. Wielkość pliku to 1337 megabits [Mb]
    2. Oblicz wielkość w bitach [b]
    3. Oblicz wielkość w kilobitach [kb]
    4. W obliczeniach użyj floordiv (`//`)
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 1 kb = 1024 b
    * 1 Mb = 1024 Kb

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert size_b is not Ellipsis, 'Assignment solution must be in `size_b` instead of ... (Ellipsis)'
    >>> assert size_kb is not Ellipsis, 'Assignment solution must be in `size_kb` instead of ... (Ellipsis)'
    >>> assert size_Mb is not Ellipsis, 'Assignment solution must be in `size_Mb` instead of ... (Ellipsis)'
    >>> assert type(size_b) is int, 'Variable `size_b` has invalid type, should be int'
    >>> assert type(size_kb) is int, 'Variable `size_kb` has invalid type, should be int'
    >>> assert type(size_Mb) is int, 'Variable `size_Mb` has invalid type, should be int'

    >>> size_b
    1401946112
    >>> size_kb
    1369088
    >>> size_Mb
    1337
"""

b = 1
kb = 1024 * b
Mb = 1024 * kb

size = ...  # int: 1337 megabits
size_b = ...  # int: size in bytes
size_kb = ...  # int: size in kilobytes
size_Mb = ...  # int: size in megabytes

# Solution
size = 1337 * Mb
size_b = size // b
size_kb = size // kb
size_Mb = size // Mb
