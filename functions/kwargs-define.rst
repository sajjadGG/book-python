****************************************************
Defining function with arbitrary number of arguments
****************************************************


Recap information about function parameters
===========================================
.. code-block:: python

    def echo(a, b):
        print(a)
        print(b)


    echo(1, 2)       # pozycyjne
    echo(a=1, b=2)   # nazwane, kolejność nie ma znaczenia
    echo(b=2, a=1)   # nazwane, kolejność nie ma znaczenia
    echo(1, b=2)     # pozycyjne i nazwane
    echo(a=1, 2)     # SyntaxError: positional argument follows keyword argument


Arbitrary number of positional arguments
========================================
- ``*`` in this context, is not multiplication in mathematical sense
- ``args`` is a convention, but you can use any name
- ``*args`` is used for positional arguments
- ``*args`` unpacks to ``tuple``

.. code-block:: python

    def echo(*args):
        print(args)


    echo()                        # ()
    echo(1)                       # (1,)
    echo(2, 3)                    # (2, 3)
    echo('red', 2)                # ('red', 2)
    echo('red', 'green', 'blue')  # ('red', 'green', 'blue')

.. code-block:: python

    def echo(a, b, c=0, *args):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # ()


    echo(1, 2)

.. code-block:: python

    def echo(a, b, c=0, *args):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)


    echo(1, 2, 3, 4, 5, 6)


Arbitrary number of keyword arguments
=====================================
- ``**`` in this context, is not power in mathematical sense
- ``kwargs`` is a convention, but you can use any name
- ``**kwargs`` is used for keyword arguments
- ``**kwargs`` unpacks to ``dict``

.. code-block:: python

    def echo(**kwargs):
        print(kwargs)


    echo(a=10)                                      # {'a': 10}
    echo(color='red')                               # {'color': 'red'}
    echo(first_name='Jan', last_name='Twardowski')  # {'first_name': 'Jan', 'last_name': Twardowski}

.. code-block:: python

    def echo(a, b, c=0, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(kwargs)  # {}


    echo(1, 2)

.. code-block:: python

    def echo(a, b, c=0, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(kwargs)  # {'d':7, 'e': 8}


    echo(1, 2, d=7, e=8)

.. code-block:: python

    def echo(a, b, c=0, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(kwargs)  # {'d':7, 'e': 8}


    echo(1, 2, 3, d=7, e=8)


Arbitrary number of positional and named arguments
==================================================
.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {}


    echo(1, 2, 3, 4, 5, 6)

.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(args)    # ()
        print(kwargs)  # {'d':7, 'e': 8}


    echo(1, 2, d=7, e=8)

.. code-block:: python

    def echo(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {'d':7, 'e': 8}


    echo(1, 2, 3, 4, 5, 6, d=7, e=8)


Use cases
=========
.. code-block:: python

    def add(*args):
        total = 0

        for arg in args:
            total += arg

        return total


    add()            # 0
    add(1)           # 1
    add(1, 4)        # 5
    add(3, 1)        # 4
    add(1, 2, 3, 4)  # 10

.. code-block:: python
    :caption: Converts arguments between different units

    def kelvin_to_celsius(*degrees):
        return [x+273.15 for x in degrees]


    kelvin_to_celsius(1)
    # [274.15]

    kelvin_to_celsius(1, 2, 3, 4, 5)
    # [274.15, 275.15, 276.15, 277.15, 278.15]


.. code-block:: python
    :caption: Generate HTML list from function arguments

    def html_list(*args):
        print('<ul>')

        for element in args:
            print(f'<li>{element}</li>')

        print('</ul>')


    html_list('apple', 'banana', 'orange')
    # <ul>
    # <li>apple</li>
    # <li>banana</li>
    # <li>orange</li>
    # </ul>

.. code-block:: python
    :caption: Intuitive definition of ``print`` function

    def print(*values, sep=' ', end='\n', ...):
        return sep.join(values) + end


Assignments
===========

Numeric Values, positional only
-------------------------------
* Filename: ``kwargs_numeric_args.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min

#. Stwórz funkcję ``is_numeric``
#. Funkcja może przyjmować dowolną liczbę argumentów różnych typów
#. Numeryczną wartością jest ``int`` lub ``float``
#. Za pomocą ``isinstance()`` sprawdź wszystkie elementy listy:

    - Zwróć ``True`` jeżeli wszystkie są numeryczne
    - Zwróć ``False`` jeżeli którykolwiek jest innego typu

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Rzutowanie i konwersja typów

Numeric Values, positional and keyword
--------------------------------------
* Filename: ``kwargs_numeric_kwargs.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min

#. Stwórz funkcję ``is_numeric``
#. Funkcja może przyjmować dowolną liczbę argumentów różnych typów
#. Numeryczną wartością jest ``int`` lub ``float``
#. Za pomocą ``isinstance()`` sprawdź:

    - Zwróć ``True`` jeżeli wszystkie są numeryczne
    - Zwróć ``False`` jeżeli którykolwiek jest innego typu

#. Funkcja może przyjmować zarówno argumenty pozycyjne jak i nazwane

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Rzutowanie i konwersja typów
