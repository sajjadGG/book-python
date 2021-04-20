"""
* Assignment: Exception Catch Except
* Status: required
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Convert value passed to the `check` function as a `float`
    2. If conversion fails then print 'Invalid value'
    3. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj wartośc przekazaną do funckji `check` jako `float`
    2. Jeżeli konwersja się nie powiedzie to wypisz 'Invalid value'
    3. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> check('1')
    >>> check('1.0')
    >>> check('1,0')
    Invalid value
"""

def check(value):
    ...


# Solution
def check(value):
    try:
        float(value)
    except ValueError:
        print('Invalid value')
