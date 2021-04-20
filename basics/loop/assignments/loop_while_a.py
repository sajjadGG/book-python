"""
* Assignment: Loop While to Float
* Status: required
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create `result: list[float]`
    3. Use `while` to iterate over `DATA`
    4. Convert current elements of `DATA` to `float`
    5. Converted value append to `result`
    6. Run doctests - all must succeed

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `result: list[float]`
    3. Użyj `while` do iterowania po `DATA`
    4. Przekonwertuj obecny element `DATA` do `float`
    5. Przekonwertowaną wartość dodaj na koniec `result`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `Stop` or `Ctrl+C` kills infinite loop

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> type(result)
    <class 'list'>

    >>> assert all(type(x) is float for x in result)

    >>> result
    [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]
"""

# Given
DATA = (2, 3, 3.5, 4, 4.5, 5)
result = ...  # list[float]: values from DATA converted to float

# Solution
result = []
i = 0

while i < len(DATA):
    value = float(DATA[i])
    result.append(value)
    i += 1
