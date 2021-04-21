"""
* Assignment: Exception Catch Finally
* Status: required
* Complexity: easy
* Lines of code: 8 lines
* Time: 8 min

English:
    1. Convert value passed to the function as a `degrees: int`
    2. If conversion fails, raise exception `TypeError` with message:
        'Invalid type, expected int or float'
    3. Use `finally` to print `degrees` value
    4. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
    5. Run doctests - all must succeed

Polish:
    1. Przekonwertuj wartość przekazaną do funckji jako `degrees: int`
    2. Jeżeli konwersja się nie powiedzie to podnieś wyjątek `TypeError`
        z komunikatem 'Invalid type, expected int or float'
    3. Użyj `finally` do wypisania wartości `degrees`
    4. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> check(1)
    1
    >>> check(180)
    180
    >>> check(1.0)
    1
    >>> check('one')
    Traceback (most recent call last):
    TypeError: Invalid type, expected int or float
"""

def check(value):
    ...


# Solution
def check(degrees):
    try:
        degrees = int(degrees)
    except ValueError:
        raise TypeError('Invalid type, expected int or float')
    finally:
        print(degrees)
