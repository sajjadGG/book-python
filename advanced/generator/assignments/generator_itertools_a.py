"""
* Assignment: Generator Itertools Count
* Complexity: medium
* Lines of code: 13 lines
* Time: 13 min

English:
    1. `Label encoder` algorithm encodes labels (str) to numbers (int).
       Each unique label will assign autoincremented numbers.
       example: {'virginica': 0, 'setosa': 1, 'versicolor': 2}
    2. Create two implementations of this algorighm:
       a. labelencoder_i() - using variable `i` and `i += 1`
       b. labelencoder_count() - using `itertools.count`
    3. Function resut must be `dict[str,int]`

Polish:
    1. Algorytm `label_encoder` koduje etykiety (str) do liczb (int).
       Kolejnym wystąpieniom unikalnych etykiet przyporządkowuje liczby.
       przykład: {'virginica': 0, 'setosa': 1, 'versicolor': 2}
    2. Stwórz dwie implementacje algorytmu:
       a. labelencoder_i() - z wykorzystaniem zmiennej `i` oraz `i += 1`
       b. labelencoder_count() - z wykorzystaniem `itertools.count`
    3. Wynik funkcji ma być `dict[str,int]`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction, isgeneratorfunction

    >>> assert isfunction(labelencoder_i)
    >>> assert isfunction(labelencoder_count)

    >>> labelencoder_i(DATA)
    {'virginica': 0, 'setosa': 1, 'versicolor': 2}

    >>> labelencoder_count(DATA)
    {'virginica': 0, 'setosa': 1, 'versicolor': 2}
"""
from itertools import count


DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


def labelencoder_i(data):
    ...


def labelencoder_count(data):
    ...


# Solution
def labelencoder_i(data):
    result = {}
    i = 0
    for *_, species in data[1:]:
        if species not in result:
            result[species] = i
            i += 1
    return result


def labelencoder_count(data):
    result = {}
    i = count()
    for *_, species in data[1:]:
        if species not in result:
            result[species] = next(i)
    return result
