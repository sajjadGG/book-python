"""
* Assignment: Function Scope Global
* Filename: function_scope_global.py
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Use data from "Given" section (see below)
    2. Define in global scope `SELECT: set[str]` with values: `'setosa', 'versicolor'`
    3. Define function `sumif(features, label)`
    4. Function sums `features`, only when `label` is in `SELECT`
    5. When `label` is not in `select` return `0` (zero)
    6. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Zdefiniuj w przestrzeni globalnej `SELECT: set[str]` z wartościami: `'setosa', 'versicolor'`
    3. Zdefiniuj funkcję `sumif(features, label)`
    4. Funkcja sumuje `features`, tylko gdy `label` jest w `SELECT`
    5. Gdy `label` nie występuje w `select` zwróć `0` (zero)
    6. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Tests:
    >>> from inspect import isfunction
    >>> isfunction(sumif)
    True
    >>> sum(sumif(X,y) for *X, y in DATA[1:])
    49.1
"""


# Given
DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa')]


# Solution
SELECT = {'setosa', 'versicolor'}


def sumif(features, label):
    if label in SELECT:
        return sum(features)
    else:
        return 0
