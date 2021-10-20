Logic None
==========


Rationale
---------
* Empty (null) or unknown (unset) value
* It is not ``False`` value


Definition
----------
* First letter capitalized, other are lower cased

>>> data = None


None, Null, Nil
---------------
>>> data = none
Traceback (most recent call last):
NameError: name 'none' is not defined
>>>
>>> data = NONE
Traceback (most recent call last):
NameError: name 'NONE' is not defined

>>> data = null
Traceback (most recent call last):
NameError: name 'null' is not defined
>>>
>>> data = Null
Traceback (most recent call last):
NameError: name 'Null' is not defined
>>>
>>> data = NULL
Traceback (most recent call last):
NameError: name 'NULL' is not defined

>>> data = nil
Traceback (most recent call last):
NameError: name 'NIL' is not defined
>>>
>>> data = NIL
Traceback (most recent call last):
NameError: name 'NIL' is not defined


Identity Check
--------------
* ``x is None`` - ``x`` is the same object as ``y``
* ``x is not None`` - ``x`` is not the same object as ``y``

>>> data = None
>>>
>>>
>>> data is None
True
>>>
>>> data is not None
False


Value Check
-----------
* Do not use ``==`` or ``!=`` to check ``None`` values
* It works, but it is a subject to change


>>> data = None
>>>
>>>
>>> data == None
True
>>>
>>> data != None
False


Type Casting
------------
With ``if`` statements behaves like negative values

>>> bool(None)
False

>>> bool(False)
False
>>>
>>> None == False
False
>>>
>>> None is False
False


Use Case
--------
>>> firstname = 'Melissa'
>>> lastname = 'Lewis'
>>> age = None
>>>
>>> age is None
True


Assignments
-----------
.. literalinclude:: assignments/type_none_a.py
    :caption: :download:`Solution <assignments/type_none_a.py>`
    :end-before: # Solution
