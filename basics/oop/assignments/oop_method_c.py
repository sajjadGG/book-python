"""
* Assignment: OOP Method Call
* Complexity: easy
* Lines of code: 2 lines
* Time: 2 min

English:
    1. Use data from "Given" section (see below)
    2. Create instance of `Stats` class
    3. Iterate over `DATA` skipping header
    4. Separate features from label
    5. Call `mean()` method of `Stats` class passing list of features as an argument
    6. Define `result: list[float]` with list of means from each row
    7. Compare result with "Tests" section (see below)

Polish:
    1. Użyj danych z sekcji "Given" (patrz poniżej)
    2. Stwórz instancję klasy `Stats`
    3. Iteruj po `DATA` pomijając nagłówek
    4. Rozdziel cechy od etykiety
    5. Wywołuj metodę `mean()` klasy `Stats` przekazując listę features jako argument
    6. Zdefiniuj `result: list[float]` z listą średnich każdego z wierszy
    7. Porównaj wyniki z sekcją "Tests" (patrz poniżej)

Hints:
    * `round()`

Tests:
    >>> assert type(result) is list
    >>> assert all(type(x) is float for x in result)
    >>> result
    [3.9, 2.5, 3.5, 4.1, 3.9, 2.4]
"""


# Given
DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


class Stats:
    def mean(self, data):
        result = sum(data) / len(data)
        return round(result, 1)


# Solution
stats = Stats()
result = [stats.mean(X) for *X, y in DATA[1:]]
