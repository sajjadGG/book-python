"""
* Assignment: Type Int Sub
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    2. Zero Kelvin (absolute) is equal to -273.15 Celsius degrees
    3. For calculation use round number -273 (0K = -273°C)
    4. How many Celsius degrees has average temperatures at surface [1]:
        a. Lunar day: 453 K
        b. Lunar night: 93 K
    5. Run doctests - all must succeed

Polish:
    1. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    2. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza
    3. W zadaniu przyjmij równe -273°C (0K = -273°C)
    4. Ile stopni Celsiusza wynoszą średnie temperatury powierzchni [1]:
        a. Księżyca w dzień: 453 K
        b. Księżyca w nocy: 93 K
    5. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Centro de Astrobiología (CSIC-INTA).
        Rover Environmental Monitoring Station, Mars Science Laboratory (NASA).
        Year: 2019.
        Retrieved: 2019-08-06.
        URL: http://cab.inta-csic.es/rems/marsweather.html

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert moon_day is not Ellipsis, 'Assignment solution must be in `moon_day` instead of ... (Ellipsis)'
    >>> assert moon_night is not Ellipsis, 'Assignment solution must be in `moon_night` instead of ... (Ellipsis)'
    >>> assert type(moon_day) is int, 'Variable `moon_day` has invalid type, should be int'
    >>> assert type(moon_night) is int, 'Variable `moon_night` has invalid type, should be int'

    >>> moon_day
    180
    >>> moon_night
    -180
"""

Celsius = 273
Kelvin = 1

moon_day = ...  # int: 453 Kelvins in Celsius
moon_night = ...  # int: 93 Kelvins in Celsius

# Solution
moon_day = 453*Kelvin - Celsius
moon_night = 93*Kelvin - Celsius
