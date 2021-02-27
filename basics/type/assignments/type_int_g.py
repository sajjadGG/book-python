"""
* Assignment: Type Int Bytes
* Complexity: easy
* Lines of code: 7 lines
* Time: 3 min

English:
    1. File size is 100 megabytes
    2. Calculate size in kilobytes
    2. Calculate size in megabits
    3. Compare result with "Tests" section (see below)

Polish:
    1. Wielkość pliku to 100 megabajtów
    2. Oblicz wielkość w kilobajtach
    2. Oblicz wielkość w megabitach
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Tests:
    >>> type(size)
    <class 'int'>
    >>> type(size_kB)
    <class 'int'>
    >>> type(size_Mb)
    <class 'int'>
    >>> size_kB
    102400
    >>> size_Mb
    800
"""

# Given
b = 1
kb = 1024 * b
Mb = 1024 * kb

B = 8 * b
kB = 1024 * B
MB = 1024 * kB

size = 100  # Megabytes
size_kB = ...  # kilobytes
size_Mb = ...  # megabits

# Solution

size = 100 * MB
size_kB = size // kB
size_Mb = size // Mb
