"""
* Assignment: Type None
* Complexity: easy
* Lines of code: 5 lines
* Time: 3 min

English:
    1. Use data from "Given" section (see below)
    2. What you need to put in expressions to get the expected outcome?
    3. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Co należy podstawić w wyrażeniach aby otrzymać wartość oczekiwaną?
    3. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> bool(result_a)
    True
    >>> bool(result_b)
    False
    >>> bool(result_c)
    True
    >>> bool(result_d)
    False
    >>> bool(result_e)
    False
"""

# Given
a = ...  # bool True
b = ...  # bool False
c = ...  # bool True
d = ...  # bool False
e = ...  # bool False

# Do not modify following lines
result_a = a is None
result_b = b is not None
result_c = bool(bool(c) is not bool(c)) == False
result_d = bool(bool(d) is not bool(d)) == False and bool(d)
result_e = (bool(bool(e) is not bool(e)) == False and bool(e)) and (e is not None)

# Solution
a = None  # bool True
b = None  # bool False
c = None  # bool True
d = None  # bool False
e = None  # bool False

result_a = a is None
result_b = b is not None
result_c = bool(bool(c) is not bool(c)) == False
result_d = bool(bool(d) is not bool(d)) == False and bool(d)
result_e = (bool(bool(e) is not bool(e)) == False and bool(e)) and (e is not None)
