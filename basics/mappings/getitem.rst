Mapping Getitem
===============
* Key lookup is very efficient ``O(1)``
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


Use Case - 0x01
---------------
>>> PAYROLL = [
...     {'name': 'Mark Watney',   '2000-01': 2000, '2000-02': 2000, '2000-03': 2000},
...     {'name': 'Melissa Lewis', '2000-01': 3000, '2000-02': 3000, '2000-03': 3000},
...     {'name': 'Rick Martinez', '2000-03': 2500},
...     {'name': 'Alex Vogel',    '2000-01': 2500, '2000-02': 2500, '2000-03': 2500},
... ]

>>> result = f'{"Employee":<15} {"January":>10} {"February":>9} {"March":>6}'
>>>
>>> for employee in PAYROLL:
...     name = employee['name']
...     january = employee['2000-01']
...     february = employee['2000-02']
...     march = employee['2000-03']
...     result += f'{name:<15} {january:>10} {february:>9} {march:>6}'
...
Traceback (most recent call last):
KeyError: '2000-01'

>>> result = f'{"Employee":<15} {"January":>10} {"February":>9} {"March":>6}\n'
>>>
>>> for employee in PAYROLL:
...     name = employee['name']
...     january = employee.get('2000-01', 'n/a')
...     february = employee.get('2000-02', 'n/a')
...     march = employee.get('2000-03', 'n/a')
...     result += f'{name:<15} {january:>10} {february:>9} {march:>6}\n'
>>>
>>> print(result)
Employee           January  February  March
Mark Watney           2000      2000   2000
Melissa Lewis         3000      3000   3000
Rick Martinez          n/a       n/a   2500
Alex Vogel            2500      2500   2500
<BLANKLINE>

>>> result = f'{"Employee":<15} {"January":>10} {"February":>9} {"March":>6}\n'
>>>
>>> for employee in PAYROLL:
...     name = employee['name']
...     january = employee.get('2000-01', '-')
...     february = employee.get('2000-02', '-')
...     march = employee.get('2000-03', '-')
...     result += f'{name:<15} {january:>10} {february:>9} {march:>6}\n'
>>>
>>> print(result)
Employee           January  February  March
Mark Watney           2000      2000   2000
Melissa Lewis         3000      3000   3000
Rick Martinez            -         -   2500
Alex Vogel            2500      2500   2500
<BLANKLINE>

>>> result = f'{"Employee":<15} {"January":>10} {"February":>9} {"March":>6}\n'
>>>
>>> for employee in PAYROLL:
...     name = employee['name']
...     january = employee.get('2000-01', '')
...     february = employee.get('2000-02', '')
...     march = employee.get('2000-03', '')
...     result += f'{name:<15} {january:>10} {february:>9} {march:>6}\n'
>>>
>>> print(result)
Employee           January  February  March
Mark Watney           2000      2000   2000
Melissa Lewis         3000      3000   3000
Rick Martinez                          2500
Alex Vogel            2500      2500   2500
<BLANKLINE>

.. todo:: Assignments
