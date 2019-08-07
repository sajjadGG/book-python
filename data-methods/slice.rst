.. _Slice:

******
Slices
******


Accessing range of elements
===========================
* Slice Index must be positive or negative ``int``
* Slice has three indexes:

    - start (inclusive)
    - stop (exclusive)
    - step


Accessing slice from start
==========================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    len(text)
    # 28

    text[0:2]       # 'We'
    text[:2]        # 'We'
    text[3:9]       # 'choose'
    text[23:28]     # 'Moon!'
    text[23:27]     # 'Moon'


Accessing slice from back
=========================
* Negative index starts from the end and go right to left

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
=====================================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:100]  # 'We choose to go to the Moon!'
    text[100:]  # ''


Accessing slice from all elements
=================================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[:]               # 'We choose to go to the Moon!'


Arithmetic operations on slice indexes
======================================
.. code-block:: python

    text = 'We choose to go to the Moon!'
    first = 23
    last = 28

    text[first:last]       # 'Moon!'
    text[first:last-1]     # 'Moon'


Every ``n-th`` element
======================
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::2]             # 'W hoet ot h on'

.. code-block:: python

    DATA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    DATA[::2]
    # [
    #   [1, 2, 3],
    #   [7, 8, 9],
    # ]

Reversing
---------
.. code-block:: python

    text = 'We choose to go to the Moon!'

    text[::-1]            # '!nooM eht ot og ot esoohc eW'
    text[::-2]            # '!oMeto go soce'


Slicing data structures
=======================
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

    DATA[:3]            # ['a', 'b', 'c']
    DATA[3:]            # ['d', 'e']
    DATA[1:4]           # ['b', 'c', 'd']

.. code-block:: python

    DATA = ['a', 'b', 'c', 'd', 'e']

    DATA[::2]           # ['a', 'c', 'e']
    DATA[::-1]          # ['e', 'd', 'c', 'b', 'a']

Slice ``set``
-------------
* Slicing ``set`` is not possible

.. code-block:: python

    DATA = {'a', 'b', 'c', 'd', 'e'}

    DATA[1:2]
    # TypeError: 'set' object is not subscriptable

Slice ``dict``
--------------
.. code-block:: python

    DATA = {'a': 1, 'b': 2}

    DATA[1:2]
    # TypeError: unhashable type: 'slice'


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
* Level: Easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/slice_every_nth.py`

#. Stwórz ``a: tuple`` z cyframi 0, 1, 2, 3
#. Stwórz ``b: list`` z cyframi 2, 3, 4, 5
#. Stwórz ``c: set``, który będzie zawierał co drugie elementy z ``a`` i ``b``
#. Wyświetl ``c`` na ekranie

:The whys and wherefores:
    * Definiowanie i korzystanie z ``list``, ``tuple``, ``set``
    * Slice zbiorów danych
    * Rzutowanie i konwersja typów

Split train/test
----------------
* Level: Easy
* Lines of code to write: 6 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/slice_split_train_test.py`

.. code-block:: python
    :caption: Iris Dataset
    :name: listing-slice-iris-dataset

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (7.6, 3.0, 6.6, 2.1, 'virginica'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
        (7.1, 3.0, 5.9, 2.1, 'virginica'),
        (4.6, 3.4, 1.4, 0.3, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (5.0, 3.6, 1.4, 0.3, 'setosa'),
        (5.5, 2.3, 4.0, 1.3, 'versicolor'),
        (6.5, 3.0, 5.8, 2.2, 'virginica'),
        (6.5, 2.8, 4.6, 1.5, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (6.9, 3.1, 4.9, 1.5, 'versicolor'),
        (4.6, 3.1, 1.5, 0.2, 'setosa'),
    ]

#. Mając do dyspozycji zbiór danych Irysów z listingu :numref:`listing-slice-iris-dataset`
#. Zapisz nagłówek (pierwsza linia) do zmiennej
#. Zapisz do innej zmiennej dane bez nagłówka (``data = DATA[1:]``)
#. Wylicz punkt podziału: ilość rekordów danych bez nagłówka razy procent
#. Podziel zbiór na dwie listy w proporcji:

    - ``X_train`` - dane do uczenia - 60%
    - ``X_test`` - dane testowe - 40%

#. Z danych bez nagłówka zapisz do uczenia rekordy od początku do punktu podziału
#. Z danych bez nagłówka zapisz do testów rekordy od punktu podziału do końca

:The whys and wherefores:
    * Umiejętność przetwarzania złożonych typów danych
    * Korzystanie z przecięć danych
    * Konwersja typów
    * Magic Number

Iris dataset
------------
* Level: Medium
* Lines of code to write: 30 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/slice_iris.py`

#. Do rozwiązania zadania nie używaj pętli, generatorów, rozwinięć and instrukcji warunkowych.
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

Slicing text
------------
* Level: Easy
* Lines of code to write: 8 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/slice_text.py`

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
