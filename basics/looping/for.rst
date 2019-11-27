.. _Loop For:

************
Loop ``for``
************


Syntax
======

Generic syntax
--------------
.. highlights::
    * ``ITERABLE`` must implement ``iterator`` interface
    * More on iterators in chapter :ref:`Iterators`

.. code-block:: python
    :caption: ``for`` loop syntax

    for <VARIABLE> in <ITERABLE> :
        ...

Example
-------
.. code-block:: python
    :caption: ``for`` loop syntax: printing each number from ``list``
    :emphasize-lines: 3

    DATA = ['a', 'b', 'c']

    for letter in DATA:
        print(letter)

    # a
    # b
    # c

.. code-block:: python
    :caption: ``for`` loop syntax: data can be inline
    :emphasize-lines: 1

    for letter in ['a', 'b', 'c']:
        print(letter)

    # a
    # b
    # c


Iterating over ``str``
======================
.. highlights::
    * Iterating ``str`` will get character on each iteration

.. code-block:: python
    :caption: Iterating over ``str``

    for letter in 'setosa':
        print(letter)

    # s
    # e
    # t
    # o
    # s
    # a


Iterating simple collections
============================

Iterating over ``list``
-----------------------
.. code-block:: python
    :caption: Iterating over ``list``

    DATA = [5.1, 3.5, 1.4, 0.2, 'setosa']

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Iterating over ``tuple``
------------------------
.. code-block:: python
    :caption: Iterating over ``tuple``

    DATA = (5.1, 3.5, 1.4, 0.2, 'setosa')

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'

Iterating over ``set``
----------------------
.. code-block:: python
    :caption: Iterating over ``set``

    DATA = {5.1, 3.5, 1.4, 0.2, 'setosa'}

    for obj in DATA:
        print(obj)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'


Working with Generators and Iterators
=====================================

Loops with ``range``
--------------------
.. highlights::
    * ``range(start, stop, step)``
    * ``range(0, 3)`` will generate ``(0, 1, 2)``
    * ``start`` is inclusive, default: ``0``
    * ``stop`` is exclusive, required
    * ``step`` default: ``1``

.. code-block:: python
    :caption: Loops with ``range``

    for number in range(0, 3):
        print(number)

    # 0
    # 1
    # 2

.. code-block:: python
    :caption: Loops with ``range``

    for number in range(4, 11, 2):
        print(number)

    # 4
    # 6
    # 8
    # 10

``enumerate``
-------------
.. highlights::
    * Pythonic way
    * Preferred over ``i=0`` and ``i+=1`` for every iteration
    * ``enumerate()`` will return ``counter`` and ``value`` for every iteration

.. code-block:: python

    DATA = ['a', 'b', 'c']

    for letter in DATA:
        print(letter)

    # a
    # b
    # c

.. code-block:: python
    :caption: ``enumerate()`` will return ``counter`` and ``value`` for every iteration

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA):
        print(i, letter)

    # 0 a
    # 1 b
    # 2 c

.. code-block:: python
    :caption: ``enumerate()`` can start with custom number

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA, start=5):
        print(i, letter)

    # 5 a
    # 6 b
    # 7 c


Assignments
===========

Example
-------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/for_counter.py`

:English:
    #. Iterate over data from "Input" section and count occurrences of each number
    #. Create empty ``OUTPUT: Dict[int, int]``:

        * key - digit
        * value - number of occurrences

    #. Iterating over numbers check if number is already in ``OUTPUT``

        * If first occurrence, then add it to ``OUTPUT`` with value 1
        * If exists, then increment the value by 1

    #. Compare results with "Output" section below

:Polish:
    #. Iterując po danych wejściowych z sekcji "Input" policz wystąpienia każdej z cyfr
    #. Stwórz pusty ``OUTPUT: Dict[int, int]``:

        * klucz - cyfra
        * wartość - liczba wystąpień

    #. Iterując po cyfrach sprawdź czy cyfra znajduje się już w ``OUTPUT``

        * Jeżeli pierwsze wystąpienie, to dodaj ją do ``OUTPUT`` z wartością 1
        * Jeżeli istnieje, to zwiększ w wartość o 1

    #. Porównaj wynik z sekcją "Output" poniżej

:Input:
    .. code-block:: python

        INPUT = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0, 0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
                 2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9, 1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
                 4, 8, 1, 9, 6, 3]

:Output:
    .. code-block:: python

        from typing import Dict

        OUTPUT: Dict[int, int]
        # {1: 7, 4: 8, 6: 4, 7: 4, 5: 4, 0: 7, 9: 5, 8: 6, 2: 2, 3: 3}

:Solution:
    .. literalinclude:: solution/for_counter.py
        :language: python

:The whys and wherefores:
    * Defining ``dict`` :ref:`Mapping Dict`
    * Updating ``dict``
    * Iterating over sequences

Segmentation
------------
* Complexity level: easy
* Lines of code to write: 12 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/for_segmentation.py`

:English:
    #. For input data (see below)
    #. Count occurrences of each group
    #. Define groups:

        * ``small`` - numbers in range [0-2]
        * ``medium`` - numbers in range [3-7]
        * ``large`` - numbers in range [8-9]

    #. Print ``OUTPUT: Dict[str, int]``:

        * key - group
        * value - number of occurrences

    #. Compare results with "Output" section below

:Polish:
    #. Dla danych wejściowych (patrz sekcja input)
    #. Policz wystąpienia każdej z group
    #. Zdefiniuj grupy

        * ``small`` - liczby z przedziału [0-2]
        * ``medium`` - liczby z przedziału [3-7]
        * ``large`` - liczby z przedziału [8-9]

    #. Wypisz ``OUTPUT: Dict[str, int]``:

        * klucz - grupa
        * wartość - liczba wystąpień

    #. Porównaj wynik z sekcją "Output" poniżej

:Input:
    .. code-block:: python

        INPUT = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0, 0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
                 2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9, 1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
                 4, 8, 1, 9, 6, 3]

:Output:
    .. code-block:: python

        from typing import Dict


        OUTPUT: Dict[str, int]
        # {'small': 16, 'medium': 23, 'large': 11}

:The whys and wherefores:
    * Defining ``dict``
    * Updating ``dict``
    * Iterating over sequences

Text analysis
-------------
* Complexity level: medium or hard
* Lines of code to write: 30 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/for_text_analysis.py`

:English:
    #. Given is text of the "Moon Speech" by John F. Kennedy's (see below)
    #. Sentences are separated by period (``.``)
    #. Clean each sentence from whitespaces at the beginning and at the end
    #. Words are separated by spaces
    #. Print the total number in whole text:

        * adverbs (words ending with "ly")
        * sentences
        * words
        * letters
        * characters (including spaces inside sentences, but without periods ``.``)
        * comas (``,``)

    #. Compare results with "Output" section below

:Polish:
    #. Dany jest tekst przemówienia "Moon Speech" wygłoszonej przez John F. Kennedy'ego (patrz sekcja input)
    #. Zdania oddzielone są kropkami (``.``)
    #. Każde zdanie oczyść z białych znaków na początku i końcu
    #. Słowa oddzielone są spacjami
    #. Wypisz także ile jest łącznie w całym tekście:

        * przysłówków (słów zakończonych na "ly")
        * zdań
        * słów
        * liter
        * znaków (łącznie ze spacjami wewnątrz zdań, ale bez kropek ``.``)
        * przecinków (``,``)

    #. Porównaj wynik z sekcją "Output" poniżej

:Input:
    .. code-block:: text
        :caption: "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12 :cite:`Kennedy1962`

        We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win

:Output:
    .. code-block:: text

        Sentences: 7
        Words: 71
        Characters: 348
        Letters: 283
        Commas: 1
        Adverbs: 0

:The whys and wherefores:
    * String splitting
    * Calculating lengths
    * Iterating over string
    * Variable naming convention
    * Good variable names
