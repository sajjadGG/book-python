Mapping Keys
============


Valid Keys
----------
* hashable

>>> data = {
...     1: 'red',
...     2: 'green',
...     3: 'blue',
... }

>>> data = {
...     1.1: 'red',
...     2.2: 'green',
...     3.3: 'blue',
... }

>>> data = {
...     'a': 'red',
...     'b': 'green',
...     'c': 'blue',
... }

>>> data = {
...     True: 'red',
...     False: 'green',
...     None: 'blue',
... }

>>> data = {
...     (1,2,3): 'red',
...     (4,5,6): 'green',
...     (7,8,9): 'blue',
... }


Invalid Keys
------------
* unhashable
* ``list``, ``set`` and ``dict`` cannot be a key

>>> data = {
...     [1,2,3]: 'red',
...     [4,5,6]: 'green',
...     [7,8,9]: 'blue',
... }
Traceback (most recent call last):
TypeError: unhashable type: 'list'

>>> data = {
...     {1,2,3}: 'red',
...     {4,5,6}: 'green',
...     {7,8,9}: 'blue',
... }
Traceback (most recent call last):
TypeError: unhashable type: 'set'

>>> data = {
...     {1: None, 2:None, 3:None}: 'red',
...     {4: None, 5:None, 6:None}: 'green',
...     {7: None, 8:None, 9:None}: 'blue',
... }
Traceback (most recent call last):
TypeError: unhashable type: 'dict'


Get Keys
--------
In Python 2, the methods items(), keys() and values() used to "take a snapshot"
of the dictionary contents and return it as a list. It meant that if the
dictionary changed while you were iterating over the list, the contents in the
list would not change. In Python 3, these methods return a view object whose
contents change dynamically as the dictionary changes. Therefore, in order for
the behavior of iterations over the result of these methods to remain consistent
with previous versions, an additional call to list() has to be performed in
Python 3 to "take a snapshot" of the view object contents. [#Hamidi2017]_

>>> crew = {
...    'commander': 'Melissa Lewis',
...    'botanist': 'Mark Watney',
...    'chemist': 'Alex Vogel'}
>>>
>>>
>>> crew.keys()
dict_keys(['commander', 'botanist', 'chemist'])
>>>
>>> list(crew.keys())
['commander', 'botanist', 'chemist']


Use Case - 0x01
---------------
>>> calendarium = {
...    1961: 'First Human Space Flight',
...    1969: 'First Step on the Moon'}


Use Case - 0x02
---------------
>>> calendarium = {
...    1961: ['First Russian Space Flight', 'First US Space Flight'],
...    1969: ['First Step on the Moon']}


References
----------
.. [#Hamidi2017] Frédéric Hamidi. Why does Python 3 need dict.items to be wrapped with list()? Retrieved: 2021-02-28. URL: https://stackoverflow.com/a/17695716


Assignments
-----------
.. literalinclude:: assignments/mapping_define_a.py
    :caption: :download:`Solution <assignments/mapping_dict_a.py>`
    :end-before: # Solution
