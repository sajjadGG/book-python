.. _Control Flow Exceptions:

**********
Exceptions
**********


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
    :emphasize-lines: 2

    name = 'Jan'
    name.append('Twardowski')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
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
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # ModuleNotFoundError: No module named 'match'

IndexError
----------
.. highlights::
    * Sequence subscript is out of range

.. code-block:: python
    :caption: ``IndexError`` exception
    :emphasize-lines: 2

    DATA = ['a', 'b', 'c']
    DATA[100]
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # IndexError: list index out of range

KeyError
--------
.. highlights::
    * Dictionary key is not found

.. code-block:: python
    :caption: ``KeyError`` exception
    :emphasize-lines: 2

    DATA = {'a': 1, 'b': 2}
    DATA['x']
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # KeyError: 'x'

NameError
---------
.. highlights::
    * Local or global name is not found

.. code-block:: python
    :caption: ``KeyError`` exception
    :emphasize-lines: 1

    print(first_name)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
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
    # Traceback (most recent call last):
    #   File "<stdin>", line 1
    #     if True
    #           ^
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
    # Traceback (most recent call last):
    #   File "<stdin>", line 1
    #     print('My name...')
    #     ^
    # IndentationError: unexpected indent

TypeError
---------
.. highlights::
    * Operation or function is applied to an object of inappropriate type

.. code-block:: python
    :caption: ``TypeError`` exception
    :emphasize-lines: 7

    42 + 1
    # 43

    'a' + 'b'
    # 'ab'

    42 + 'a'
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'

    'a' + 42
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: can only concatenate str (not "int") to str

ValueError
----------
.. highlights::
    * Argument is right type but an inappropriate value

.. code-block:: python
    :caption: ``ValueError`` exception
    :emphasize-lines: 4

    float(1.2)
    # 1.2

    float(1,2)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # TypeError: float expected at most 1 arguments, got 2


Raising exceptions
==================
.. code-block:: python
    :caption: Raise Exception without message

    raise RuntimeError
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # RuntimeError

.. code-block:: python
    :caption: Exception with additional message

    raise RuntimeError('Some message')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # RuntimeError: Some message


Use case
========
.. code-block:: python

    temperature = input('Type temperature [Kelvin]: ')
    # Type temperature [Kelvin]: -10<ENTER>

    if float(temperature) < 0:
        raise ValueError
    # Traceback (most recent call last):
    #   File "<stdin>", line 2, in <module>
    # ValueError

.. code-block:: python

    temperature = input('Type Temperature [Kelvin]: ')

    if type(temperature) not in (float, int):
        raise TypeError('Argument ``a`` must be int or float')

    if float(temperature) < 0:
        raise ValueError('Kelvin temperature cannot be negative')

    print(temperature)

.. code-block:: python
    :emphasize-lines: 2

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')

    apollo13()
    # Traceback (most recent call last):
    #   File "<stdin>", line 5, in <module>
    #   File "<stdin>", line 2, in apollo13
    # RuntimeError: Oxygen tank explosion

.. code-block:: python
    :emphasize-lines: 2

    def apollo18():
        raise NotImplementedError('Mission dropped due to budget cuts')

    apollo18()
    # Traceback (most recent call last):
    #   File "<stdin>", line 5, in <module>
    #   File "<stdin>", line 2, in apollo18
    # NotImplementedError: Mission dropped due to budget cuts

Assertion
=========
* Raises ``AssertionError`` if argument is ``False``
* Can have optional message

.. code-block:: python
    :emphasize-lines: 2

    import sys

    assert sys.version_info >= (3, 8)
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # AssertionError

    assert sys.version_info >= (3, 8), "Python 3.8+ required."
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # AssertionError: Python 3.8+ required.


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
    #   File "<stdin>", line 1, in <module>
    # RuntimeError

.. code-block:: python
    :emphasize-lines: 4

    raise RuntimeError('Huston we have a problem')
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # RuntimeError: Huston we have a problem

.. code-block:: python
    :emphasize-lines: 6-8

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')

    apollo13()
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    #   File "<stdin>", line 2, in apollo13
    # RuntimeError: Oxygen tank explosion

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

.. code-block:: python
    :caption: Catch single exception
    :emphasize-lines: 7

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    try:
        apollo13()
    except RuntimeError:
        print('Houston we have a problem!')

    # Houston we have a problem!

.. code-block:: python
    :caption: Catch many exceptions with the same handling
    :emphasize-lines: 7

    def apollo13():
        raise RuntimeError('Oxygen tank explosion')


    try:
        apollo13()
    except (RuntimeError, TypeError, NameError):
        print('Houston we have a problem!')

    # Houston we have a problem!

.. code-block:: python
    :caption: Catch many exceptions with different handling

    try:
        with open(r'/tmp/iris.csv') as file:
            print(file.read())

    except FileNotFoundError:
        print('File does not exist')

    except PermissionError:
        print('Permission denied')

    # File does not exist

.. code-block:: python
    :caption: Exceptions logging
    :emphasize-lines: 8,9

    import logging


    def apollo13():
        raise RuntimeError('Oxygen tank explosion')

    try:
        apollo13()
    except RuntimeError as err:
        logging.error(err)

    # ERROR:root:Oxygen tank explosion


``else`` and ``finally``
========================
* ``else`` is executed when no exception occurred
* ``finally`` is executed always (even if there was exception)
* Used to close file, connection or transaction to database

.. code-block:: python
    :caption: ``else`` is executed when no exception occurred

    def apollo11():
        print('Try landing on the Moon')

    try:
        apollo11()
    except Exception:
        print('Abort')
    else:
        print('Landing a man on the Moon')

    # Try landing on the Moon
    # Landing a man on the Moon

.. code-block:: python
    :caption: ``finally`` is executed always (even if there was exception)

    def apollo11():
        print('Try landing on the Moon')

    try:
        apollo11()
    except Exception:
        print('Abort')
    finally:
        print('Returning safely to the Earth')

    # Try landing on the Moon
    # Returning safely to the Earth

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

    # Program P63 - Landing Manoeuvre Approach Phase
    # Yo're GO for landing
    # Returning safely to the Earth


Always catch exceptions!
========================
* ``Ctrl-C`` raises ``KeyboardInterrupt``

.. code-block:: python
    :caption: User cannot simply kill program with ``Ctrl-C``
    :emphasize-lines: 3

    while True:
        try:
            number = float(input('Type number: '))
        except:
            continue

.. code-block:: python
    :caption: User can kill program with ``Ctrl-C``
    :emphasize-lines: 4

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
* class which inherits from ``Exception``

.. code-block:: python

    class MyError(Exception):
        pass


    raise MyError
    # Traceback (most recent call last):
    #   File "<stdin>", line 5, in <module>
    # MyError

    raise MyError('More verbose description')
    # Traceback (most recent call last):
    #   File "<stdin>", line 5, in <module>
    # MyError: More verbose description

Use-case
--------
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


Exit Status Code
================
.. highlights::
    * exit with status ``0`` - no error
    * any other status - error

.. code-block:: python

    try:
        float('hello')
    except ValueError:
        print('Cannot type cast to float')
        exit(1)

    # Cannot type cast to float
    # [...] program exited with status 1

Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/exception_example.py`

:English:
    #. Ask user to input angle in degrees
    #. Cotangens for 180 degrees is infinite
    #. Define own exception
    #. If user typed angle equal to 180, raise your exception

:Polish:
    #. Poproś użytkownika o wprowadzenie kąta
    #. Cotangens dla konta 180 ma nieskończoną wartość
    #. Zdefiniuj własny wyjątek
    #. Jeżeli użytkownik wprowadził kąt równy 180, podnieś swój wyjątek

:Solution:
    .. literalinclude:: solution/exception_example.py
        :language: python

Raise Exception
---------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/exception_raise.py`

:English:
    #. Ask user to input age
    #. If user has less than 18 years
    #. Raise an exception ``PermissionError`` with message "Adults only"

:Polish:
    #. Poproś użytkownika o wprowadzenie wieku
    #. Jeżeli użytkownik ma mniej niż 18 lat
    #. Wyrzuć wyjątek ``PermissionError`` z komunikatem "Adults only"

Catch Exception
---------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/exception_catch.py`

:English:
    #. Ask user to input temperature in Kelvins
    #. Convert temperature to ``float``
    #. Print 'Invalid temperature' if cannot type cast to ``float``
    #. Print temperature

:Polish:
    #. Poproś użytkownika o wprowadzenie temperatury w Kelwinach
    #. Przekonwertuj temperaturę do ``float``
    #. Wypisz "Invalid temperature" jak nie można rzutować do ``float``
    #. Wypisz temperaturę

Define Exception
----------------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/exception_define.py`

:English:
    #. Ask user to input temperature in Kelvins
    #. User will always type proper ``int`` or ``float``
    #. Define exception for negative temperature
    #. Raise your exception if temperature is less than 0

:Polish:
    #. Poproś użytkownika o wprowadzenie temperatury w Kelwinach
    #. Użytkownik zawsze poda poprawne ``int`` lub ``float``
    #. Zdefiniuj wyjątek dla temperatur ujemnych
    #. Podnieś własny wyjątek jeżeli temperatura jest poniżej 0
