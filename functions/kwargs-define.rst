*****************************
Functions with many arguments
*****************************


Operands ``*`` and ``**``
=========================
- This is not multiplication or power!
- ``*args`` - positional arguments, unpacks to ``tuple``
- ``**kwargs`` - keyword arguments, unpacks to ``dict``


Recap information about function parameters
===========================================
.. code-block:: python

    def add(a, b):
        return a + b


    add(1, 2)       # pozycyjne
    add(a=1, b=2)   # nazwane, kolejność nie ma znaczenia
    add(b=2, a=1)   # nazwane, kolejność nie ma znaczenia
    add(1, b=2)     # pozycyjne i nazwane


Defining function with many arguments
=====================================

Many positional arguments
-------------------------
.. code-block:: python

    def show(*args):
        print(args)


    show()                        # ()
    show(1)                       # (1,)
    show(2, 3)                    # (2, 3)
    show('red', 2)                # ('red', 2)
    show('red', 'green', 'blue')  # ('red', 'green', 'blue')

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

Many named arguments
--------------------
.. code-block:: python

    def show(**kwargs):
        print(kwargs)


    show(a=10)                                      # {'a': 10}
    show(color='red')                               # {'color': 'red'}
    show(first_name='Jan', last_name='Twardowski')  # {'first_name': 'Jan', 'last_name': Twardowski}

Many named and positional arguments
-----------------------------------
.. code-block:: python

    def show(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {}


    show(1, 2, 3, 4, 5, 6)

.. code-block:: python

    def show(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 0
        print(args)    # ()
        print(kwargs)  # {'d':7, 'e': 8}


    show(1, 2, d=7, e=8)

.. code-block:: python

    def show(a, b, c=0, *args, **kwargs):
        print(a)       # 1
        print(b)       # 2
        print(c)       # 3
        print(args)    # (4, 5, 6)
        print(kwargs)  # {'d':7, 'e': 8}


    show(1, 2, 3, 4, 5, 6, d=7, e=8)


Use cases
=========
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

.. code-block:: python
    :caption: One of the most common use of ``*args``, ``**kwargs`` is for proxy methods.

    # ``read_csv`` is a function from ``pandas`` library
    def read_csv(filepath_or_buffer, sep=', ', delimiter=None,
                 header='infer', names=None, index_col=None,
                 usecols=None, squeeze=False, prefix=None,
                 mangle_dupe_cols=True, dtype=None, engine=None,
                 converters=None, true_values=None, false_values=None,
                 skipinitialspace=False, skiprows=None, nrows=None,
                 na_values=None, keep_default_na=True, na_filter=True,
                 verbose=False, skip_blank_lines=True, parse_dates=False,
                 infer_datetime_format=False, keep_date_col=False,
                 date_parser=None, dayfirst=False, iterator=False,
                 chunksize=None, compression='infer', thousands=None,
                 decimal=b'.', lineterminator=None, quotechar='"',
                 quoting=0, escapechar=None, comment=None, encoding=None,
                 dialect=None, tupleize_cols=None, error_bad_lines=True,
                 warn_bad_lines=True, skipfooter=0, doublequote=True,
                 delim_whitespace=False, low_memory=True, memory_map=False,
                 float_precision=None):
        ...

    def my_csv(file, decimal=b',', *args, **kwargs):
        return read_csv(
            filepath_or_buffer=file,
            decimal=decimal,
            encoding='utf-8',
            usecols=['Petal length', 'Species'],
            skip_blank_lines=True,
            *args,
            **kwargs)

    my_csv('iris.csv', decimal='.', verbose=True)

.. code-block:: python
    :caption: One of the most common use of ``*args``, ``**kwargs`` is for proxy methods.

    class Point2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y


    class Point3D(Point2D):
        def __init__(self, z, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.z = z

.. code-block:: python

    from functools import wraps

    def login_required(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if user.is_logged():
                return f(*args, **kwargs)
            else:
                print('Permission denied')
        return wrapper


Assignments
===========

Numeric Values
--------------
* Filename: ``kwargs_numeric.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min

#. Stwórz funkcję ``is_numeric``
#. Funkcja może przyjmować dowolną ilość argumentów
#. Za pomocą funkcji ``isinstance()`` sprawdź czy wszystkie argumenty są ``int`` albo ``float``:

    - Jeżeli wszystkie są ``int`` albo ``float``, to zwróć ``True``
    - Jeżeli którykolwiek nie jest, to zwróć ``False``

:The whys and wherefores:
    * Definiowanie i uruchamianie funkcji
    * Sprawdzanie przypadków brzegowych (niekompatybilne argumenty)
    * Parsowanie argumentów funkcji
    * Rzutowanie i konwersja typów
