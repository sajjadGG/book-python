Mapping Dict
============


Rationale
---------
* ``dict`` are key-value storage
* key lookup is very efficient ``O(1)``
* Mutable - can add, remove, and modify items


Definition
----------
* ``{}`` is used more often
* ``dict()`` is more readable
* Comma after last element is optional
* Since Python 3.7: ``dict`` keeps order of elements
* Before Python 3.7: ``dict`` order is not ensured!!
* https://mail.python.org/pipermail/python-dev/2017-December/151283.html

>>> data = {}
>>> data = dict()

>>> data = {
...    1961: 'First Human Space Flight',
...    1969: 'First Step on the Moon'}

>>> data = {
...    1961: ['First Russian Space Flight', 'First US Space Flight'],
...    1969: ['First Step on the Moon']}

>>> data = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}

>>> data = dict(
...    commander='Melissa Lewis',
...    botanist='Mark Watney',
...    chemist='Alex Vogel')

Duplicating items are overridden by latter:

>>> data = {
...    'commander': 'Melissa Lewis',
...    'commander': 'Jan Twardowski'}
>>>
>>> data
{'commander': 'Jan Twardowski'}


GetItem
-------
* ``[...]`` throws ``KeyError`` exception if key not found in ``dict``
* ``.get()`` returns ``None`` if key not found
* ``.get()`` can have default value, if key not found

Getitem Method:

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> crew['commander']
'Melissa Lewis'
>>>
>>> crew['pilot']
Traceback (most recent call last):
KeyError: 'pilot'

Get Method:

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> crew.get('commander')
'Melissa Lewis'
>>>
>>> crew.get('pilot')
>>>
>>> crew.get('pilot', 'not assigned')
'not assigned'

Getting keys other than ``str``:

>>> calendarium = {
...    1961: 'First Human Space Flight',
...    1969: 'First Step on the Moon'}
>>>
>>> calendarium[1961]
'First Human Space Flight'
>>>
>>> calendarium.get(1961)
'First Human Space Flight'
>>>
>>> calendarium['1961']
Traceback (most recent call last):
KeyError: '1961'
>>>
>>> calendarium.get('1961')
>>>
>>> calendarium.get('1961', 'unknown')
'unknown'


Get Keys, Values and Key-Value Pairs
------------------------------------
* Key can be any hashable object

In Python 2, the methods items(), keys() and values() used to "take a snapshot" of the dictionary contents and return it as a list. It meant that if the dictionary changed while you were iterating over the list, the contents in the list would not change. In Python 3, these methods return a view object whose contents change dynamically as the dictionary changes. Therefore, in order for the behavior of iterations over the result of these methods to remain consistent with previous versions, an additional call to list() has to be performed in Python 3 to "take a snapshot" of the view object contents. [#Hamidi2017]_

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> crew.keys()
dict_keys(['commander', 'botanist', 'chemist'])
>>>
>>> crew.values()
dict_values(['Melissa Lewis', 'Mark Watney', 'Alex Vogel'])
>>>
>>> crew.items()
dict_items([('commander', 'Melissa Lewis'), ('botanist', 'Mark Watney'), ('chemist', 'Alex Vogel')])
>>>
>>> list(crew.keys())
['commander', 'botanist', 'chemist']
>>>
>>> list(crew.values())
['Melissa Lewis', 'Mark Watney', 'Alex Vogel']
>>>
>>> list(crew.items())  # doctest: +NORMALIZE_WHITESPACE
[('commander', 'Melissa Lewis'),
 ('botanist', 'Mark Watney'),
 ('chemist', 'Alex Vogel')]


Set Item
--------
* Adds if value not exist
* Updates if value exist

Set Item Method:

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> crew['pilot'] = 'Rick Martinez'
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez'}
>>>
>>> crew['commander'] = 'Jan Twardowski'
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Jan Twardowski',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez'}

Update Method:

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> crew.update(pilot='Rick Martinez')
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez'}
>>>
>>> crew.update(commander='Jan Twardowski')
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Jan Twardowski',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez'}

Update Method:

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> new = {
...    'pilot': 'Rick Martinez',
...    'surgeon': 'Chris Beck',
...    'engineer': 'Beth Johanssen'}
>>>
>>> crew.update(new)
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}


Delete Item
-----------

Pop Method:

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel',
...    'pilot': 'Rick Martinez',
...    'surgeon': 'Chris Beck',
...    'engineer': 'Beth Johanssen'}
>>>
>>> left_alone_on_mars = crew.pop('botanist')
>>>
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}
>>>
>>> print(left_alone_on_mars)
Mark Watney

Popitem Method:

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> last = crew.popitem()
>>>
>>> print(crew)
{'commander': 'Melissa Lewis', 'botanist': 'Mark Watney'}
>>>
>>> print(last)
('chemist', 'Alex Vogel')

Del Keyword:

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> del crew['chemist']
>>>
>>> print(crew)
{'commander': 'Melissa Lewis', 'botanist': 'Mark Watney'}


Merge
-----
* Merge (``|``) and update (``|=``) operators have been added to the built-in dict class.
* Since Python 3.9: :pep:`584` -- Add Union Operators To dict

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> new = {
...     'pilot': 'Rick Martinez',
...     'surgeon': 'Chris Beck',
...     'engineer': 'Beth Johanssen'}
>>>
>>> everyone = crew | new
>>>
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel'}
>>>
>>> print(new)  # doctest: +NORMALIZE_WHITESPACE
{'pilot': 'Rick Martinez',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}
>>>
>>> print(everyone)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> new = {
...    'pilot': 'Rick Martinez',
...    'surgeon': 'Chris Beck',
...    'engineer': 'Beth Johanssen'}
>>>
>>> crew |= new
>>>
>>> print(crew)  # doctest: +NORMALIZE_WHITESPACE
{'commander': 'Melissa Lewis',
 'botanist': 'Mark Watney',
 'chemist': 'Alex Vogel',
 'pilot': 'Rick Martinez',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}
>>>
>>> print(new)  # doctest: +NORMALIZE_WHITESPACE
{'pilot': 'Rick Martinez',
 'surgeon': 'Chris Beck',
 'engineer': 'Beth Johanssen'}


GetItem and Slice
-----------------
* GetItem with index on ``dict`` is not possible
* Slicing on ``dict`` is not possible

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> crew[0]
Traceback (most recent call last):
KeyError: 0
>>> crew[1]
Traceback (most recent call last):
KeyError: 1
>>> crew[2]
Traceback (most recent call last):
KeyError: 2
>>> crew[-0]
Traceback (most recent call last):
KeyError: 0
>>> crew[-1]
Traceback (most recent call last):
KeyError: -1
>>> crew[-2]
Traceback (most recent call last):
KeyError: -2
>>> crew[1:2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'
>>> crew[:2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'
>>> crew[::2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'

>>> crew = {
...    0: 'Melissa Lewis',
...    1: 'Mark Watney',
...    2: 'Alex Vogel'}
>>>
>>> crew[0]
'Melissa Lewis'
>>> crew[1]
'Mark Watney'
>>> crew[2]
'Alex Vogel'
>>> crew[-0]
'Melissa Lewis'
>>> crew[-1]
Traceback (most recent call last):
KeyError: -1
>>> crew[-2]
Traceback (most recent call last):
KeyError: -2
>>> crew[1:2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'
>>> crew[:2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'
>>> crew[::2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'


Dict or Set
-----------
* Both ``set`` and ``dict`` keys must be hashable
* Both ``set`` and ``dict`` uses the same ``{`` and ``}`` braces
* Despite similar syntax, they are different types

>>> data = {1, 2}
>>> type(data)
<class 'set'>

>>> data = {1: 2}
>>> type(data)
<class 'dict'>

>>> data = {1, 2, 3, 4}
>>> type(data)
<class 'set'>
>>> data = {1: 2, 3: 4}
>>> type(data)
<class 'dict'>

Empty ``dict`` and empty ``set``:

>>> data = {1: 1}
>>> data.pop(1)
1
>>> data
{}

>>> data = {1}
>>> data.pop()
1
>>> data
set()

Differences:

>>> data = {1: 1}
>>> isinstance(data, set)
False
>>> isinstance(data, dict)
True

>>> data = {1}
>>> isinstance(data, set)
True
>>> isinstance(data, dict)
False

>>> data = {}
>>> isinstance(data, set)
False
>>> isinstance(data, dict)
True


Length
------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>> len(crew)
3
>>> len(crew.keys())
3
>>> len(crew.values())
3
>>> len(crew.items())
3


Examples
--------
>>> git = {
...    'ce16a8ce': 'commit/1',
...    'cae6b510': 'commit/2',
...    '895444a6': 'commit/3',
...    'aef731b5': 'commit/4',
...    '4a92bc79': 'branch/master',
...    'b3bbd85a': 'tag/v1.0'}


Assignments
-----------
.. literalinclude:: assignments/mapping_dict_a.py
    :caption: :download:`Solution <assignments/mapping_dict_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_dict_b.py
    :caption: :download:`Solution <assignments/mapping_dict_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_dict_c.py
    :caption: :download:`Solution <assignments/mapping_dict_c.py>`
    :end-before: # Solution

.. literalinclude:: assignments/mapping_dict_d.py
    :caption: :download:`Solution <assignments/mapping_dict_d.py>`
    :end-before: # Solution


References
----------
.. [#Hamidi2017] Frédéric Hamidi. Why does Python 3 need dict.items to be wrapped with list()? Accessed Data: 2021-02-28. URL: https://stackoverflow.com/a/17695716
