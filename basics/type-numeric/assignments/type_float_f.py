"""
* Assignment: Type Float Pressure
* Required: no
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Operational pressure of EMU spacesuit: 4.3 PSI
    2. Operational pressure of ORLAN spacesuit: 40 kPa
    3. Calculate operational pressure in hPa for EMU
    4. Calculate operational pressure in hPa for Orlan
    5. Results round to one decimal place
    6. Run doctests - all must succeed

Polish:
    1. Ciśnienie operacyjne skafandra kosmicznego EMU (NASA): 4.3 PSI
    2. Ciśnienie operacyjne skafandra kosmicznego ORLAN (Roscosmos): 40 kPa
    3. Oblicz ciśnienie operacyjne skafandra EMU w hPa
    4. Oblicz ciśnienie operacyjne skafandra Orlan w hPa
    5. Wynik zaokrąglij do jednego miejsca po przecinku
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert emu is not Ellipsis, 'Assignment solution must be in `emu` instead of ... (Ellipsis)'
    >>> assert orlan is not Ellipsis, 'Assignment solution must be in `orlan` instead of ... (Ellipsis)'
    >>> assert type(emu) is float, 'Variable `emu` has invalid type, should be float'
    >>> assert type(orlan) is float, 'Variable `orlan` has invalid type, should be float'

    >>> orlan
    400.0
    >>> emu
    296.5
"""

Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa
psi = 6894.757 * Pa

emu = ...  # float: 4.3 pounds per square inch in hectopascals, round to one decimal place
orlan = ...  # float: 40 kilopascals in hectopascals, round to one decimal place

# Solution
emu = round(4.3*psi/hPa, 1)
orlan = round(40*kPa/hPa, 1)
