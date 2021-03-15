"""
* Assignment: Type Int Bandwidth
* Complexity: easy
* Lines of code: 10 lines
* Time: 3 min

English:
    1. Having internet connection with speed 100 Mb/s
    2. How long will take to download 100 MB?
    3. To calculate time divide file size by speed
    3. Note, that all values must be `int` (type cast if needed)
    3. In Calculations use floordiv (`//`)
    4. Compare result with "Tests" section (see below)

Polish:
    1. Mając łącze internetowe 100 Mb/s
    2. Ile zajmie ściągnięcie pliku 100 MB?
    3. Aby wyliczyć czas podziel wielkość pliku przez prękość
    3. Zwróć uwagę, że wszystkie wartości mają być `int` (rzutuj typ jeżeli potrzeba)
    3. W obliczeniach użyj floordiv (`//`)
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Tests:
    >>> type(bandwidth)
    <class 'int'>
    >>> type(size)
    <class 'int'>
    >>> type(duration)
    <class 'int'>
    >>> duration // SECOND
    8
"""

# Given
SECOND = 1

b = 1
kb = 1024 * b
Mb = 1024 * kb

B = 8 * b
kB = 1024 * B
MB = 1024 * kB

bandwidth = ...  # 100 megabits per second
size = ...  # 100 megabytes
duration = ...  # size by bandwidth in seconds

# Solution
bandwidth = (100 * Mb) // SECOND
size = 100 * MB
duration = (size // bandwidth)
