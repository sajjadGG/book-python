"""
* Assignment: Sequence GetItem Select
* Required: yes
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Non-functional requirements:
        a. Use only indexes (`getitem`)
        b. Do not use `str.split()`, `slice`, `for`, `while` or any other control-flow statement
        c. All tests must pass
    2. Write header (row with index 0) to `header: tuple` variable
    3. Create `result: list`
    4. Select row at index 2, convert it to `list` and add to `result`
    5. Select row at index 4, convert it to `tuple` and add to `result`
    6. Select row at index -2, convert it to `set` and add to `result`
    7. Select row at index -4, convert it to `frozenset` and add to `result`
    8. Append to `result`: empty `list`, empty `tuple`, empty `set` and empty `frozenset`
    9. Run doctests - all must succeed

Polish:
    1. Wymagania niefunkcjonalne:
        a. Korzystaj tylko z indeksów (`getitem`)
        b. Nie używaj `str.split()`, `slice`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej
        c. Wszystkie testy muszą przejść
    2. Zapisz nagłówek (wiersz o indeksie 0) do zmiennej `header: tuple`
    3. Stwórz `result: list`
    4. Wybierz wiersz o indeksie 2, przekonwertuj go do `list` i dodaj do `result`
    5. Wybierz wiersz o indeksie 4, przekonwertuj go do `tuple` i dodaj do `result`
    6. Wybierz wiersz o indeksie -4, przekonwertuj go do `set` i dodaj do `result`
    7. Wybierz wiersz o indeksie -2, przekonwertuj go do `frozenset` i dodaj do `result`
    8. Dodaj na koniec `result`: pustą `list`, pustą `tuple`, pusty `set`, pusty `frozenset`
    9. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(header) is tuple, 'Variable `header` has invalid type, should be tuple'
    >>> assert type(result) is list, 'Variable `result` has invalid type, should be list'
    >>> assert len(result) == 8, 'Variable `result` length should be 8'

    >>> ('sepal_length' not in result
    ...  and 'sepal_width' not in result
    ...  and 'petal_length' not in result
    ...  and 'petal_width' not in result
    ...  and 'species' not in result)
    True

    >>> header
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')

    >>> [5.1, 3.5, 1.4, 0.2, 'setosa'] in result
    True
    >>> (6.3, 2.9, 5.6, 1.8, 'virginica') in result
    True
    >>> {1.3, 2.8, 4.1, 5.7, 'versicolor'} in result
    True
    >>> frozenset({1.5, 3.2, 4.5, 6.4, 'versicolor'}) in result
    True
    >>> list() in result
    True
    >>> tuple() in result
    True
    >>> set() in result
    True
    >>> frozenset() in result
    True
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]

header = ...  # tuple[str]: from row at index 0
result = ...  # list[list|tuple|set|frozenset]: empty list

result  # append list from DATA at index 2
result  # append tuple from DATA at index 4
result  # append set from DATA at index -4
result  # append frozenset DATA at index -2

result  # append empty list
result  # append empty tuple
result  # append empty set
result  # append empty frozenset

# Solution
header = DATA[0]
result = []

result.append(list(DATA[2]))
result.append(tuple(DATA[4]))
result.append(set(DATA[-4]))
result.append(frozenset(DATA[-2]))

result.append(list())
result.append(tuple())
result.append(set())
result.append(frozenset())
