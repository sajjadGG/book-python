Any
===
* Return True if any element of the iterable is true.
* If the iterable is empty, return False.


Solution
--------
>>> def any(iterable):
...     if not iterable:
...         return False
...     for element in iterable:
...         if element:
...             return True
...     return False


Use Case
--------
>>> any(x for x in range(0,5))
True

>>> DATA = [{'is_astronaut': True,  'name': 'Pan Twardowski'},
...         {'is_astronaut': True,  'name': 'Mark Watney'},
...         {'is_astronaut': False, 'name': 'José Jiménez'},
...         {'is_astronaut': True,  'name': 'Melissa Lewis'},
...         {'is_astronaut': False, 'name': 'Alex Vogel'}]
>>>
>>>
>>> if any(person['is_astronaut'] for person in DATA):
...     print('At least one person is astronaut')
... else:
...     print('There are no astronauts')
At least one person is astronaut
