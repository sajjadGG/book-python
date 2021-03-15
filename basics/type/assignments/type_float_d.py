"""
* Assignment: Type Float Distance
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use code from "Given" section (see below)
    2. Convert units
    3. Instead `...` substitute calculated and converted values
    4. Note the number of decimal places
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj kodu z sekcji "Given" (patrz poniżej)
    2. Przekonwertuj jednostki
    3. Zamiast `...` podstaw wyliczone i przekonwertowane wartości
    4. Zwróć uwagę na ilość miejsc po przecinku
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> meters
    'Meters: 1337'
    >>> kilometers
    'Kilometers: 1'
    >>> miles
    'Miles: 0.83'
    >>> nautical_miles
    'Nautical Miles: 0.722'
    >>> all_units
    'All: km: 1, mi: 0.8, nm: 0.72'
"""

# Given
m = 1
km = 1000 * m
mi = 1609.344 * m
NM = 1852 * m

distance = 1337 * m

meters = f'Meters: {...}'  # 0 decimal places
kilometers = f'Kilometers: {...}'  # 0 decimal places
miles = f'Miles: {...}'  # 2 decimal places
nautical_miles = f'Nautical Miles: {...}'  # 3 decimal places
all_units = f'All: km: {...}, mi: {...}, nm: {...}'  # 0, 1, 2 decimal places

# Solution
meters = f'Meters: {distance/m:.0f}'
kilometers = f'Kilometers: {distance/km:.0f}'
miles = f'Miles: {distance/mi:.2f}'
nautical_miles = f'Nautical Miles: {distance/NM:.3f}'
all_units = f'All: km: {distance/km:.0f}, mi: {distance/mi:.1f}, nm: {distance/NM:.2f}'
