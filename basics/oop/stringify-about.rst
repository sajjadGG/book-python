OOP Stringify About
===================


Rationale
---------
* ``str()``
* ``repr()``
* ``format()``


Str
---
* ``str(obj)`` -> ``obj.__str__()``
* ``print(obj)`` -> ``str(obj)`` -> ``obj.__str__()``

>>> import datetime
>>>
>>> date = datetime.date(1961, 4, 12)
>>>
>>>
>>> str(date)
'1961-04-12'
>>>
>>> print(date)
1961-04-12


Repr
----
* ``repr(obj)`` -> ``obj.__repr__()``
* ``obj`` -> ``repr(obj)`` -> ``obj.__repr__()``

>>> import datetime
>>>
>>> date = datetime.date(1961, 4, 12)
>>>
>>>
>>> repr(date)
'datetime.date(1961, 4, 12)'
>>>
>>> date
datetime.date(1961, 4, 12)



.. todo:: Assignments
