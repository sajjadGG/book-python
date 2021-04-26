"""
* Assignment: Type Float Distance
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Convert units
    2. Instead `...` substitute calculated and converted values
    3. Note the number of decimal places
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj jednostki
    2. Zamiast `...` podstaw wyliczone i przekonwertowane wartości
    3. Zwróć uwagę na ilość miejsc po przecinku
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert meters is not Ellipsis, 'Assignment solution must be in `meters` instead of ... (Ellipsis)'
    >>> assert kilometers is not Ellipsis, 'Assignment solution must be in `kilometers` instead of ... (Ellipsis)'
    >>> assert miles is not Ellipsis, 'Assignment solution must be in `miles` instead of ... (Ellipsis)'
    >>> assert nautical_miles is not Ellipsis, 'Assignment solution must be in `nautical_miles` instead of ... (Ellipsis)'
    >>> assert all_units is not Ellipsis, 'Assignment solution must be in `all_units` instead of ... (Ellipsis)'
    >>> assert type(meters) is str, 'Variable `volume` has invalid type, should be str'
    >>> assert type(kilometers) is str, 'Variable `volume` has invalid type, should be str'
    >>> assert type(miles) is str, 'Variable `volume` has invalid type, should be str'
    >>> assert type(nautical_miles) is str, 'Variable `volume` has invalid type, should be str'
    >>> assert type(all_units) is str, 'Variable `volume` has invalid type, should be str'

    >>> meters
    'Meters: 1337'
    >>> kilometers
    'Kilometers: 1'
    >>> miles
    'Miles: 0.83'
    >>> nautical_miles
    'Nautical Miles: 0.722'
    >>> all_units
    'All: km: 1, mi: 0.8, NM: 0.72'
"""

m = 1
km = 1000 * m
mi = 1609.344 * m
NM = 1852 * m

distance = 1337 * m

meters = f'Meters: {...}'  # float: distance in meters 0 decimal places
kilometers = f'Kilometers: {...}'  # float: distance in kilometers with 0 decimal places
miles = f'Miles: {...}'  # float: distance in miles with 2 decimal places
nautical_miles = f'Nautical Miles: {...}'  # float: distance in nautical miles with 3 decimal places
all_units = f'All: km: {...}, mi: {...}, NM: {...}'  # float: distance in km, mi, NM with 0, 1, 2 decimal places

# Solution
meters = f'Meters: {distance/m:.0f}'
kilometers = f'Kilometers: {distance/km:.0f}'
miles = f'Miles: {distance/mi:.2f}'
nautical_miles = f'Nautical Miles: {distance/NM:.3f}'
all_units = f'All: km: {distance/km:.0f}, mi: {distance/mi:.1f}, NM: {distance/NM:.2f}'
