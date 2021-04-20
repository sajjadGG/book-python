"""
* Assignment: Exception Assert Version
* Status: required
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Check value passed to a `check` function
        a. Check if `version` is greater or equal to `REQUIRED_VERSION`
        b. If not, raise exception with message 'Python 3.7+ required'
    2. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
        c. Use `assert` kyword
    3. Run doctests - all must succeed

Polish:
    1. Sprawdź poprawność wartości przekazanej do funckji `check`
        a. Sprawdź czy `version` jest większe lub równe `REQUIRED_VERSION`
        b. Jeżeli nie, podnieś wyjątek z komunikatem 'Python 3.7+ required'
    2. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
        c. Użyj słowa kluczowego `assert`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> check( (3,6,0) )
    Traceback (most recent call last):
    AssertionError: Python 3.7+ required
    >>> check( (3,6,12) )
    Traceback (most recent call last):
    AssertionError: Python 3.7+ required
    >>> check( (3,7) )
    >>> check( (3,7,0) )
    >>> check( (3,7,1) )
    >>> check( (3,8) )
    >>> check( (3,9) )
    >>> check( (3,10) )
"""

REQUIRED_VERSION = (3, 7)


def check(version):
    ...


# Solution
def check(version):
    assert version >= REQUIRED_VERSION, 'Python 3.7+ required'
