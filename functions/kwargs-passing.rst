**********************
Passing many arguments
**********************


Arbitrary number of positional arguments
========================================
- ``*`` in this context, is not multiplication in mathematical sense
- ``args`` is a convention, but you can use any name
- ``*args`` is used for positional arguments
- ``*args`` unpacks from ``tuple``, ``list`` or ``set``

.. code-block:: python

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    echo(1, 2)

.. code-block:: python

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    args = (1, 2)
    echo(*args)


Arbitrary number of keyword arguments
=====================================
- ``**`` in this context, is not power in mathematical sense
- ``kwargs`` is a convention, but you can use any name
- ``**kwargs`` is used for keyword arguments
- ``**kwargs`` unpacks from ``dict``

.. code-block:: python

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    echo(a=1, b=2)

.. code-block:: python

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    kwargs = {'a': 1, 'b': 2}
    echo(**kwargs)


Arbitrary number of positional and keyword arguments
====================================================
.. code-block:: python

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    echo(1, b=2)

.. code-block:: python

    def echo(a, b, c=0):
        print(a)    # 1
        print(b)    # 2
        print(c)    # 0

    args = (1,)
    kwargs = {'b': 2}

    echo(*args, **kwargs)


Examples
========

Creating complex numbers
------------------------
.. code-block:: python

    complex(real=3, imag=5)
    # (3+5j)

.. code-block:: python

    kwargs = {'real': 3, 'imag': 5}
    complex(**kwargs)
    # (3+5j)

Vectors
-------
.. code-block:: python

    def echo(x, y, z):
        print(x)    # 1
        print(y)    # 0
        print(z)    # 1

    vector = (1, 0, 1)

    echo(*vector)


Use cases
=========

Print formatting
----------------
* Now f-string formatting is preferred

.. code-block:: python

    name = 'Jan Twardowski'
    agency = 'POLSA'

    output = "{agency} astronaut {name} first on the Moon".format(**locals())
    print(output)
    # POLSA astronaut Jan Twardowski first on the Moon

Print formatting in classes
---------------------------
* Now f-string formatting is preferred

.. code-block:: python

    class Osoba:
        first_name = 'Jan'
        last_name = 'Twardowski'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)

.. code-block:: python

    class Osoba:
        first_name = 'Jan'
        last_name = 'Twardowski'

        def __str__(self):
            return '{first_name} {last_name}'.format(first_name='Jan', last_name='Twardowski')

.. code-block:: python

    class Osoba:
        first_name = 'Jan'
        last_name = 'Twardowski'

        def __str__(self):
            return f'{self.first_name} {self.last_name}'

Common configuration
--------------------
.. code-block:: python

    def draw_line(x, y, color, style, width, markers):
        ...


    draw_line(1, 2, color='red', style='dashed', width='2px', markers='disc')
    draw_line(3, 4, color='red', style='dashed', width='2px', markers='disc')
    draw_line(5, 6, color='red', style='dashed', width='2px', markers='disc')

.. code-block:: python
    :caption: Podawanie parametrów do funkcji

    def draw_chart(a, b, color, style, width, markers):
        ...


    config = {
        'color': 'czerwony',
        'style': 'dashed',
        'width': '2px',
        'markers': 'disc',
    }

    draw_line(1, 2, **config)
    draw_line(3, 4, **config)
    draw_line(5, 6, **config)

Placeholder class
-----------------
.. code-block:: python

    DATA = [
        {"sepal_length": 6.0, "sepal_width": 3.4, "petal_length": 4.5, "petal_width": 1.6, "species": "versicolor"},
        {"sepal_length": 4.9, "sepal_width": 3.1, "petal_length": 1.5, "petal_width": 0.1, "species": "setosa"},
    ]

    class Iris:
        def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species

    flowers = []

    for row in DATA:
        flower = Iris(**row)
        flowers.append(flower)

.. code-block:: python

    class Kontakt:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)


    kontakt1 = Kontakt(imie='Jan', nazwisko='Twardowski')
    kontakt1.imie           # Jan
    kontakt1.nazwisko       # 'Twardowski'

    kontakt2 = Kontakt(sepal_length=6.0, sepal_width=3.4, nazwisko='Twardowski')
    kontakt2.sepal_length   # 6.0
    kontakt2.nazwisko       # 'Twardowski'


    DATA = {"sepal_length": 6.0, "sepal_width": 3.4, "petal_length": 4.5, "petal_width": 1.6, "species": "versicolor"},
    kontakt3 = Kontakt(**DATA)
    kontakt3.species
    # 'versicolor'


    DATA = [
        {"sepal_length": 6.0, "sepal_width": 3.4, "petal_length": 4.5, "petal_width": 1.6, "species": "versicolor"},
        {"sepal_length": 4.9, "sepal_width": 3.1, "petal_length": 1.5, "petal_width": 0.1, "species": "setosa"},
    ]
    for kontakt in DATA:
        k = Kontakt(**DATA)
        k.species

    # 'versicolor'
    # 'setosa'

Calling function with all variables from higher order function
--------------------------------------------------------------
.. code-block:: python

    def show(*args, **kwargs):
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')

    def function(a, b, c=0):
        x = 4
        y = 5

        show(**locals())

    function(1, 2)
    # args: ()
    # kwargs: {'a': 1, 'b': 2, 'c': 0, 'x': 4, 'y': 5}

Proxy functions
---------------
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
    :caption: Positional arguments in ``args`` can be passed to proxied function after named parameters!

    def my_csv(file, *args, **kwargs):
        return pd.read_csv(
            file,
            encoding='utf-8',
            skip_blank_lines=True,
            *args,
            **kwargs)

    my_csv('iris.csv', ',', verbose=True)




Init
----
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


Decorators
----------
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

Iris
----
* Filename: ``kwargs_iris.py``
* Lines of code to write: 15 lines
* Estimated time of completion: 20 min
* Input data: https://raw.githubusercontent.com/AstroMatt/book-python/master/functions/data/iris.csv

#. Otwórz link w przeglądarce i skopiuj zawartość do pliku na dysku o nazwie ``iris.csv``
#. Z pliku ``iris.csv`` odseparuj nagłówek i dane
#. Z nagłówka odrzuć rekord ``species``
#. Stwórz funkcję ``print_iris(species, **pomiary)``, która wyświetli zawartość wszystkich argumentów za pomocą ``locals()``
#. Dla każdego rekordu w danych:

    #. Usuń białe spacje
    #. Podziel po przecinku ``,``
    #. Wyniki podziału zapisz do dwóch zmiennych:

        * ``pomiary: Dict[str, float]`` - pomiary
        * ``gatunek: str`` - nazwa gatunku

    #. Odpalaj funkcję ``print_iris()``, podając wartości ``pomiary`` i ``gatunek``
    #. ``gatunek`` ma być podany pozycyjnie
    #. ``pomiary`` mają być podane nazwanie

