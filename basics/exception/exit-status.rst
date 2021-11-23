Exit Status Code
================

Rationale
---------
* exit status ``0`` - no error
* any other exit status - error
* This will not work in Jupyter


Example
-------
>>> try:
...     float('hello')
... except ValueError:
...     print('Cannot type cast to float')
...     exit(1)
Traceback (most recent call last):
SystemExit: 1


Use Case - 0x01
---------------
* Tests
* CI/CD - Continuous Integration / Continuous Delivery

When all tests pass (without any error) exit code will be zero.
This is how CI/CD tools works. They check what exit status was
generated while executing particular steps of the CI/CD pipeline.

.. code-block:: console

    $ python -m doctest myscript.py
    $ echo $?
    0

In case of error the exit code will be non-zero. This is why CI/CD tool knows
if tests failed, therefore it yields an error for whole build or pipeline execution.

.. code-block:: console

    $ python -m doctest myscript.py
    **********************************************************************
    File "/home/watney/myscript.py", line 41, in myscript
    Failed example:
        1 + 2
    Expected:
        3
    Got:
        4
    **********************************************************************
    1 items had failures:
       1 of   2 in myscript
    ***Test Failed*** 1 failures.

    $ echo $?
    1
