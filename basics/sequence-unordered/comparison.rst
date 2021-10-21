Sequence Unordered
==================


Both
----
* unordered
* impossible to getitem and slice
* unique elements
* only **hashable** elements


Frozenset
---------
* immutable


Set
---
* mutable


Memory Footprint
----------------
>>> from sys import getsizeof
>>>
>>>
>>> a = {1, 2, 3}
>>> b = frozenset({1, 2, 3})
>>>
>>> getsizeof(a)
216
>>>
>>> getsizeof(b)
216


Assignments
-----------
.. todo:: Create assignments
