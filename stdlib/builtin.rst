.. _Builtin functions:

*****************
Builtin functions
*****************


``range()``
===========
* Tworzy **iterator**, który zwraca liczby w sekwencji.

.. code-block:: python

    for liczba in range(0, 5):
        print(liczba)


    for liczba in range(0, 5, 2):
        print(liczba)

.. code-block:: python

    numbers_generator = range(0, 5)
    print(numbers_generator)
    # range(0, 5)

.. code-block:: python

    numbers_generator = range(0, 5)
    numbers = list(numbers_generator)

    print(numbers)  # [0, 1, 2, 3, 4]


Sprawdzanie typów
=================

``isinstance()``
----------------
* Sprawdza czy dany obiekt jest instancją danej klasy
* Jeżeli jest więcej niż jeden typ to musi być ``tuple`` a nie ``list`` lub ``set``

.. code-block:: python

    isinstance(10, int)           # True
    isinstance(10, float)         # False
    isinstance(10, (int, float))  # True

``issubclass()``
----------------

``type()``
----------


Działania na kolekcjach
=======================

``any()``
---------

``all()``
---------

``sum()``
---------

``len()``
---------


Konwersje typów
===============

``bin()``
---------
* Konwertuje liczbę na binarną
* Nie stosuje kodu uzupełnień do dwóch

.. code-block:: python

    0b101111    # 47

.. code-block:: python

    bin(3)      # '0b11'
    bin(-3)     # '-0b11'

``hex()``
---------
* Konwertuje liczbę na heksadecymalną
* Konwersja kolorów w HTML
* Shellcode

.. code-block:: python

    hex(99)  # '0x63'

``oct()``
---------
* Konwertuje liczbę na octalną
* Przydatne do uprawnień w systemie operacyjnym

.. code-block:: python

    oct(33261)  # '0o100755'

``ord()``
---------
Zwraca kod ASCII jednoznakowego stringa.

.. code-block:: python

    ord('a')  # 97

``chr()``
---------
Z pozycji w tablicy ASCII konwertuje kod na znak Unicode.

.. code-block:: python

    chr(97)  # 'a'

``eval()``
----------
.. code-block:: python

    eval('name="José Jiménez"; print(name)')
    # José Jiménez


Other builtin functions
=======================
.. csv-table:: Most used Built-in functions
    :header-rows: 1

    "Name", "Description"
    "``__import__``", ""
    "``abs()``", ""
    "``all()``", ""
    "``any()``", ""
    "``ascii()``", ""
    "``bin()``", ""
    "``bool()``", ""
    "``bytearray()``", ""
    "``bytes()``", ""
    "``callable()``", ""
    "``chr()``", ""
    "``classmethod()``", ""
    "``compile()``", ""
    "``complex()``", ""
    "``delattr()``", ""
    "``dict()``", ""
    "``dir()``", ""
    "``divmod()``", ""
    "``enumerate()``", ""
    "``eval()``", ""
    "``exec()``", ""
    "``filter()``", ""
    "``float()``", ""
    "``format()``", ""
    "``frozenset()``", ""
    "``getattr()``", ""
    "``globals()``", ""
    "``hasattr()``", ""
    "``hash()``", ""
    "``help()``", ""
    "``hex()``", ""
    "``id()``", ""
    "``input()``", ""
    "``int()``", ""
    "``isinstance()``", ""
    "``issubclass()``", ""
    "``iter()``", ""
    "``len()``", ""
    "``list()``", ""
    "``locals()``", ""
    "``map()``", ""
    "``max()``", ""
    "``memoryview()``", ""
    "``min()``", ""
    "``next()``", ""
    "``object()``", ""
    "``oct()``", ""
    "``open()``", ""
    "``ord()``", ""
    "``pow()``", ""
    "``print()``", ""
    "``property()``", ""
    "``range()``", ""
    "``repr()``", ""
    "``reversed()``", ""
    "``round()``", ""
    "``set()``", ""
    "``setattr()``", ""
    "``slice()``", ""
    "``sorted()``", ""
    "``staticmethod()``", ""
    "``str()``", ""
    "``sum()``", ""
    "``super()``", ""
    "``tuple()``", ""
    "``type()``", ""
    "``vars()``", ""
    "``zip()``", ""


Assignments
===========

Average
-------
* Complexity level: easy
* Lines of code to write: 12 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/builtin_average.py`

:English:
    #. For given ``INPUT`` (see below)
    #. Separate header and data
    #. Define dict ``OUTPUT``, keys are column names from header
    #. For each row in data, add values to proper lists in ``OUTPUT``
    #. Define function ``mean()``, calculating mean for arbitrary number of arguments
    #. Return ``None`` if any argument to the function is not ``float`` or ``int``
    #. To calculate mean use built-in functions
    #. Iterating over ``OUTPUT`` print column name and calculated average

:Polish:
    #. Dla danych ``INPUT`` (patrz poniżej)
    #. Odseparuj nagłówek od danych
    #. Zdefiniuj słownik ``OUTPUT: Dict[str, list]``, klucze to nazwy kolumn z nagłówka
    #. Dla każdego wiersza w danych, dodawaj wartości do odpowiednich list w ``OUTPUT``
    #. Zdefiniuj funkcję ``mean()``, liczącą średnią dla dowolnej ilości argumentów
    #. Zwróć ``None`` jeżeli którykolwiek z argumentów do funkcji nie jest ``float`` lub ``int``
    #. Do wyliczenia średniej wykorzystaj wbudowane funkcje
    #. Iterując po ``OUTPUT`` wypisz nazwę kolumny oraz wyliczoną średnią

:Input:
    .. code-block:: python

        INPUT = [
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

:Output:
    .. code-block:: python

        OUTPUT = {
            'Sepal length': [5.8, 5.1, ...],
            'Sepal width': [2.7, 3.5, ...],
            'Petal length': [5.1, 1.4, ...],
            'Petal width': [1.9, 0.2, ...],
            'Species': ['virginica', 'setosa', ...],
        }

:The whys and wherefores:
    * :ref:`Builtin functions`
    * :ref:`Iterating nested sequences`
    * :ref:`Slice`
