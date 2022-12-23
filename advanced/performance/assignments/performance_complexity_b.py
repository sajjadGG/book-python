"""
* Assignment: Performance Compexity UniqueKeys
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 5 min

English:
    1. Collect unique keys from all rows in one sequence `result`
    2. Run doctests - all must succeed

Polish:
    1. Zbierz unikalne klucze z wszystkich wierszy w jednej sekwencji `result`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `row.keys()`
    * Compare solutions with :ref:`Micro-benchmarking use case`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result is not Ellipsis
    True
    >>> type(result) in (set, list, tuple, frozenset)
    True
    >>> sorted(result)
    ['Petal length', 'Petal width', 'Sepal length', 'Sepal width', 'Species']
"""

DATA = [
    {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
    {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
    {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
    {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
    {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
    {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
]

# Unique keys from DATA dicts
# type: set[str]
result = ...

# Solution
result = set()

for row in DATA:
    result.update(row.keys())


"""
# 1.86 µs ± 290 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = set()
for row in DATA:
    for key in row.keys():
        result.add(key)


# 1.37 µs ± 208 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = set()
for row in DATA:
    result.update(row.keys())


# 1.91 µs ± 334 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = list()
for row in DATA:
    for key in row.keys():
        if key not in result:
            result.append(key)


# 2.15 µs ± 277 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = list()
for row in DATA:
    for key in row.keys():
        if key not in result:
            result.append(key)
result = set(result)


# 2.19 µs ± 306 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = list()
for row in DATA:
    for key in row.keys():
        result.append(key)
result = set(result)


# 1.52 µs ± 192 ns per loop (mean ± std. dev. of 10 runs, 10000 loops each)
# %%timeit -r 10 -n 10_000
result = list()
for row in DATA:
    result.extend(row.keys())
result = set(result)
"""
