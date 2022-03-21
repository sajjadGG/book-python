Exception Assertion
===================


Important
---------
* Raises ``AssertionError`` if argument is ``False``
* Can have optional message
* Running Python with the ``-O`` optimization flag disables assert statements

Note the output of the following statements:

>>> data = [1, 2, 3]
>>>
>>> 1 in data
True
>>> 4 in data
False

In both examples from above, the output is visible. We can intercept it to the
variable, but we need to define it and store those values.

In the next example ``assert`` keywords allows to proceed with execution,
if only the assertion is ``True``.

>>> data = [1, 2, 3]
>>>
>>> assert 1 in data

So if there is an error (value ``4`` is not a member of ``data``),
then the exception is raised.

>>> data = [1, 2, 3]
>>>
>>> assert 4 in data
Traceback (most recent call last):
AssertionError

Assertions can have additional information, which can help with debugging:

>>> data = [1, 2, 3]
>>>
>>> assert 4 in data, '4 must be in data'
Traceback (most recent call last):
AssertionError: 4 must be in data


Sequence Assertion
------------------
>>> data = [1, 2, 3]
>>>
>>> assert type(data) is list
>>> assert all(type(x) is int for x in data)

>>> import sys
>>>
>>> assert sys.version_info >= (3, 9)
>>> assert sys.version_info >= (3, 9), 'Python 3.9+ required'


Assignments
-----------
.. literalinclude:: assignments/exception_assert_a.py
    :caption: :download:`Solution <assignments/exception_assert_a.py>`
    :end-before: # Solution
