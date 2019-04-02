.. _Slice:

*******
Slicing
*******


Accessing element with index
============================
* Index must be positive or negative ``int``
* Index must be less or equal to length of object
* Negative index starts from the end and go right to left

Accessing element from start
----------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0]         # 'W'
    text[1]         # 'e'
    text[23]        # 'M'

Accessing element from back
---------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[-1]        # '!'
    text[-5]        # 'M'

Accessing not existing element
------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[100]
    # IndexError: string index out of range


Accessing range of elements
===========================
* Slice has three indexes

    - start (inclusive)
    - stop (exclusive)
    - step

* Slice Index must be positive or negative ``int``
* Negative index starts from the end and go right to left

Accessing slice from start
--------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[0:2]       # 'We'
    text[:2]        # 'We'
    text[3:9]       # 'choose'
    text[23:28]     # 'Moon!'

Accessing slice from back
-------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[-5:]       # 'Moon!'
    text[-5:-1]     # 'Moon'
    text[:-6]       # 'We choose to go to the'

.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[4:-2]  # 'hoose to go to the Moo'
    text[-5:5]  # ''

Accessing slice not existing elements
-------------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:100]  # 'We choose to go to the Moon!'
    text[100:]  # ''

Accessing slice from all elements
---------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:]               # 'We choose to go to the Moon!'

Arithmetic operations on slice indexes
--------------------------------------
.. code-block:: python

    text = 'We choose to go to the Moon!'
    first = 23
    last = 28

    text[first:last]       # 'Moon!'
    text[first:last-1]     # 'Moon'

Every n element
---------------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::2]             # 'W hoet ot h on'

Reversing
---------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::-1]            # '!nooM eht ot og ot esoohc eW'
    text[::-2]            # '!oMeto go soce'


Slice data structures
=====================

Slicing ``str``
---------------
.. code-block:: python

    DATA = 'abcde'

    DATA[2]             # 'c'
    DATA[-1]            # 'e'

.. code-block:: python

    DATA = 'abcde'

    DATA[:3]            # 'abc'
    DATA[3:]            # 'de'
    DATA[1:4]           # 'bcd'

.. code-block:: python

    DATA = 'abcde'

    DATA[::2]           # 'ace'
    DATA[::-1]          # 'edcba'

Slicing ``tuple``
-----------------
.. code-block:: python

    DATA = ('a', 'b', 'c', 'd', 'e')

    DATA[2]             # 'c'
    DATA[-1]            # 'e'

.. code-block:: python

    DATA = ('a', 'b', 'c', 'd', 'e')

    DATA[:3]            # ('a', 'b', 'c')
    DATA[3:]            # ('d', 'e')
    DATA[1:4]           # ('b', 'c', 'd')

.. code-block:: python

    DATA = ('a', 'b', 'c', 'd', 'e')

    DATA[::2]           # ('a', 'c', 'e')
    DATA[::-1]          # ('e', 'd', 'c', 'b', 'a')

Slicing ``list``
----------------
* Slicing works the same as for ``str``

.. code-block:: python

    DATA = ['a', 'b', 'c', 'd', 'e']

    DATA[1]             # 'b'
    DATA[-2]            # 'd'

.. code-block:: python

    DATA = ['a', 'b', 'c', 'd', 'e']

    DATA[:3]            # ['a', 'b', 'c']
    DATA[3:]            # ['d', 'e']
    DATA[1:4]           # ['b', 'c', 'd']

.. code-block:: python

    DATA = ['a', 'b', 'c', 'd', 'e']

    DATA[::2]           # ['a', 'c', 'e']
    DATA[::-1]          # ['e', 'd', 'c', 'b', 'a']

Slice ``dict``
--------------
.. code-block:: python

    DATA = {'a': 1, 'b': 2}

    DATA[1:2]
    # TypeError: unhashable type: 'slice'

Slice ``set``
-------------
* Slicing ``set`` is not possible

.. code-block:: python

    DATA = {'a', 'b', 'c', 'd', 'e'}

    DATA[1]
    # TypeError: 'set' object is not subscriptable

.. code-block:: python

    DATA = {'a', 'b', 'c', 'd', 'e'}

    DATA[1:2]
    # TypeError: 'set' object is not subscriptable


Slice function
==============
* Slice object can be returned from function
* Function can, for example, calculate starting point of a sub-string

.. code-block:: python

    text = 'We choose to go to the Moon!'

    between = slice(23, 28)
    text[between]
    # 'Moon!'


Assignments
===========

Simple collections
------------------
* Filename: ``slice_every_nth.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min

#. Stwórz ``a: tuple`` z cyframi 0, 1, 2, 3
#. Stwórz ``b: list`` z cyframi 2, 3, 4, 5
#. Stwórz ``c: set``, który będzie zawierał co drugie elementy z ``a`` i ``b``
#. Wyświetl ``c`` na ekranie

:The whys and wherefores:
    * Definiowanie i korzystanie z ``list``, ``tuple``, ``set``
    * Slice zbiorów danych
    * Rzutowanie i konwersja typów

Slicing text
------------
* Filename: ``slice_text.py``
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min

#. Z podanych poniżej ciągów znaków
#. Za pomocą ``[...]`` wydobądź ``Jana III Sobieskiego``
#. Jakie parametry użyłeś dla każdej z linijek?

.. code-block:: python

    a = 'UL. Jana III Sobieskiego 1/2'
    b = 'ulica Jana III Sobieskiego 1 apt 2'
    c = 'os. Jana III Sobieskiego'
    d = 'plac Jana III Sobieskiego 1/2'
    e = 'aleja Jana III Sobieskiego'
    f = 'alei Jana III Sobieskiego 1/2'
    g = 'Jana III Sobieskiego 1 m. 2'
    h = 'os. Jana III Sobieskiego 1 apt 2'

    expected = 'Jana III Sobieskiego'
    print(f'{a == expected}\t a: "{a}"')
    print(f'{b == expected}\t b: "{b}"')
    print(f'{c == expected}\t c: "{c}"')
    print(f'{d == expected}\t d: "{d}"')
    print(f'{e == expected}\t e: "{e}"')
    print(f'{f == expected}\t f: "{f}"')
    print(f'{g == expected}\t g: "{g}"')
    print(f'{h == expected}\t h: "{h}"')

:The whys and wherefores:
    * Definiowanie zmiennych
    * Wycinanie elementów stringów
    * Indeksacja elementów

Iris dataset
------------
* Filename: ``slice_iris.py``
* Lines of code to write: 30 lines
* Estimated time of completion: 20 min

#. Mając dane z listingu poniżej

    .. code-block:: python

        DATA = (
            5.8, 2.7, 5.1, 1.9, 'virginica',
            5.1, 3.5, 1.4, 0.2, 'setosa',
            5.7, 2.8, 4.1, 1.3, 'versicolor',
            6.3, 2.9, 5.6, 1.8, 'virginica',
            6.4, 3.2, 4.5, 1.5, 'versicolor',
            4.7, 3.2, 1.3, 0.2, 'setosa',
        )

#. Za pomocą slice wyodrębnij zmienną ``features: List[Tuple[float]]`` z wynikami pomiarów

    .. code-block:: python

        features = [
            (5.8, 2.7, 5.1, 1.9),
            (5.1, 3.5, 1.4, 0.2),
            (5.7, 2.8, 4.1, 1.3),
            (6.3, 2.9, 5.6, 1.8),
            (6.4, 3.2, 4.5, 1.5),
            (4.7, 3.2, 1.3, 0.2),
        ]

#. Za pomocą slice (co piąty element) wyodrębnij zmienną ``labels: List[str]``, która będzie zawierała w kolejności wszystkie nazwy gatunków:

    .. code-block:: python

        labels = [
            'virginica',
            'setosa',
            'versicolor',
            'virginica',
            'versicolor',
            'setosa',
        ]

#. Wyodrębnij zmienną ``species: Set[str]``, która jest unikalnym zbiorem gatunków (na podstawie ``labels``)

    .. code-block:: python

        species = {
            'versicolor',
            'setosa',
            'virginica',
        }

:The whys and wherefores:
    * Definiowanie i korzystanie z ``list``, ``tuple``, ``set``
    * Slice zbiorów danych
    * Rzutowanie i konwersja typów
