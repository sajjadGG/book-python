"""
* Assignment: Loop Comprehension Split
* Required: no
* Complexity: medium
* Lines of code: 9 lines
* Time: 13 min

English:
    1. Using List Comprehension split `DATA` into:
        a. `features_train: list[tuple]` - 60% of first features in `DATA`
        b. `features_test: list[tuple]` - 40% of last features in `DATA`
        c. `labels_train: list[str]` - 60% of first labels in `DATA`
        d. `labels_test: list[str]` - 40% of last labels in `DATA`
    2. In order to do so, calculate pivot point:
        a. length of `DATA` times given percent (60% = 0.6)
        b. remember, that slice indicies must be `int`, not `float`
        c. for example: if dataset has 10 rows, then 6 rows will be for
        training, and 4 rows for test
    3. Run doctests - all must succeed

Polish:
    1. Używając List Comprehension podziel `DATA` na:
        a. `features_train: list[tuple]` - 60% pierwszych features w `DATA`
        b. `features_test: list[tuple]` - 40% ostatnich features w `DATA`
        c. `labels_train: list[str]` - 60% pierwszych labels w `DATA`
        d. `labels_test: list[str]` - 40% ostatnich labels w `DATA`
    2. Aby to zrobić, wylicz punkt podziału:
        a. długość `DATA` razy zadany procent (60% = 0.6)
        b. pamiętaj, że indeksy slice muszą być `int` a nie `float`
        c. na przykład: if zbiór danych ma 10 wierszy, to 6 wierszy będzie
        do treningu, a 4 do testów
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(features_train) is list, \
    'make sure features_train is a list'

    >>> assert type(features_test) is list, \
    'make sure features_test is a list'

    >>> assert type(labels_train) is list, \
    'make sure labels_train is a list'

    >>> assert type(labels_test) is list, \
    'make sure labels_test is a list'

    >>> assert all(type(x) is tuple for x in features_train), \
    'all elements in features_train should be tuple'

    >>> assert all(type(x) is tuple for x in features_test), \
    'all elements in features_test should be tuple'

    >>> assert all(type(x) is str for x in labels_train), \
    'all elements in labels_train should be str'

    >>> assert all(type(x) is str for x in labels_test), \
    'all elements in labels_test should be str'

    >>> features_train  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9),
     (5.1, 3.5, 1.4, 0.2),
     (5.7, 2.8, 4.1, 1.3),
     (6.3, 2.9, 5.6, 1.8),
     (6.4, 3.2, 4.5, 1.5),
     (4.7, 3.2, 1.3, 0.2)]

    >>> features_test  # doctest: +NORMALIZE_WHITESPACE
    [(7.0, 3.2, 4.7, 1.4),
     (7.6, 3.0, 6.6, 2.1),
     (4.9, 3.0, 1.4, 0.2),
     (4.9, 2.5, 4.5, 1.7)]

    >>> labels_train
    ['virginica', 'setosa', 'versicolor', 'virginica', 'versicolor', 'setosa']

    >>> labels_test
    ['versicolor', 'virginica', 'setosa', 'virginica']
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
]

ratio = 0.6
header, *data = DATA
split = int(len(data) * ratio)

# Solution
features_train = [tuple(X) for *X,y in data[:split]]
features_test = [tuple(X) for *X,y in data[split:]]
labels_train = [y for *X,y in data[:split]]
labels_test = [y for *X,y in data[split:]]

# Alternative Solution
features = [tuple(X) for *X,y in data]
labels = [y for *X,y in data]
features_train = features[:split]
features_test = features[split:]
labels_train = labels[:split]
labels_test = labels[split:]

# Alternative Solution
train = data[:split]
test = data[split:]
features_train = [tuple(X) for *X,y in train]
features_test = [tuple(X) for *X,y in test]
labels_train = [y for *X,y in train]
labels_test = [y for *X,y in test]


# memory complexity - How memory consuming is the task
# computational complexity - How many computations
# cyclomatic complexity - How many loops are in the code, how nested they are
# cognitive complexity - How hard it to understand code (complex structures, bool logic)


"""
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
...     (7.6, 3.0, 6.6, 2.1, 'virginica'),
...     (4.9, 3.0, 1.4, 0.2, 'setosa'),
...     (4.9, 2.5, 4.5, 1.7, 'virginica'),
... ]
... 
... ratio = 0.6
... header, *data = DATA
... split = int(len(data) * ratio)

>>> %%timeit -r 10 -n 1000
... features_train = [tuple(X) for *X,y in data[:split]]
... features_test = [tuple(X) for *X,y in data[split:]]
... labels_train = [y for *X,y in data[:split]]
... labels_test = [y for *X,y in data[split:]]
5.63 µs ± 475 ns per loop (mean ± std. dev. of 10 runs, 1000 loops each)

>>> %%timeit -r 10 -n 1000
... features = [tuple(X) for *X,y in data]
... labels = [y for *X,y in data]
... features_train = features[:split]
... features_test = features[split:]
... labels_train = labels[:split]
... labels_test = labels[split:]
4.76 µs ± 440 ns per loop (mean ± std. dev. of 10 runs, 1000 loops each)

>>> %%timeit -r 10 -n 1000
... train = data[:split]
... test = data[split:]
... features_train = [tuple(X) for *X,y in train]
... features_test = [tuple(X) for *X,y in test]
... labels_train = [y for *X,y in train]
... labels_test = [y for *X,y in test]
5 µs ± 449 ns per loop (mean ± std. dev. of 10 runs, 1000 loops each)
"""


"""
DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica'),
]

ratio = 0.6
header, *data = DATA
split = int(len(data) * ratio)

>>> %%timeit -r 10 -n 1000
... features_train = [tuple(X) for *X,y in data[:split]]
... features_test = [tuple(X) for *X,y in data[split:]]
... labels_train = [y for *X,y in data[:split]]
... labels_test = [y for *X,y in data[split:]]
45.7 µs ± 5.79 µs per loop (mean ± std. dev. of 10 runs, 1000 loops each)

>>> %%timeit -r 10 -n 1000
... features = [tuple(X) for *X,y in data]
... labels = [y for *X,y in data]
... features_train = features[:split]
... features_test = features[split:]
... labels_train = labels[:split]
... labels_test = labels[split:]
45.5 µs ± 2.92 µs per loop (mean ± std. dev. of 10 runs, 1000 loops each)

>>> %%timeit -r 10 -n 1000
... train = data[:split]
... test = data[split:]
... features_train = [tuple(X) for *X,y in train]
... features_test = [tuple(X) for *X,y in test]
... labels_train = [y for *X,y in train]
... labels_test = [y for *X,y in test]
44.9 µs ± 5.51 µs per loop (mean ± std. dev. of 10 runs, 1000 loops each)
"""
