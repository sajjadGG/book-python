Comprehension Good Practices
============================


Microbenchmark
--------------
>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = []
... for x in range(0,5):
...     result.append(x)
...
457 ns ± 69.4 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = [x for x in range(0,5)]
...
411 ns ± 76.6 ns per loop (mean ± std. dev. of 1000 runs, 1000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = [x for x in range(0,50)]
...
1.45 µs ± 181 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = []
... for x in range(0,50):
...     result.append(x)
...
2.79 µs ± 306 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = [x for x in range(0,500)]
...
14.1 µs ± 1.02 µs per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... result = []
... for x in range(0,500):
...     result.append(x)
...
28.5 µs ± 2.23 µs per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Conclusion:

In this case comprehensions are twice as fast as regular loops (:pep:`20`).


Performance
-----------
Setup:

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... all(c > 1.0 for *a,b in DATA[1:] for c in a if isinstance(c, float))
...
1.41 µs ± 180 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... all(x > 1.0 for *X,y in DATA[1:] for x in X if isinstance(x, float))
...
1.36 µs ± 167 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... all(observation > 1.0 for *features, label in DATA[1:] for observation in features if isinstance(observation, float))
...
1.38 µs ± 162 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... all(x > 1.0
...     for *X,y in DATA[1:]
...     for x in X
...     if isinstance(x, float))
...
1.4 µs ± 179 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> # doctest: +SKIP
... %%timeit -r 1000 -n 1000
... all(observation > 1.0
...     for *features, label in DATA[1:]
...     for observation in features
...     if isinstance(observation, float))
...
1.39 µs ± 192 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

Conclusion:

No evidence, that multiline comprehension with long variable names are slower.
They are far more readable. "Readability counts" (:pep:`20`)



Performance
-----------
.. todo:: cleanup

Setup:

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
... ]

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = []
... for row in DATA[1:]:
...     for value in row:
...         if isinstance(value, float):
...             result.append(value >= 1.0)
... result = all(result)
5.24 µs ± 591 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = True
... for row in DATA[1:]:
...     for value in row:
...         if isinstance(value, float):
...             if value < 1.0:
...                 result = False
...                 break
3.49 µs ± 596 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = all(value >= 1.0
...              for row in DATA[1:]
...              for value in row
...              if isinstance(value, float))
1.55 µs ± 436 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = all(value >= 1.0 for row in DATA[1:] for value in row if isinstance(value, float))
1.51 µs ± 396 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = all(y >= 1.0 for x in DATA[1:] for y in x if isinstance(y, float))
1.53 µs ± 433 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -n 1000 -r 1000  # doctest: +SKIP
... result = all(x >= 1.0 for X in DATA[1:] for x in X if isinstance(x, float))
1.57 µs ± 437 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)
