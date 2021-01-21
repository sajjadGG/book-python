Filter
======


Rationale
---------
* Select elements from sequence
* Generator (lazy evaluated)
* Built-in

Syntax:

    * ``filter(callable, *iterables)``
    * required ``callable`` - Function
    * required ``iterables`` - 1 or many sequence or iterator objects

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> DATA = [0, 1, 2, 3, 4, 5, 6]
>>>
>>> list(x for x in DATA if even(x))
[0, 2, 4, 6]
>>> list(filter(even, DATA))
[0, 2, 4, 6]

>>> DATA = [0, 1, 2, 3, 4, 5, 6]
>>>
>>> list(x for x in DATA if x%2==0)
[0, 2, 4, 6]
>>>
>>> list(filter(lambda x: x%2==0, DATA))
[0, 2, 4, 6]


Pattern
-------
Plain code:

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5, 6]
>>> result = []
>>>
>>> for x in DATA:
...     if even(x):
...         result.append(x)
>>>
>>> print(result)
[2, 4, 6]

Comprehension:

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5, 6]
>>> result = [x for x in DATA if x%2==0]
>>>
>>> print(result)
[2, 4, 6]

Filter:

>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5, 6]
>>> result = filter(even, DATA)
>>>
>>> list(result)
[2, 4, 6]


Lazy Evaluation
---------------
>>> def even(x):
...     return x % 2 == 0
>>>
>>>
>>> DATA = [1, 2, 3, 4, 5, 6]
>>> result = filter(even, DATA)
>>>
>>> next(result)
2
>>> next(result)
4
>>> next(result)
6
>>> next(result)
Traceback (most recent call last):
StopIteration


Use Cases
---------
>>> people = [
...     {'age': 21, 'name': 'Jan Twardowski'},
...     {'age': 25, 'name': 'Mark Watney'},
...     {'age': 18, 'name': 'Melissa Lewis'}]
>>>
>>>
>>> def adult(person):
...     return person['age'] >= 21
>>>
>>>
>>> result = filter(adult, people)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'age': 21, 'name': 'Jan Twardowski'},
 {'age': 25, 'name': 'Mark Watney'}]

>>> people = [
...     {'is_astronaut': False, 'name': 'Jan Twardowski'},
...     {'is_astronaut': True, 'name': 'Mark Watney'},
...     {'is_astronaut': True, 'name': 'Melissa Lewis'}]
>>>
>>>
>>> def astronaut(person):
...     return person['is_astronaut']
>>>
>>>
>>> result = filter(astronaut, people)
>>> list(result)  # doctest: +NORMALIZE_WHITESPACE
[{'is_astronaut': True, 'name': 'Mark Watney'},
 {'is_astronaut': True, 'name': 'Melissa Lewis'}]

>>> astronauts = ['Mark Watney', 'Melissa Lewis']
>>>
>>> people = ['Jan Twardowski', 'Mark Watney',
...           'Melissa Lewis', 'Jimenez']
>>>
>>>
>>> def is_astronaut(person):
...     return person in astronauts
>>>
>>>
>>> result = filter(is_astronaut, people)
>>> list(result)
['Mark Watney', 'Melissa Lewis']


Assignments
-----------
.. literalinclude:: ../_assignments/idioms_filter_a.py
    :caption: :download:`Solution <../_assignments/idioms_filter_a.py>`
    :end-before: # Solution
