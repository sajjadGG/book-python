Mapping About
=============


Value
-----
* identifier + scalar = value

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>> age = 40
>>> height = 185.5
>>> weight = 75.5


Data
----
* value + relation = data

>>> astronaut = ('Mark', 'Watney', 40, 185.5, 75.5)


Information
-----------
* data + context = information

>>> astronaut = {
...     'firstname': 'Mark',
...     'lastname': 'Watney',
...     'age': 40,
...     'height': 185.5,
...     'weight': 75.5,
... }


Use Case - 0x01
---------------
>>> commander = 'Melissa Lewis'
>>> botanist = 'Mark Watney'
>>> pilot = 'Rick Martinez'

>>> crew = ('Melissa Lewis', 'Mark Watney', 'Rick Martinez')

>>> crew = {
...     'commander': 'Melissa Lewis',
...     'botanist': 'Mark Watney',
...     'pilot': 'Rick Martinez',
... }
