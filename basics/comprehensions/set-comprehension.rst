Comprehension Set
=================


Syntax
------
``set`` comprehension approach to applying function to elements:

>>> {x+10 for x in range(0, 5)}
{10, 11, 12, 13, 14}

>>> set(x+10 for x in range(0, 5))
{10, 11, 12, 13, 14}


Use Case - Unique
-----------------
>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
...     (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> result = {row[-1] for row in DATA[1:]}
>>>
>>> sorted(result)
['setosa', 'versicolor', 'virginica']


Assignments
-----------
.. todo:: Create Assignments
