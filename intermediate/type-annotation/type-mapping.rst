Type Annotation Mapping
=======================
* Before Python 3.9 you need ``from typing import Dict``
* Since Python 3.9: :pep:`585` -- Type Hinting Generics In Standard Collections
* Since Python 3.10: :pep:`604` -- Allow writing union types as X | Y


Dict
----
Empty:

>>> data: dict = {}
>>> data: dict = dict()

Generic:

>>> data: dict = {'firstname': 'Mark', 'lastname': 'Watney'}

Strict:

>>> data: dict[str, str] = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> data: dict[str, str|int] = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>>
>>> data: dict[int, str] = {
...    0: 'setosa',
...    1: 'virginica',
...    2: 'versicolor'}
>>>
>>> data: dict[float, str] = {
...    5.8: 'Sepal length',
...    2.7: 'Sepal width',
...    5.1: 'Petal length',
...    1.9: 'Petal width'}
>>>
>>> data: dict[str, float] = {
...    'Sepal length': 5.8,
...    'Sepal width': 2.7,
...    'Petal length': 5.1,
...    'Petal width': 1.9}


Typed Dict
----------
Since Python 3.8: :pep:`589` -- TypedDict: Type Hints for Dictionaries with a Fixed Set of Keys

>>> from typing import TypedDict


>>> class Astronaut(TypedDict):
...     firstname: str
...     lastname: str
...     age: int | float
...
...
>>> def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut["firstname"]} {astronaut["lastname"]}'
...
...
>>> mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
>>> hello_astronaut(mark)  # ok
>>>
>>> mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney'}
>>> hello_astronaut(mark)  # error: missing `age`  # doctest: +SKIP
>>>
>>> mark: Astronaut = {'firstname': 'Mark'}
>>> hello_astronaut(mark)  # error: missing `lastname` and `age`  # doctest: +SKIP
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
>>> hello_astronaut(mark)  # ok
>>>
>>> mark = Astronaut(firstname='Mark', lastname='Watney')
>>> hello_astronaut(mark)  # error: missing `age`  # doctest: +SKIP
>>>
>>> mark = Astronaut(firstname='Mark')
>>> hello_astronaut(mark)  # error: missing `lastname`  # doctest: +SKIP
>>>
>>> iris = {'genus': 'Iris', 'species': 'Setosa'}
>>> hello_astronaut(iris)  # error: not an astronaut  # doctest: +SKIP


Future
------
* Since Python 3.11 :pep:`655` -- Marking individual TypedDict items as required or potentially-missing

>>> # doctest: +SKIP
... from typing import Required, NotRequired
...
...
... class Astronaut(TypedDict):
...     firstname: Required[str]
...     lastname: Required[str]
...     age: NotRequired[int|float]
...
...
... def hello_astronaut(astronaut: Astronaut):
...     result = f'Hello {astronaut["firstname"]} {astronaut["lastname"]}')
...
...
... mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney', 'age': 40}
... hello_astronaut(mark)  # ok
...
... mark: Astronaut = {'firstname': 'Mark', 'lastname': 'Watney'}
... hello_astronaut(mark)  # ok
...
... mark: Astronaut = {'firstname': 'Mark'}
... hello_astronaut(mark)  # error: missing `lastname`
...
... mark = Astronaut(firstname='Mark', lastname='Watney', age=40)
... hello_astronaut(mark)  # ok
...
... mark = Astronaut(firstname='Mark', lastname='Watney')
... hello_astronaut(mark)  # ok
...
... mark = Astronaut(firstname='Mark')
... hello_astronaut(mark)  # error: missing `lastname`
...
... iris = {'genus': 'Iris', 'species': 'Setosa'}
... hello_astronaut(iris)  # error: not an astronaut


Use Case - 0x01
---------------
>>> calendarium: dict[int, str] = {
...     1961: 'Yuri Gagarin fly to space',
...     1969: 'Neil Armstrong set foot on the Moon',
... }


Use Case - 0x02
---------------
>>> calendarium: dict[int, list[str]] = {
...     1961: ['Yuri Gagarin fly to space', 'Alan Shepard fly to space'],
...     1969: ['Neil Armstrong set foot on the Moon'],
... }


Further Reading
---------------
* More information in `Type Annotations`
* More information in `CI/CD Type Checking`
