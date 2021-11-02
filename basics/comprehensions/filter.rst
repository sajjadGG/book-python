Comprehension Filter
====================


Syntax
------
>>> result = []
...
>>> for x in range(0,5):
...     if x % 2 == 0:
...         result.append(x)
>>>
>>> print(result)
[0, 2, 4]

>>> result = [x for x in range(0,5) if x%2==0]
>>> print(result)
[0, 2, 4]


Code Readability
----------------
>>> result = [pow(x, 2) for x in range(0, 5) if x % 2 == 0]

>>> result = [pow(x,2) for x in range(0,5) if x%2==0]

>>> result = [pow(x,2)
...           for x in range(0,5)
...               if x % 2 == 0]

>>> result = [pow(x,2)
...           for x in range(0,5)
...           if x % 2 == 0]


Use Case - Even or Odd
----------------------
>>> [x for x in range(0,5)]
[0, 1, 2, 3, 4]

>>> [x%2==0 for x in range(0,5)]
[True, False, True, False, True]


Use Case - Even or Odd
----------------------
>>> result = {}
>>>
>>> for x in range(0,5):
...     is_even = (x % 2 == 0)
...     result.update({x: is_even})
>>>
>>> print(result)
{0: True, 1: False, 2: True, 3: False, 4: True}

>>> {x: (x%2==0) for x in range(0,5)}
{0: True, 1: False, 2: True, 3: False, 4: True}


Use Case - Filter list[tuple]
-----------------------------
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
>>> [features for *features,label in DATA if label == 'setosa']  # doctest: +NORMALIZE_WHITESPACE
[[5.1, 3.5, 1.4, 0.2],
 [4.7, 3.2, 1.3, 0.2]]
>>>
>>> [X for *X,y in DATA if y=='setosa']  # doctest: +NORMALIZE_WHITESPACE
[[5.1, 3.5, 1.4, 0.2],
 [4.7, 3.2, 1.3, 0.2]]


Use Case - Filter list[dict]
----------------------------
>>> DATA = [
...     {'is_astronaut': True,  'name': 'Jan Twardowski'},
...     {'is_astronaut': True,  'name': 'Mark Watney'},
...     {'is_astronaut': False, 'name': 'José Jiménez'},
...     {'is_astronaut': True,  'name': 'Melissa Lewis'},
...     {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [person
...               for person in DATA
...               if person['is_astronaut']]
>>>
>>> print(astronauts)  # doctest: +NORMALIZE_WHITESPACE
[{'is_astronaut': True, 'name': 'Jan Twardowski'},
 {'is_astronaut': True, 'name': 'Mark Watney'},
 {'is_astronaut': True, 'name': 'Melissa Lewis'}]

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>> astronauts = [person['name']
...               for person in DATA
...               if person['is_astronaut']]
>>>
>>> print(astronauts)
['Jan Twardowski', 'Mark Watney', 'Melissa Lewis']


Assignments
-----------
.. literalinclude:: assignments/comprehension_filter_a.py
    :caption: :download:`Solution <assignments/comprehension_filter_a.py>`
    :end-before: # Solution
