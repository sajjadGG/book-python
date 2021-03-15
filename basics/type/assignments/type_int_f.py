"""
* Assignment: Type Int Bits
* Complexity: medium
* Lines of code: 4 lines
* Time: 3 min

English:
    1. File size is 1337 megabits [Mb]
    2. Calculate size in bits [b]
    3. Calculate size in kilobits [kb]
    4. In Calculations use floordiv (`//`)
    5. Compare result with "Tests" section (see below)

Polish:
    1. Wielkość pliku to 1337 megabits [Mb]
    2. Oblicz wielkość w bitach [b]
    3. Oblicz wielkość w kilobitach [kb]
    4. W obliczeniach użyj floordiv (`//`)
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 kb = 1024 b
    * 1 Mb = 1024 Kb

Tests:
    >>> type(size_b)
    <class 'int'>
    >>> type(size_kb)
    <class 'int'>
    >>> type(size_Mb)
    <class 'int'>
    >>> size_b
    1401946112
    >>> size_kb
    1369088
    >>> size_Mb
    1337
"""

# Given
b = 1
kb = 1024 * b
Mb = 1024 * kb

size = 1337*Mb  # megabits
size_b = ...  # bytes
size_kb = ...  # kilobytes
size_Mb = ...  # megabytes

# Solution
size = 1337 * Mb
size_b = size // b
size_kb = size // kb
size_Mb = size // Mb
