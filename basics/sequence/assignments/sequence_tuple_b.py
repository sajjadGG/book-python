"""
* Assignment: Sequence Tuple Select
* Complexity: easy
* Lines of code: 1 lines
* Time: 5 min

English:
    1. Use data from "Given" section (see below)
    2. Create a `tuple` representing all species
    3. To convert table use multiline select with `alt` key in your IDE
    4. Do not use `slice`, `getitem`, `for`, `while` or any other control-flow statement
    5. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz `tuple` z nazwami gatunków
    3. Do konwersji tabelki wykorzystaj zaznaczanie wielu linijek za pomocą klawisza `alt` w Twoim IDE
    4. Nie używaj `slice`, `getitem`, `for`, `while` lub jakiejkolwiek innej instrukcji sterującej
    5. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `ALT` + `left mouse button` = multiple select
    * `ALT` + `SHIFT` + `left mouse button drag` = vertical selection

Tests:
    >>> import sys
    >>> sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, 'Assignment solution must be in `result` instead of ... (Ellipsis)'
    >>> assert type(result) is tuple, 'Variable `result` has invalid type, should be tuple'
    >>> assert all(type(x) is str for x in result), 'All elements in result should be str'
    >>> assert len(result) == 5, 'Variable `result` length should be 5'
    >>> assert result.count('virginica') == 2, 'Result should have 2 elements of virginica'
    >>> assert result.count('setosa') == 1, 'Result should have 1 elements of setosa'
    >>> assert result.count('versicolor') == 2, 'Result should have 2 elements of versicolor'

    >>> ('sepal_length' not in result
    ...  and 'sepal_width' not in result
    ...  and 'petal_length' not in result
    ...  and 'petal_width' not in result
    ...  and 'species' not in result)
    True

"""

# Given
DATA = [
    'sepal_length,sepal_width,petal_length,petal_width,species',
    '5.8,2.7,5.1,1.9,virginica',
    '5.1,3.5,1.4,0.2,setosa',
    '5.7,2.8,4.1,1.3,versicolor',
    '6.3,2.9,5.6,1.8,virginica',
    '6.4,3.2,4.5,1.5,versicolor',
]

result = ...  # define a tuple from header - DATA row with index 0

# Solution
result = ('virginica', 'setosa', 'versicolor', 'virginica', 'versicolor')
