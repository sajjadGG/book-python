Operator String About
=====================
* ``str()``
* ``repr()``

Setup:

>>> import datetime
>>>
>>> date = datetime.date(1961, 4, 12)


Str
---
* ``print(obj)`` -> ``str(obj)`` -> ``obj.__str__()``

>>> print(date)
1961-04-12

>>> str(date)
'1961-04-12'

>>> date.__str__()
'1961-04-12'


Repr
----
* ``obj`` -> ``repr(obj)`` -> ``obj.__repr__()``

>>> date
datetime.date(1961, 4, 12)

>>> repr(date)
'datetime.date(1961, 4, 12)'

>>> date.__repr__()
'datetime.date(1961, 4, 12)'
