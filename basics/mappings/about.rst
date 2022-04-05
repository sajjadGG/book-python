Mapping About
=============


Scalar
------
* Scalar

>>> 'Mark'  # doctest: +SKIP
>>> 'Watney'  # doctest: +SKIP
>>> 40  # doctest: +SKIP
>>> 185.5  # doctest: +SKIP
>>> 75.5  # doctest: +SKIP


Value
-----
* Identifier + scalar = value

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>> age = 40
>>> height = 185.5
>>> weight = 75.5


Data
----
* Value + relation = data

>>> astronaut = ('Mark', 'Watney', 40, 185.5, 75.5)


Information
-----------
* Data + context = information

>>> astronaut = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'age': 40,
...     'height': 185.5,
...     'weight': 75.5,
... }
