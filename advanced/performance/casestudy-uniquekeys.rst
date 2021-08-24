Case Study: Unique Keys
=======================


Prepare
-------
Setup code used for all examples:

>>> DATA = [
...     {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
...     {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
...     {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
...     {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
...     {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
...     {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'}]


List Append If
--------------
Append if object not in the list:

>>> #%%timeit -r 1000 -n 10_000
>>> result = list()
>>> for row in DATA:
...     for key in row.keys():
...         if key not in result:
...             result.append(key)
2.16 µs ± 26.5 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


List Append
-----------
Append to list and deduplicate at the end:

>>> #%%timeit -r 1000 -n 10_000
>>> result = list()
... for row in DATA:
...     for key in row.keys():
...         result.append(key)
>>> set(result)
2.5 µs ± 32.9 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Add
-------
>>> ##%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     for key in row.keys():
...         result.add(key)
2.12 µs ± 32.4 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)

Set Update
----------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(row.keys())
1.57 µs ± 26.7 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension
-----------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set(key
...     for record in DATA
...         for key in record.keys())
2.06 µs ± 79.7 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension Add
---------------------
* Add to Set Comprehension.
* Code appends generator object not values, this is why it is so fast!:

>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> result.add(key
...     for record in DATA
...        for key in record.keys())
447 ns ± 9.52 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)

Set Comprehension Update
------------------------
Update Set Comprehension:

>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> result.update(tuple(x.keys()) for x in DATA)
2.06 µs ± 45.9 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension Update
------------------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(row)


Set Comprehension Update Tuple
------------------------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(tuple(row))
2.09 µs ± 16.1 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension Update List
-----------------------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(list(row))
2.33 µs ± 30.2 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)


Set Comprehension Update Set
----------------------------
>>> #%%timeit -r 1000 -n 10_000
>>> result = set()
>>> for row in DATA:
...     result.update(set(row))
1.71 µs ± 54 ns per loop (mean ± std. dev. of 1000 runs, 10000 loops each)
