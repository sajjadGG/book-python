"""
* Assignment: Type Float Velocity
* Complexity: easy
* Lines of code: 9 lines
* Time: 3 min

English:
    1. Speed limit is 75 MPH
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Speed limit print in KPH (km/h)
    5. Result round to one decimal place
    6. Compare result with "Tests" section (see below)

Polish:
    1. Ograniczenie prędkości wynosi 75 MPH
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Ograniczenie prędkości wypisz w KPH (km/h)
    5. Wynik zaokrąglij do jednego miejsca po przecinku
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(kph)
    <class 'float'>
    >>> type(mph)
    <class 'float'>
    >>> type(speed_limit)
    <class 'float'>
    >>> round(kph, 3)
    0.278
    >>> round(mph, 3)
    0.447
    >>> round(speed_limit/mph, 1)
    75.0
    >>> round(speed_limit/kph, 1)
    120.7
"""

# Given
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

m = 1
km = 1000 * m
mi = 1609.344 * m

mph = ...  # miles per hour
kph = ...  # kilometers per hour

speed_limit = 70  # miles per hour

# Solution
kph = km / HOUR
mph = mi / HOUR

speed_limit = 75 * mph
