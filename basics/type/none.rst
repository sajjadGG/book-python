Type None
=========


Definition
----------
* First letter capitalized, other are lower cased
* Empty (null) or unknown (unset) value
* It is not ``False`` value
* With ``if`` statements behaves like negative values

>>> data = None


Comparison (Identity Check)
---------------------------
* ``x is None`` - ``x`` is the same object as ``y``
* ``x is not None`` - ``x`` is not the same object as ``y``

>>> age = None
>>>
>>> age is None
True
>>> age is not None
False


Comparison (Value Check)
------------------------
* Do not use ``==`` or ``!=`` to check ``None`` values
* It works, but it is a subject to change

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
