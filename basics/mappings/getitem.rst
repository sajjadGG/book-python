Mapping Getitem
===============


Rationale
---------
* ``[...]`` throws ``KeyError`` exception if key not found in ``dict``
* ``.get()`` returns ``None`` if key not found
* ``.get()`` can have default value, if key not found


Getitem Method
--------------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>> crew['commander']
'Melissa Lewis'
>>>
>>> crew['chemist']
Traceback (most recent call last):
KeyError: 'chemist'


Get Method
----------
>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>> crew.get('commander')
'Melissa Lewis'
>>>
>>> crew.get('chemist')
>>>
>>> crew.get('chemist', 'not assigned')
'not assigned'


Key Type
--------
Getting keys other than ``str``:

>>> calendarium = {
...    1961: 'First Human Space Flight',
...    1969: 'First Step on the Moon'}
>>>
>>>
>>> calendarium[1961]
'First Human Space Flight'
>>>
>>> calendarium['1961']
Traceback (most recent call last):
KeyError: '1961'



GetItem
-------
* GetItem with index on ``dict`` is not possible

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew[0]
Traceback (most recent call last):
KeyError: 0
>>>
>>> crew[1]
Traceback (most recent call last):
KeyError: 1

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew[-0]
Traceback (most recent call last):
KeyError: 0
>>>
>>> crew[-1]
Traceback (most recent call last):
KeyError: -1


Slice
-----
* Slicing on ``dict`` is not possible

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'pilot': 'Rick Martinez'}
>>>
>>>
>>> crew[1:2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'
>>>
>>> crew[:2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'
>>>
>>> crew[::2]
Traceback (most recent call last):
TypeError: unhashable type: 'slice'


GetItem on Numeric Dict Keys
----------------------------
>>> crew = {
...    0: 'Melissa Lewis',
...    1: 'Mark Watney',
...    2: 'Rick Martinez'}
>>>
>>>
>>> crew[0]
'Melissa Lewis'
>>>
>>> crew[1]
'Mark Watney'
>>>
>>> crew[2]
'Rick Martinez'
>>>
>>> crew[-0]
'Melissa Lewis'
>>>
>>> crew[-1]
Traceback (most recent call last):
KeyError: -1
>>>
>>> crew[-2]
Traceback (most recent call last):
KeyError: -2


Assignments
-----------
.. todo:: Create assignments
