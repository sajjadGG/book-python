Comprehension All, Any
======================


Any
---
>>> any(x for x in range(0,5))
True

>>> PEOPLE = [{'is_astronaut': True,  'name': 'Melissa Lewis'},
...           {'is_astronaut': True,  'name': 'Mark Watney'},
...           {'is_astronaut': False, 'name': 'Rick Martinez'},
...           {'is_astronaut': True,  'name': 'Alex Vogel'}]
>>>
>>>
>>> if any(person['is_astronaut'] for person in PEOPLE):
...     print('At least one person is astronaut')
... else:
...     print('There are no astronauts')
At least one person is astronaut


All
---
>>> all(x for x in range(0,5))
False

>>> PEOPLE = [{'is_astronaut': True,  'name': 'Melissa Lewis'},
...           {'is_astronaut': True,  'name': 'Mark Watney'},
...           {'is_astronaut': False, 'name': 'Rick Martinez'},
...           {'is_astronaut': True,  'name': 'Alex Vogel'}]
>>>
>>>
>>> if all(person['is_astronaut'] for person in PEOPLE):
...     print('Everyone is astronaut')
... else:
...     print('Not everyone is astronaut')
Not everyone is astronaut

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
>>> all(observation > 1.0
...     for *features, label in DATA[1:]
...     for observation in features
...     if isinstance(observation, float))
False



Assignments
-----------
.. todo:: Create Assignments
