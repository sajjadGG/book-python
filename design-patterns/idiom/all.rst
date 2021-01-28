All
===


Rationale
---------
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:


Implementation
--------------
.. code-block:: python

    def all(iterable):
        if not iterable:
            return False
        for element in iterable:
            if not element:
                return False
        return True


Use Case
--------
>>> all(x for x in range(0,5))
False

>>> DATA = [{'is_astronaut': True,  'name': 'Jan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>>
>>> if all(person['is_astronaut'] for person in DATA):
...     print('Everyone is astronaut')
... else:
...     print('Not everyone is astronaut')
Not everyone is astronaut

>>> DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
...         (5.8, 2.7, 5.1, 1.9, 'virginica'),
...         (5.1, 3.5, 1.4, 0.2, 'setosa'),
...         (5.7, 2.8, 4.1, 1.3, 'versicolor'),
...         (6.3, 2.9, 5.6, 1.8, 'virginica'),
...         (6.4, 3.2, 4.5, 1.5, 'versicolor'),
...         (4.7, 3.2, 1.3, 0.2, 'setosa'),
...         (7.0, 3.2, 4.7, 1.4, 'versicolor')]
>>>
>>>
>>> all(observation > 1.0
...     for *features, label in DATA[1:]
...     for observation in features
...     if isinstance(observation, float))
False
>>>
>>> all(x > 1.0
...     for *X,y in DATA[1:]
...     for x in X
...     if isinstance(x, float))
False
