Logic None
==========


Rationale
---------
* Empty (null) or unknown (unset) value

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>> age = None


Definition
----------
* First letter capitalized, other are lower cased

>>> data = None

It is not ``False`` value:

>>> None == False
False
>>>
>>> None is False
False


Type Casting
------------
With ``if`` statements behaves like negative values

>>> bool(False)
False
>>>
>>> bool(None)
False


Identity Check
--------------
* ``x is None`` - ``x`` is the same object as ``y``
* ``x is not None`` - ``x`` is not the same object as ``y``

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>> age = None
>>>
>>> age is None
True
>>> age is not None
False


Value Check
-----------
* Do not use ``==`` or ``!=`` to check ``None`` values
* It works, but it is a subject to change

>>> firstname = 'Mark'
>>> lastname = 'Watney'
>>> age = None
>>>
>>> age == None
True
>>> age != None
False


Assignments
-----------
.. literalinclude:: assignments/type_none_a.py
    :caption: :download:`Solution <assignments/type_none_a.py>`
    :end-before: # Solution
