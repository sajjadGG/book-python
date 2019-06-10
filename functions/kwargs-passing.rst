**********************
Passing many arguments
**********************


Operators ``*`` i ``**``
========================
- This is not multiplication or power!
- ``*args`` - positional arguments, unpacks ``tuple``, ``list`` or ``set``
- ``**kwargs`` - keyword arguments, unpacks ``dict``


Unpacking sequences
===================
* ``*`` unpacks ``tuple``, ``list`` or ``set``

.. code-block:: python

    complex(3, 5)

.. code-block:: python

    args = (3, 5)
    complex(*args)


Unpacking ``dict``
==================
* ``**`` unpacks ``dict``

.. code-block:: python

    complex(real=3, imag=5)

.. code-block:: python

    kwargs = {'real': 3, 'imag': 5}
    complex(**kwargs)

Use Case
--------
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


Przekazywanie do funkcji zmiennej ilości parametrów
===================================================

Passing sequence as positional arguments
----------------------------------------
.. code-block:: python

    def show(x, y, z):
        print(x, y, z)

    vector = (1, 0, 1)

    # show(1, 0, 1)
    show(*vector)
    # 1, 0, 1

.. code-block:: python

    def show(a, b, c=0):
        print(locals())

    show(1, 2, 3)
    # {'a': 1, 'b': 2, 'c': 3}

    dane = (1, 2, 3)
    show(*dane)
    # {'a': 1, 'b': 2, 'c': 3}

    dane = (1, 2)
    show(*dane)
    # {'a': 1, 'b': 2, 'c': 0}

.. code-block:: python

    def show(a, b, c=0, *args):
        print(locals())

    dane = (1, 2, 3, 4)
    show(*dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4,)}

    dane = (1, 2, 3, 4, 5, 6, 7)
    show(*dane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6, 7)}

    show(1, 2)
    # {'a': 1, 'b': 2, 'c': 0, 'args': ()}

Passing ``dict`` as named argument
----------------------------------
.. code-block:: python
    :caption: Named parameters don't care about order

    def show(x, y, z):
        print(x, y, z)

    vector = {'z': 1, 'y': 0, 'x': 1}

    # show(z=1, y=0, x=1)
    show(**vector)
    # 1, 0, 1

.. code-block:: python

    def show(a, b, c=0, **kwargs):
        print(locals())

    dane = {'x': 77, 'y': 99, 'a': 7}
    show(1, 2, 3, **dane)
    # TypeError: show() got multiple values for argument 'a'

.. code-block:: python

    def show(a, b, c=0, **kwargs):
        print(locals())

    show(1, 2, x=77, y=99)
    # {'a': 1, 'b': 2, 'c': 0, 'kwargs': {'x': 77, 'y': 99}}

    show(1, 2, x=77, y=99, c=7)
    # {'a': 1, 'b': 2, 'c': 7, 'kwargs': {'x': 77, 'y': 99}}

    dane = {'x': 77, 'y': 99}
    show(1, 2, 3, **dane)
    # {'a': 1, 'b': 2, 'c': 3, 'kwargs': {'x': 77, 'y': 99}}

    dane = {'a': 1, 'b': 2, 'x': 77, 'y': 99}
    show(**dane)
    # {'a': 1, 'b': 2, 'c': 0, 'kwargs': {'x': 77, 'y': 99}}

Passing sequence and ``dict`` as arguments
------------------------------------------
.. code-block:: python

    def show(a, b, c=0, *args, **kwargs):
        print(locals())

    show(1, 2, 3, 4, 5, 6, x=77, y=99)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}

    pozycyjne = (4, 5, 6)
    nazwane = {'x': 77, 'y': 99}
    show(1, 2, 3, *pozycyjne, **nazwane)
    # {'a': 1, 'b': 2, 'c': 3, 'args': (4, 5, 6), 'kwargs': {'x': 77, 'y': 99}}


Use cases
=========

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

Example
-------
.. code-block:: python

    mynum = 1000
    mystr = 'Hello World!'
    print "{mystr} New-style formatting is {mynum}x more fun!".format(**locals())

Print formatting in classes
---------------------------
.. code-block:: python

    class Osoba:
        first_name = 'Jan'
        last_name = 'Twardowski'

        def __str__(self):
            return '{first_name} {last_name}'.format(**self.__dict__)
            return '{first_name} {last_name}'.format(first_name='Jan', last_name='Twardowski')
            return f'{self.first_name} {self.last_name}'


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

