"""
* Assignment: Type Float Volume
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Bottle volume is 20 Fl Oz
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Compare result with "Tests" section (see below)

Polish:
    1. Objętość butelki wynosi 20 Fl Oz
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> type(volume)
    <class 'float'>
    >>> imperial
    20.0
    >>> metric
    0.5914688
"""

# Given
liter = 1
floz = 0.02957344 * liter

volume: float  # Bottle volume is 20 Fl Oz
imperial: float
metric: float

# Solution
volume = 20 * floz
imperial = volume / floz
metric = volume / liter
