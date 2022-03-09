Sequence Ordered
================


Both
----
* ordered
* possible to getitem and slice
* elements can be duplicated
* elements of any types


Tuple
-----
* immutable
* one contingent block of data in memory


List
----
* mutable
* implemented in memory as list of references to objects
* objects are scattered in memory


Memory Footprint
----------------
>>> from sys import getsizeof
>>>
>>> a = [1, 2, 3]
>>> b = (1, 2, 3)
>>>
>>> getsizeof(a)
120
>>>
>>> getsizeof(b)
64


Memory
------
.. figure:: img/memory-compare.png

    Memory representation for ``list`` and ``tuple``


.. todo:: Assignments
