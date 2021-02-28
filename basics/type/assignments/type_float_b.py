"""
* Assignment: Type Float Altitude
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Plane altitude is 10.000 ft
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Result round to one decimal place
    5. Compare result with "Tests" section (see below)

Polish:
    1. Wysokość lotu samolotem wynosi 10 000 ft
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Wynik zaokrąglij do jednego miejsca po przecinku
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(altitude)
    <class 'float'>
    >>> imperial
    10000.0
    >>> metric
    3048.0
"""

# Given
m = 1
ft = 0.3048 * m

altitude: float  # Plane altitude is 10.000 ft
imperial: float
metric: float

# Solution
altitude = 10_000 * ft
imperial = altitude / ft
metric = altitude / m
