Exception Raise
===============


Rationale
---------
* Used when error occurs
* You can catch exception and handles erroneous situation
* Exception example situations:

    * File does not exists
    * No permissions to read file
    * Function argument is invalid type (ie. ``int('one')``)
    * Value is incorrect (ie. negative Kelvin temperature)
    * Network or database connection could not be established


Raising Exceptions
------------------
Raise Exception without message:

    >>> raise RuntimeError
    Traceback (most recent call last):
    RuntimeError

Exception with additional message:

    >>> raise RuntimeError('Some message')
    Traceback (most recent call last):
    RuntimeError: Some message


Example
-------
We want to check if Kelvin temperature given by user is not negative.
Note that Kelvin temperatures below zero doesn't exist, hence it's an absolute
scale.

In order to do so, we need to ask user to input value. Let's assume user input
``-1``. Remember, ``input()`` function always returns ``str`` and you have to
convert it manually.

.. testsetup::

    # Mock input() built-in function
    from unittest.mock import MagicMock
    input = MagicMock(return_value='-1')

We need to check if the temperature is not negative. If temperature is 0 or
above, it is ok, and we can proceed with program execution. However if the
temperature is below zero... Then we should warn user about problem and exit
program. This is why we have exceptions. We can break execution of a program
in erroneous situations.

    >>> temperature = input('Type temperature: ')  # User inputs: -1
    >>> temperature = float(temperature)
    >>>
    >>> if temperature > 0.0:
    ...     print('Temperature is valid')
    ... else:
    ...     raise ValueError('Kelvin cannot be negative')
    Traceback (most recent call last):
    ValueError: Kelvin cannot be negative

Good software communicates well with programmer. Exceptions are common language
to talk about problems and not-nominal (abnormal) situations in your code.

    >>> def check(temperature):
    ...     if type(temperature) not in {float, int}:
    ...         raise TypeError('Temperature must be int or float')
    ...     if temperature < 0:
    ...         raise ValueError('Kelvin temperature cannot be negative')
    ...     return temperature


Use Case
--------
    >>> def apollo13():
    ...     raise RuntimeError('Oxygen tank explosion')
    >>>
    >>>
    >>> apollo13()
    Traceback (most recent call last):
    RuntimeError: Oxygen tank explosion

    >>> def apollo18():
    ...     raise NotImplementedError('Mission dropped due to budget cuts')
    >>>
    >>>
    >>> apollo18()
    Traceback (most recent call last):
    NotImplementedError: Mission dropped due to budget cuts


Assignments
-----------
.. literalinclude:: assignments/exception_raise_a.py
    :caption: :download:`Solution <assignments/exception_raise_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/exception_raise_b.py
    :caption: :download:`Solution <assignments/exception_raise_b.py>`
    :end-before: # Solution
