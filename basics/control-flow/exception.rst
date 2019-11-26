.. _Control Flow Exceptions:

***********************
Control Flow Exceptions
***********************


What are and why to use exceptions?
===================================
.. highlights::
    * Used when error occurs
    * You can catch exception and handles erroneous situation
    * Exception example situations:

        * File does not exists
        * Function argument is invalid
        * Network or database connection could not be established


Most common exceptions
======================

AttributeError
--------------
.. highlights::
    * Attribute reference or assignment fails

.. code-block:: python
    :caption: ``AttributeError`` exception
    :emphasize-lines: 3

    name = 'Jan'

    name.append('Twardowski')
    # AttributeError: 'str' object has no attribute 'append'

ImportError, ModuleNotFoundError
--------------------------------
.. highlights::
    * Module could not be located

.. code-block:: python
    :caption: ``ModuleNotFoundError`` exception
    :emphasize-lines: 2

    import math
    import match
    # ModuleNotFoundError

IndexError
----------
.. highlights::
    * Sequence subscript is out of range

.. code-block:: python
    :caption: ``IndexError`` exception
    :emphasize-lines: 3

    DATA = ['a', 'b', 'c']

    DATA[100]
    # IndexError: list index out of range

KeyError
--------
.. highlights::
    * Dictionary key is not found

.. code-block:: python
    :caption: ``KeyError`` exception
    :emphasize-lines: 3

    DATA = {'a': 1, 'b': 2}

    DATA['x']
    # KeyError: 'x'

NameError
---------
.. highlights::
    * Local or global name is not found

.. code-block:: python
    :caption: ``KeyError`` exception
    :emphasize-lines: 1

    print(first_name)
    # NameError: name 'first_name' is not defined

SyntaxError
-----------
.. highlights::
    * Parser encounters a syntax error

.. code-block:: python
    :caption: ``SyntaxError`` exception
    :emphasize-lines: 1

    if True
        print('Yes')

    # SyntaxError: invalid syntax

IndentationError
----------------
.. highlights::
    * Syntax errors related to incorrect indentation

.. code-block:: python
    :caption: ``IndentationError`` exception
    :emphasize-lines: 3

    if True:
       print('Hello!')
        print('My name...')
       print('Jose Jimenez')

    # IndentationError: unexpected indent

TypeError
---------
.. highlights::
    * Operation or function is applied to an object of inappropriate type

.. code-block:: python
    :caption: ``TypeError`` exception
    :emphasize-lines: 2

    42 + 'Answer to the Ultimate Question of Life, the Universe, and Everything'
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

ValueError
----------
.. highlights::
    * Argument is right type but an inappropriate value

.. code-block:: python
    :caption: ``ValueError`` exception
    :emphasize-lines: 1

    float('Jan Twardowski')
    # ValueError: could not convert string to float: 'Jan Twardowski'


Raising exceptions
==================

Raise Exception without message
-------------------------------
.. code-block:: python
    :caption: Raise Exception without message

    raise RuntimeError

Exception with additional message
---------------------------------
.. code-block:: python
    :caption: Exception with additional message

    raise RuntimeError('Some message')

Use case
--------
.. code-block:: python

    def add_numbers(a, b):
        if not isinstance(a, (float, int)):
            raise ValueError('Argument ``a`` must be int or float')

        if not isinstance(b, (float, int)):
            raise ValueError('Argument ``b`` must be int or float')

        return a + b


.. code-block:: python
    :emphasize-lines: 2

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    apollo13()

.. code-block:: python
    :emphasize-lines: 2

    def apollo18():
        raise NotImplementedError('Mission dropped due to budget cuts')


    apollo18()


Traceback
=========

Traceback analysis
------------------
.. highlights::
    * Stacktrace is 8 levels deep, it's not Java's 200 ;)

.. code-block:: python
    :emphasize-lines: 4

    raise RuntimeError
    # Traceback (most recent call last):
    #   File "<input>", line 1, in <module>
    # RuntimeError

.. code-block:: python
    :emphasize-lines: 4

    raise RuntimeError('Huston we have a problem')
    # Traceback (most recent call last):
    #   File "<input>", line 1, in <module>
    # RuntimeError: Huston we have a problem

.. code-block:: python
    :emphasize-lines: 11-15

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')

    apollo13()
    # Traceback (most recent call last):
    #   File "<input>", line 1, in <module>
    #   File "/Applications/PyCharm 2019.2 EAP.app/Contents/helpers/pydev/_pydev_bundle/pydev_umd.py", line 197, in runfile
    #     pydev_imports.execfile(filename, global_vars, local_vars)  # execute the script
    #   File "/Applications/PyCharm 2019.2 EAP.app/Contents/helpers/pydev/_pydev_imps/_pydev_execfile.py", line 18, in execfile
    #     exec(compile(contents+"\n", file, 'exec'), glob, loc)
    #   File "/home/python/my_script.py", line 4, in <module>
    #     apollo13()
    #   File "/home/python/my_script.py", line 2, in apollo13
    #     raise RuntimeError('Oxygen tank explosion')
    # RuntimeError: Oxygen tank explosion

Change verbosity level
----------------------
.. highlights::
    * Change level with ``sys.tracebacklimit``
    * From time to time you can have problems somewhere in the middle, but it's rare
    * Last lines are the most important, in most cases error is there

.. code-block:: python
    :emphasize-lines: 1,2

    import sys
    sys.tracebacklimit = 2


    def apollo13():
        raise RuntimeError('Oxygen tank explosion')

    apollo13()
    # Traceback (most recent call last):
    #   File "/home/python/my_script.py", line 4, in <module>
    #     apollo13()
    #   File "/home/python/my_script.py", line 2, in apollo13
    #     raise RuntimeError('Oxygen tank explosion')
    # RuntimeError: Oxygen tank explosion


Catching exceptions
===================
.. highlights::
    * ``try``
    * ``except``
    * ``else``
    * ``finally``

Catch single exception
----------------------
.. code-block:: python
    :emphasize-lines: 7

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    try:
        apollo13()
    except RuntimeError:
        print('Houston we have a problem!')

Catch many exceptions with the same handling
--------------------------------------------
.. code-block:: python
    :emphasize-lines: 7

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    try:
        apollo13()
    except (RuntimeError, TypeError, NameError):
        print('Houston we have a problem!')

Catch many exceptions with different handling
---------------------------------------------
.. code-block:: python

    try:
        with open(r'/tmp/iris.csv') as file:
            print(file.read())

    except FileNotFoundError:
        print('File does not exist')

    except PermissionError:
        print('Permission denied')

Exceptions logging
------------------
.. code-block:: python
    :emphasize-lines: 8,9

    import logging


    def apollo13():
        raise RuntimeError('Oxygen tank explosion')

    try:
        apollo13()
    except RuntimeError as err:
        logging.error(err)

``else``
--------
.. highlights::
    * Executed when no exception occurred

.. code-block:: python

    def apollo11():
        print('Try landing on the Moon')

    try:
        apollo11()
    except Exception:
        print('Abort')
    else:
        print('Landing a man on the Moon')

``finally``
-----------
.. highlights::
    * Executed always (even if there was exception)
    * Used to close file, connection or transaction to database

.. code-block:: python

    def apollo11():
        print('Try landing on the Moon')

    try:
        apollo11()
    except Exception:
        print('Abort')
    finally:
        print('Returning safely to the Earth')

``else`` and ``finally``
------------------------
.. code-block:: python

    def apollo11():
        print('Program P63 - Landing Manoeuvre Approach Phase')
        raise RuntimeError('1201 Alarm')
        raise RuntimeError('1202 Alarm')
        print('Contact lights')
        print('The Eagle has landed!')
        print("That's one small step for [a] man, one giant leap for mankind.")

    try:
        apollo11()
    except RuntimeError:
        print("Yo're GO for landing")
    except Exception:
        print('Abort')
    else:
        print('Landing a man on the Moon')
    finally:
        print('Returning safely to the Earth')

Always catch exceptions!
------------------------
.. code-block:: python
    :emphasize-lines: 6

    # Problematic code which catches 'Ctrl-C'
    # User cannot simply kill program
    while True:
        try:
            number = float(input('Type number: '))
        except:
            continue

.. code-block:: python
    :emphasize-lines: 5

    # User can kill program with 'Ctrl-C'
    while True:
        try:
            number = float(input('Type number: '))
        except Exception:
            continue


Exception hierarchy
===================
.. code-block:: text

    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          |    +-- FloatingPointError
          |    +-- OverflowError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- BufferError
          +-- EOFError
          +-- ImportError
          +-- LookupError
          |    +-- IndexError
          |    +-- KeyError
          +-- MemoryError
          +-- NameError
          |    +-- UnboundLocalError
          +-- OSError
          |    +-- BlockingIOError
          |    +-- ChildProcessError
          |    +-- ConnectionError
          |    |    +-- BrokenPipeError
          |    |    +-- ConnectionAbortedError
          |    |    +-- ConnectionRefusedError
          |    |    +-- ConnectionResetError
          |    +-- FileExistsError
          |    +-- FileNotFoundError
          |    +-- InterruptedError
          |    +-- IsADirectoryError
          |    +-- NotADirectoryError
          |    +-- PermissionError
          |    +-- ProcessLookupError
          |    +-- TimeoutError
          +-- ReferenceError
          +-- RuntimeError
          |    +-- NotImplementedError
          |    +-- RecursionError
          +-- SyntaxError
          |    +-- IndentationError
          |         +-- TabError
          +-- SystemError
          +-- TypeError
          +-- ValueError
          |    +-- UnicodeError
          |         +-- UnicodeDecodeError
          |         +-- UnicodeEncodeError
          |         +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
               +-- ImportWarning
               +-- UnicodeWarning
               +-- BytesWarning
               +-- ResourceWarning


Defining own exceptions
=======================

Syntax
------
* class which inherits from ``Exception``

.. code-block:: python

    class MyError(Exception):
        pass


    raise MyError
    raise MyError('More verbose description')

Example
-------
.. code-block:: python
    :emphasize-lines: 4-5, 10, 16-17

    import math


    class CotangentDoesNotExistsError(Exception):
        pass


    def cotangent(degrees):
        if degrees == 180:
            raise CotangentDoesNotExistsError('Cotangent for 180 degrees is infinite')

        radians = math.radians(degrees)
        return 1 / math.tan(radians)


    cotangent(180)
    # CotangentDoesNotExistsError: Cotangent for 180 degrees is infinite


Real life use-case
==================
.. code-block:: python
    :emphasize-lines: 9

    from django.contrib.auth.models import User

    try:
        user = User.objects.get(
            username=POST.get('username'),
            password=POST.get('password'),
        )
    except User.DoesNotExists:
        print('Sorry, no such user in database')


Assignments
===========
.. todo:: Create assignments
