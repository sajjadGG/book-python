Boolean Empty
=============


Rationale
---------
* empty ``bool()`` or ``False``
* empty ``int()`` or ``0``
* empty ``float()`` or ``0.0``
* empty ``complex()`` or ``0+0j`` or ``0.0+0.0j``
* empty ``str()`` or ``''``
* empty ``tuple()`` or ``()``
* empty ``list()`` or ``[]``
* empty ``set()``
* empty ``frozenset()``
* empty ``dict()`` or ``{}``
* ``None``


Scalar
------
* empty ``bool()`` or ``False``
* empty ``int()`` or ``0``
* empty ``float()`` or ``0.0``
* empty ``complex()`` or ``0+0j`` or ``0.0+0.0j``
* empty ``str()`` or ``''``
* ``None``

>>> data = 0
>>>
>>> if data:
...     print('Not empty')
>>>
>>> if not data:
...     print('Empty')
Empty

>>> data = ''
>>>
>>> if data:
...     print('Not empty')
>>>
>>> if not data:
...     print('Empty')
Empty

>>> data = None
>>>
>>> if data:
...     print('Not empty')
>>>
>>> if not data:
...     print('Empty')
Empty


Sequence
--------
* empty ``tuple()`` or ``()``
* empty ``list()`` or ``[]``
* empty ``set()``
* empty ``frozenset()``

>>> data = ()
>>>
>>> if data:
...     print('Not empty')
>>>
>>> if not data:
...     print('Empty')
Empty

>>> data = []
>>>
>>> if data:
...     print('Not empty')
>>>
>>> if not data:
...     print('Empty')
Empty

>>> data = set()
>>>
>>> if data:
...     print('Not empty')
>>>
>>> if not data:
...     print('Empty')
Empty


Mapping
-------
* empty ``dict()`` or ``{}``

>>> data = {}
>>>
>>> if data:
...     print('Not empty')
>>>
>>> if not data:
...     print('Empty')
Empty


Assignments
-----------
.. todo:: Create assignments
