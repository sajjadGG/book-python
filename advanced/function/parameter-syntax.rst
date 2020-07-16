****************
Parameter Syntax
****************


Recap
=====
.. code-block:: python

    def echo(a, b, c=3):
         print(a, b, c)

    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # 1 2 3
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # 1 2 3


Keyword-only parameters
=======================
* All parameters after ``*`` must be keyword-only

.. code-block:: python

    def echo(a, *, b, c=3):
        print(a, b, c)

    echo(1, 2)              # TypeError: echo() takes 1 positional argument but 2 were given
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required keyword-only argument: 'b'
    echo(1, 2, 3)           # TypeError: echo() takes 1 positional argument but 3 were given
    echo(1, 2, c=3)         # TypeError: echo() takes 1 positional argument but 2 positional arguments (and 1 keyword-only argument) were given
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # 1 2 3


Positional-only parameters
==========================
.. versionadded:: Python 3.8
    See :pep:`570` Python Positional-Only Parameters

* All parameters before ``/`` must be positional-only

.. code-block:: python

    def echo(a, /, b, c=3):
        print(a, b, c)

    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # 1 2 3
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'


Positional and Keyword parameters
=================================
.. code-block:: python

    def echo(a, /, b, *, c=3):
        print(a, b, c)

    echo(1, 2)              # 1 2 3
    echo(1, b=2)            # 1 2 3
    echo(1, c=3)            # TypeError: echo() missing 1 required positional argument: 'b'
    echo(1, 2, 3)           # TypeError: echo() takes 2 positional arguments but 3 were given
    echo(1, 2, c=3)         # 1 2 3
    echo(1, b=2, c=3)       # 1 2 3
    echo(a=1, b=2, c=3)     # TypeError: echo() got some positional-only arguments passed as keyword arguments: 'a'


Examples
========
.. code-block:: python

    def pow(x, y, z=None, /):
        ...

.. code-block:: python

    def quantiles(dist, /, *, n=4, method='exclusive')
        ...

.. code-block:: python

     def add(a, b, /, **kwargs):
        ...


Assignments
===========

Function Parameter Syntax Args
------------------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_parameter_syntax_args.py`

:English:
    #. Create function ``take_damage``
    #. Function takes one argument ``dmg``
    #. Argument must be passed only as positional
    #. Function does nothing
    #. Test function by running with keyword arguments
    #. Test function by running with positional arguments

:Polish:
    #. Stwórz funckję ``take_damage``
    #. Funkcja przyjmuje jeden argument ``dmg``
    #. Argument można podawać tylko pozycyjnie
    #. Funkcja nic nie robi
    #. Przetestuj funkcję uruchamiając z nazwanymi parametrami
    #. Przetestuj funkcję uruchamiając z pozycyjnymi parametrami

Function Parameter Syntax Kwargs
--------------------------------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/function_parameter_syntax_kwargs.py`

:English:
    #. Create function ``set_position``
    #. Function takes two arguments ``x`` and ``y``
    #. Arguments must be passed only as keywords
    #. Function does nothing
    #. Test function by running with keyword arguments
    #. Test function by running with positional arguments

:Polish:
    #. Stwórz funckję ``set_position``
    #. Funkcja przyjmuje dwa argumenty ``x`` i ``y``
    #. Argumenty można podawać tylko nazwanie (keyword)
    #. Funkcja nic nie robi
    #. Przetestuj funkcję uruchamiając z nazwanymi parametrami
    #. Przetestuj funkcję uruchamiając z pozycyjnymi parametrami
