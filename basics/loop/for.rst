.. _Loop For:

************
Loop ``for``
************


Syntax
======

Generic syntax
--------------
* ``DATA`` must implement ``iterator`` interface
* More on iterators in chapter :ref:`Iterators`

.. code-block:: python
    :caption: ``for`` loop syntax

    for <MY VARIABLE> in <DATA> :
        <CONTENT>

Example
-------
.. code-block:: python
    :caption: ``for`` loop syntax: printing each number from ``list``
    :emphasize-lines: 3

    DATA = ['a', 'b', 'c']

    for letter in DATA:
        print(letter)

    # 'a'
    # 'b'
    # 'c'

.. code-block:: python
    :caption: ``for`` loop syntax: data can be inline
    :emphasize-lines: 1

    for letter in ['a', 'b', 'c']:
        print(letter)

    # 'a'
    # 'b'
    # 'c'


Iterating over ``str``
======================
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

    for element in DATA:
        print(element)

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

    for element in DATA:
        print(element)

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

    for element in DATA:
        print(element)

    # 5.1
    # 3.5
    # 1.4
    # 0.2
    # 'setosa'


Working with Generators and Iterators
=====================================

Loops with ``range``
--------------------
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
* Pythonic way
* Preferred over ``i=0`` and ``i+=1`` for every iteration
* ``enumerate()`` will return ``counter`` and ``value`` for every iteration

.. code-block:: python
    :caption: ``enumerate()`` will return ``counter`` and ``value`` for every iteration

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA):
        print(f'{i} -> {letter}')

    # 0 -> a
    # 1 -> b
    # 2 -> c

.. code-block:: python
    :caption: ``enumerate()`` can start with custom number

    DATA = ['a', 'b', 'c']

    for i, letter in enumerate(DATA, start=5):
        print(f'{i}, {letter}')

    # 5 -> a
    # 6 -> b
    # 7 -> c


Assignments
===========

Counter
-------
* Complexity level: easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/for_counter.py`

:English:
    #. For input data (see below)
    #. Count occurrences of each number
    #. Print ``OUTPUT: Dict[int, int]``:

        * key - digit
        * value - number of occurrences

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Policz wystąpienia każdej z cyfr
    #. Wypisz ``OUTPUT: Dict[int, int]``:

        * klucz - cyfra
        * wartość - liczba wystąpień

:Input:
    .. code-block:: python

        INPUT = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
                 0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
                 2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
                 1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
                 4, 8, 1, 9, 6, 3]

:Output:
    .. code-block:: python

        OUTPUT = {
            0: 7,
            1: 7,
            2: 2,
            3: 3,
            4: 8,
            5: 4,
            6: 4,
            7: 4,
            8: 6,
            9: 5,
        }

:The whys and wherefores:
    * Defining ``dict``
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

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Policz wystąpienia każdej z group
    #. Zdefiniuj grupy

        * ``small`` - liczby z przedziału [0-2]
        * ``medium`` - liczby z przedziału [3-7]
        * ``large`` - liczby z przedziału [8-9]

    #. Wypisz ``OUTPUT: Dict[str, int]``:

        * klucz - grupa
        * wartość - liczba wystąpień

:Input:
    .. code-block:: python

        INPUT = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
                 0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
                 2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
                 1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
                 4, 8, 1, 9, 6, 3]

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
    #. Count how many words are there in every sentence
    #. Print ``Dict[str, int]``:

        * key - sentence
        * value - number of words

    #. Print the total number in whole text:

        * adverbs (words ending with "ly")
        * sentences
        * words
        * letters
        * characters (including spaces inside sentences, but without periods ``.``)
        * comas (``,``)

:Polish:
    #. Dany jest tekst przemówienia "Moon Speech" wygłoszonej przez John F. Kennedy'ego (patrz poniżej)
    #. Zdania oddzielone są kropkami (``.``)
    #. Każde zdanie oczyść z białych znaków na początku i końcu
    #. Słowa oddzielone są spacjami
    #. Policz ile jest słów w każdym zdaniu
    #. Wypisz ``Dict[str, int]``:

        * klucz - zdanie
        * wartość - liczba słów

    #. Wypisz także ile jest łącznie w całym tekście:

        * przysłówków (słów zakończonych na "ly")
        * zdań
        * słów
        * liter
        * znaków (łącznie ze spacjami wewnątrz zdań, ale bez kropek ``.``)
        * przecinków (``,``)

:The whys and wherefores:
    * String splitting
    * Calculating lengths
    * Iterating over string
    * Variable naming convention
    * Good variable names

.. code-block:: text
    :caption: "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12 :cite:`Kennedy1962`

    We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win
