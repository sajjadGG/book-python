.. _Loops:

************
``for`` loop
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


Example
=======

Create ``dict`` from two sequences
----------------------------------
* Pythonic way is to use ``zip()``
* In general, don't use ``len(range(...))``, because it evaluate generator

.. code-block:: python
    :caption: Create ``dict`` from two ``list``

    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3, 4]
    output = {}

    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        output[key] = value

    print(output)
    # {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3,
    #     'd': 4,
    # }


``else``
========
* ``else`` will execute, if ``break`` was not used to exit the loop

.. code-block:: python

    DATA = """
    127.0.0.1       localhost
    127.0.0.1       astromatt
    10.13.37.1      nasa.gov esa.int roscosmos.ru
    255.255.255.255 broadcasthost
    ::1             localhost
    """
    DNS = []

    for line in DATA.splitlines():
        if not line:
            continue

        ip, *hostnames = line.split()
        # ip == '10.13.37.1'
        # hostnames == ['nasa.gov', 'esa.int', 'roscosmos.ru']

        for record in DNS:
            if record['ip'] == ip:
                record['hostnames'].update(hostnames)
                break
        else:
            DNS.append({
                'hostnames': set(hostnames),
                'ip': ip,
            })

    print(DNS)
    # [
    #   {'ip': '127.0.0.1', 'hostnames': {'astromatt', 'localhost'}},
    #   {'ip': '10.13.37.1', 'hostnames': {'roscosmos.ru', 'esa.int', 'nasa.gov'}},
    #   {'ip': '255.255.255.255', 'hostnames': {'broadcasthost'}},
    #   {'ip': '::1', 'hostnames': {'localhost'}},
    # ]


Assignments
===========

Counter
-------
* Level: Easy
* Lines of code to write: 6 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/for_counter.py`

#. Dane są liczby na listingu :numref:`listing-for-counter`

    .. code-block:: python
        :name: listing-for-counter
        :caption: Numbers for ``dict`` counter

        [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
         0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
         2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
         1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
         4, 8, 1, 9, 6, 3]

#. Policz ile jest wystąpień każdej z cyfr w tej liście
#. Zwróć ``counter: Dict[int, int]``

    - klucz - cyfra
    - wartość - ilość wystąpień

:The whys and wherefores:
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Iterowanie po liście

Segmentation
------------
* Level: Easy
* Lines of code to write: 12 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/for_segmentation.py`

#. Dane są liczby na listingu :numref:`listing-for-segmentation`

    .. code-block:: python
        :name: listing-for-segmentation
        :caption: Numbers for ``dict`` counter

        [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
         0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
         2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
         1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
         4, 8, 1, 9, 6, 3]

#. Policz ile jest wystąpień każdej z grup w tej liście

    - grupa cyfr ``małe``: cyfry z przedziału [0-2]
    - grupa cyfr ``średnie``: cyfry z przedziału [3-7]
    - grupa cyfr ``duże``: cyfry z przedziału [8-9]

#. Zwróć ``counter: Dict[str, int]``

    - klucz - grupa
    - wartość - ilość wystąpień

:The whys and wherefores:
    * Definiowanie i korzystanie z ``dict`` z wartościami
    * Iterowanie po liście

Text analysis
-------------
* Level: Easy
* Lines of code to write: 30 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/for_text_analysis.py`

#. Dany jest tekst przemówienia John F. Kennedy'ego "Moon Speech" wygłoszony na Rice Stadium :numref:`listing-for-moon-speech`
#. Zdania oddzielone są kropkami
#. Każde zdanie oczyść z białych znaków na początku i końcu
#. Słowa oddzielone są spacjami
#. Policz ile jest słów w każdym zdaniu
#. Wypisz na ekranie słownik o strukturze:

    * ``Dict[str, int]``
    * klucz: zdanie
    * wartość: ilość słów

#. Na końcu wypisz także ile jest łącznie w całym tekście:

    * przysłówków (słów zakończonych na "ly")
    * zdań
    * słów
    * liter
    * znaków (łącznie ze spacjami wewnątrz zdań, ale bez kropek)
    * przecinków

:The whys and wherefores:
    * Dzielenie stringów
    * Sprawdzanie długości ciągów znaków
    * Iterowanie po elementach listy
    * Nazywanie zmiennych

.. code-block:: text
    :name: listing-for-moon-speech
    :caption: "Moon Speech" by John F. Kennedy, Rice Stadium, Houston, TX, 1962-09-12 :cite:`Kennedy1962`

    We choose to go to the Moon. We choose to go to the Moon in this decade and do the other things. Not because they are easy, but because they are hard. Because that goal will serve to organize and measure the best of our energies and skills. Because that challenge is one that we are willing to accept. One we are unwilling to postpone. And one we intend to win
