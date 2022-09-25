Mapping Keys
============

Why must dictionary keys be immutable? [#PyDocDictKeys]_

The hash table implementation of dictionaries uses a hash value calculated
from the key value to find the key. If the key were a mutable object,
its value could change, and thus its hash could also change. But since
whoever changes the key object can't tell that it was being used as a
dictionary key, it can't move the entry around in the dictionary. Then,
when you try to look up the same object in the dictionary it won't be
found because its hash value is different. If you tried to look up the
old value it wouldn't be found either, because the value of the object
found in that hash bin would be different.

If you want a dictionary indexed with a list, simply convert the list to
a tuple first; the function tuple(L) creates a tuple with the same entries
as the list L. Tuples are immutable and can therefore be used as dictionary
keys.

Some unacceptable solutions that have been proposed:

Hash lists by their address (object ID). This doesn't work because if you
construct a new list with the same value it won't be found; e.g.:

>>> mydict = {[1, 2]: '12'}
Traceback (most recent call last):
TypeError: unhashable type: 'list'

>>> mydict = {(1, 2): '12'}
>>> print(mydict[[1, 2]])
Traceback (most recent call last):
TypeError: unhashable type: 'list'

would raise a KeyError exception because the id of the [1, 2] used in the
second line differs from that in the first line. In other words, dictionary
keys should be compared using ==, not using is.

Make a copy when using a list as a key. This doesn't work because the list,
being a mutable object, could contain a reference to itself, and then the
copying code would run into an infinite loop.

Allow lists as keys but tell the user not to modify them. This would allow
a class of hard-to-track bugs in programs when you forgot or modified
a list by accident. It also invalidates an important invariant of
dictionaries: every value in d.keys() is usable as a key of the dictionary.

Mark lists as read-only once they are used as a dictionary key. The problem
is that it's not just the top-level object that could change its value;
you could use a tuple containing a list as a key. Entering anything as
a key into a dictionary would require marking all objects reachable from
there as read-only – and again, self-referential objects could cause an
infinite loop.

There is a trick to get around this if you need to, but use it at your own
risk: You can wrap a mutable structure inside a class instance which has
both a __eq__() and a __hash__() method. You must then make sure that the
hash value for all such wrapper objects that reside in a dictionary (or
other hash based structure), remain fixed while the object is in the
dictionary (or other structure).

>>> class ListWrapper:
...     def __init__(self, the_list):
...         self.the_list = the_list
...
...     def __eq__(self, other):
...         return self.the_list == other.the_list
...
...     def __hash__(self):
...         l = self.the_list
...         result = 98767 - len(l)*555
...         for i, el in enumerate(l):
...             try:
...                 result = result + (hash(el) % 9999999) * 1001 + i
...             except Exception:
...                 result = (result % 7777777) + i * 333
...         return result

Note that the hash computation is complicated by the possibility that some
members of the list may be unhashable and also by the possibility of
arithmetic overflow.

Furthermore it must always be the case that ``if o1 == o2 (ie o1.__eq__(o2)``
is True) then ``hash(o1) == hash(o2)`` (ie, o1.__hash__() == o2.__hash__()),
regardless of whether the object is in a dictionary or not. If you fail
to meet these restrictions dictionaries and other hash based structures
will misbehave.

In the case of ListWrapper, whenever the wrapper object is in a dictionary
the wrapped list must not change to avoid anomalies. Don't do this unless
you are prepared to think hard about the requirements and the consequences
of not meeting them correctly. Consider yourself warned.


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
...    'pilot': 'Rick Martinez',
... }
>>>
>>>
>>> crew.keys()
dict_keys(['commander', 'botanist', 'pilot'])
>>>
>>> list(crew.keys())
['commander', 'botanist', 'pilot']


Use Case - 0x01
---------------
>>> calendarium = {
...    1961: 'First Human Space Flight',
...    1969: 'First Step on the Moon',
... }


Use Case - 0x02
---------------
>>> calendarium = {
...    1961: ['First Russian Space Flight', 'First US Space Flight'],
...    1969: ['First Step on the Moon'],
... }


References
----------
.. [#Hamidi2017] Hamidi, Frédéric. Why does Python 3 need dict.items to be wrapped with list()? Year: 2021. Retrieved: 2021-02-28. URL: https://stackoverflow.com/a/17695716

.. [#PyDocDictKeys] van Rossum, G. et al. Why must dictionary keys be immutable? Year: 2022. Retrieved: 2022-09-25. URL: https://docs.python.org/3/faq/design.html#why-must-dictionary-keys-be-immutable


Assignments
-----------
.. literalinclude:: assignments/mapping_define_a.py
    :caption: :download:`Solution <assignments/mapping_define_a.py>`
    :end-before: # Solution
