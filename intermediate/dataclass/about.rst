Dataclass About
===============
* Used for easier class definition
* Since Python 3.7: :pep:`557` -- Data Classes


Syntax
------
* This are not static fields!
* Dataclasses require Type Annotations

>>> class Point:
...     def __init__(self, x, y, z=0):
...         self.x = x
...         self.y = y
...         self.z = z

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class Point:
...     x: int
...     y: int
...     z: int = 0


Use Case - 0x01
---------------
>>> from dataclasses import dataclass
>>> from itertools import starmap

>>> DATA = [
...     ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...     (5.8, 2.7, 5.1, 1.9, 'virginica'),
...     (5.1, 3.5, 1.4, 0.2, 'setosa'),
...     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...     (6.3, 2.9, 5.6, 1.8, 'virginica'),
...     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...     (4.7, 3.2, 1.3, 0.2, 'setosa'),
... ]

>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str

>>> flowers = starmap(Iris, DATA[1:])
>>> list(flowers)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
 Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
 Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
 Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
 Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
 Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa')]

>>> flowers = [Iris(*row) for row in DATA[1:]]
>>> print(flowers)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
 Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
 Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
 Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
 Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
 Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa')]
