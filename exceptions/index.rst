.. _Exceptions:

**********
Exceptions
**********


What are and why to use exceptions?
===================================
* Used when error occurs
* You can catch exception and handles erroneous situation
* Exception example situations:

    * File does not exists
    * Function argument is invalid
    * Network or database connection could not be established


Most common exceptions
======================
.. csv-table:: Most common exceptions
    :header-rows: 1
    :widths: 25, 75
    :file: data/exception-most-common.csv


Raising exceptions
==================
.. code-block:: python

    raise RuntimeError
    raise RuntimeError('Some message')

.. code-block:: python

    def apollo18():
        raise NotImplementedError('Mission dropped due to budget cuts')

    def apollo13():
        raise RuntimeError('Mid-flight Oxygen tank explosion')


    apollo18()
    apollo13()


Catching exceptions
===================
* ``try``
* ``except``
* ``else``
* ``finally``

.. code-block:: python

    def apollo13():
        raise RuntimeError('Mid-flight Oxygen tank explosion')


    try:
        apollo13()
    except RuntimeError:
        print('Houston we have a problem!')


.. code-block:: python

    try:
        with open(FILENAME, mode='w', encoding='utf-8') as file:
            content = file.read()
            print(content)

    except PermissionError as e:
        print('Permission denied')

    except OSError as e:
        print('File not found')

    except Exception as e:
        print('Other error')

    else:
        print('Success!')

    finally:
        print('Cleaning up')

.. warning:: Always catch exception!

    .. code-block:: python

        # Problematic code, catches also Ctrl-C
        while True:
            try:
                print('hello')
            except:
                continue

    .. code-block:: python

        # Good code, user can kill loop with Ctrl-C
        while True:
            try:
                print('hello')
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
.. code-block:: python

    import math


    class CotangentDoesNotExistsError(ArithmeticError):
        strerror = 'Cotangent for 180 degrees is infinite'
        errno = 10


    def cotangent(deg):
        if deg == 180:
            raise CotangentDoesNotExistsError

        radians = math.radians(degrees)
        return 1 / math.tan(radians)


    cotangent(180)
    # CotangentDoesNotExistsError: Cotangent for 180 degrees is infinite


Real life use-case
==================
.. code-block:: python

    from django.contrib.auth.models import User

    try:
        User.objects.get(username='jose-jimenez')
    except User.DoesNotExists:
        print('No such user')


``warnings``
============
.. code-block:: python

    import warnings


    def ariane5():
        warnings.warn('ariane5(), is deprecated, please use ariane6() instead', PendingDeprecationWarning)
        print('Launching rocket Ariane 5')

    def ariane6():
        print('Launching rocket Ariane 6')


    ariane5()
    ariane6()

.. code-block:: console

    $ python __notepad__.py

.. code-block:: console

    $ python -W all __notepad__.py
    __notepad__.py:5: PendingDeprecationWarning: ariane5(), is deprecated, please use ariane6() instead

