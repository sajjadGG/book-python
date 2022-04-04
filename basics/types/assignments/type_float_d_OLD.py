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

    >>> assert meters is not Ellipsis, \
    'Assign your result to variable `meters`'
    >>> assert kilometers is not Ellipsis, \
    'Assign your result to variable `kilometers`'
    >>> assert miles is not Ellipsis, \
    'Assign your result to variable `miles`'
    >>> assert nautical_miles is not Ellipsis, \
    'Assign your result to variable `nautical_miles`'
    >>> assert all_units is not Ellipsis, \
    'Assign your result to variable `all_units`'
    >>> assert type(meters) is str, \
    'Variable `meters` has invalid type, should be str'
    >>> assert type(kilometers) is str, \
    'Variable `kilometers` has invalid type, should be str'
    >>> assert type(miles) is str, \
    'Variable `miles` has invalid type, should be str'
    >>> assert type(nautical_miles) is str, \
    'Variable `nautical_miles` has invalid type, should be str'
    >>> assert type(all_units) is str, \
    'Variable `all_units` has invalid type, should be str'

    >>> meters
    'Meters: 1337'
    >>> kilometers
    'Kilometers: 1'
    >>> miles
    'Miles: 0.83'
    >>> nautical_miles
    'Nautical Miles: 0.722'
    >>> all_units
    'km: 1, mi: 0.8, NM: 0.72'
"""

m = 1
km = 1000 * m
mi = 1609.344 * m
NM = 1852 * m

distance = 1337 * m
distance_m = distance / m
distance_km = distance / km
distance_mi = distance / mi
distance_NM = distance / NM

# distance in meters 0 decimal places
# type: str
meters = f'Meters: {...}'

# distance in kilometers with 0 decimal places
# type: str
kilometers = f'Kilometers: {...}'

# distance in miles with 2 decimal places
# type: str
miles = f'Miles: {...}'

# distance in nautical miles with 3 decimal places
# type: str
nautical_miles = f'Nautical Miles: {...}'

# distance in km, mi, NM with 0, 1, 2 decimal places
# type: str
all_units = (f'km: {...}, '
             f'mi: {...}, '
             f'NM: {...}')

# Solution
meters = f'Meters: {distance_m:.0f}'
kilometers = f'Kilometers: {distance_km:.0f}'
miles = f'Miles: {distance_mi:.2f}'
nautical_miles = f'Nautical Miles: {distance_NM:.3f}'
all_units = (f'km: {distance_km:.0f}, '
             f'mi: {distance_mi:.1f}, '
             f'NM: {distance_NM:.2f}')
