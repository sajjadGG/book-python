OOP Stringify About
===================
* ``str()``
* ``repr()``
* ``format()``

Setup:

>>> import datetime
>>>
>>> date = datetime.date(1961, 4, 12)


Str
---
* ``str(obj)`` -> ``obj.__str__()``
* ``print(obj)`` -> ``str(obj)`` -> ``obj.__str__()``

>>> str(date)
'1961-04-12'

>>> print(date)
1961-04-12


Repr
----
* ``repr(obj)`` -> ``obj.__repr__()``
* ``obj`` -> ``repr(obj)`` -> ``obj.__repr__()``

>>> repr(date)
'datetime.date(1961, 4, 12)'

>>> date
datetime.date(1961, 4, 12)


.. todo:: Assignments
