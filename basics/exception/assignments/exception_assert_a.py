"""
* Assignment: Exception Assert Version
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. Check value passed to a `check` function
        a. Check if `version` is greater or equal to `REQUIRED_VERSION`
        b. If not, raise exception with message 'Python 3.7+ required'
    3. Non-functional requirements
        a. Write solution inside `check` function
        b. Mind the indentation level
        c. Use `assert` kyword
    4. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Sprawdź poprawność wartości przekazanej do funckji `check`
        a. Sprawdź czy `version` jest większe lub równe `REQUIRED_VERSION`
        b. Jeżeli nie, podnieś wyjątek z komunikatem 'Python 3.7+ required'
    3. Wymagania niefunkcjonalne
        a. Rozwiązanie zapisz wewnątrz funkcji `check`
        b. Zwróć uwagę na poziom wcięć
        c. Użyj słowa kluczowego `assert`
    4. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

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

# Given
REQUIRED_VERSION = (3, 7)


def check(version):
    ...


# Solution
def check(version):
    assert version >= REQUIRED_VERSION, 'Python 3.7+ required'
