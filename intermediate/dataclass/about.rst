Dataclass About
===============


Rationale
---------
* Used for easier class definition
* Since Python 3.7: :pep:`557` -- Data Classes
* Backported to Python 3.6 via ``python3 -m pip install dataclasses``


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
>>> @dataclass
... class Point:
...     x: int
...     y: int
...     z: int = 0


Under the hood
--------------
Your code:

>>> from dataclasses import dataclass
>>>
>>>
>>> @dataclass
... class ShoppingCartItem:
...     name: str
...     unit_price: float
...     quantity: int = 0
...
...     def total_cost(self) -> float:
...         return self.unit_price * self.quantity

Dataclass will generate:

>>> class ShoppingCartItem:
...     name: str
...     unit_price: float
...     quantity: int
...
...     def total_cost(self) -> float:
...         return self.unit_price * self.quantity
...
...     ## All code below is added by dataclass
...
...     def __init__(self, name: str, unit_price: float,
...                  quantity: int = 0) -> None:
...         self.name = name
...         self.unit_price = unit_price
...         self.quantity = quantity
...
...     def __repr__(self):
...         return f'ShoppingCartItem(name={self.name!r}, ' \
...                f'unit_price={self.unit_price!r}, ' \
...                f'quantity={self.quantity!r})'
...
...     def __eq__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 == (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __ne__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 != (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __lt__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                  < (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __le__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 <= (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __gt__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                  > (other.name, other.unit_price, other.quantity)
...         return NotImplemented
...
...     def __ge__(self, other):
...         if other.__class__ is self.__class__:
...             return (self.name, self.unit_price, self.quantity) \
...                 >= (other.name, other.unit_price, other.quantity)
...         return NotImplemented


Use Cases
---------
>>> from dataclasses import dataclass
>>>
>>>
>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa')]
>>>
>>>
>>> @dataclass
... class Iris:
...     sepal_length: float
...     sepal_width: float
...     petal_length: float
...     petal_width: float
...     species: str
>>>
>>>
>>> flowers = list(Iris(*row) for row in DATA[1:])
>>> print(flowers)  # doctest: +NORMALIZE_WHITESPACE
[Iris(sepal_length=5.8, sepal_width=2.7, petal_length=5.1, petal_width=1.9, species='virginica'),
 Iris(sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species='setosa'),
 Iris(sepal_length=5.7, sepal_width=2.8, petal_length=4.1, petal_width=1.3, species='versicolor'),
 Iris(sepal_length=6.3, sepal_width=2.9, petal_length=5.6, petal_width=1.8, species='virginica'),
 Iris(sepal_length=6.4, sepal_width=3.2, petal_length=4.5, petal_width=1.5, species='versicolor'),
 Iris(sepal_length=4.7, sepal_width=3.2, petal_length=1.3, petal_width=0.2, species='setosa')]
