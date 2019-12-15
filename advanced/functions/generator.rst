.. _Generators:

**********
Generators
**********


.. note::
    For information about Comprehensions, please refer to :ref:`Basic Comprehensions`


Generator expressions vs. Comprehensions
========================================
.. highlights::
    * Comprehensions executes instantly
    * Generators are lazy evaluated

.. code-block:: python

    list(x for x in range(0, 5))        # [0, 1, 2, 3, 4]
    [x for x in range(0, 5)]            # [0, 1, 2, 3, 4]

.. code-block:: python

    set(x for x in range(0, 5))         # {0, 1, 2, 3, 4}
    {x for x in range(0, 5)}            # {0, 1, 2, 3, 4}

.. code-block:: python

    {x: x for x in range(0, 5)}         # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

.. code-block:: python

    tuple(x for x in range(0, 5))       # (0, 1, 2, 3, 4)
    (x for x in range(0, 5))            # <generator object <genexpr> at 0x1197032a0>

.. code-block:: python

    all(x for x in range(0, 5))         # False
    any(x for x in range(0, 5))         # True
    sum(x for x in range(0, 5))         # 10


Lazy evaluation
===============
.. highlights::
    * Code do not execute instantly
    * Sometimes code is not executed at all!

Declaring generators
--------------------
.. code-block:: python
    :caption: This will not generate any numbers!

    a = (x for x in range(0,5))
    b = (x for x in range(0,5))
    c = (x for x in range(0,5))

.. code-block:: python
    :caption: This will only create generator expression, but not evaluate it!

    a = (x for x in range(0,5))

    print(a)
    # <generator object <genexpr> at 0x11cb45950>

Evaluating generator instantly
------------------------------
.. highlights::
    * Not very efficient
    * If you need values evaluated instantly, there is no point in using generators

.. code-block:: python

    a = (x for x in range(0,5))

    list(a)
    # [0, 1, 2, 3, 4]

Evaluate generator iteratively
------------------------------
.. highlights::
    * Generator will calculate next number for every loop iteration
    * Forgets previous number
    * Doesn't know the next number

.. code-block:: python

    a = (x for x in range(0,5))

    for i in a:
        print(i)

    # 0
    # 1
    # 2
    # 3
    # 4

Halting iteration
-----------------
.. highlights::
    * Will generate only three numbers, then stop

.. code-block:: python

    a = (x for x in range(0,5))

    for i in a:
        print(i)
        if i == 2:
            break
    # 0
    # 1
    # 2

Halting and resuming iteration
------------------------------
.. highlights::
    * Will generate only three numbers, then stop
    * Forget generator

.. code-block:: python

    a = (x for x in range(0,5))

    for i in a:
        print(i)
        if i == 2:
            break
    # 0
    # 1
    # 2

    for i in a:
        print(i)
    # 3
    # 4

What is the difference?
-----------------------
* Execution and assignment

    .. code-block:: python

        a = [x for x in range(0, 5)]

        print(a)
        # [0, 1, 2, 3, 4]

        print(a)
        # [0, 1, 2, 3, 4]

* Create generator object and assign pointer (do not execute)

    .. code-block:: python

        a = (x for x in range(0, 5))

        print(a)
        # <generator object <genexpr> at 0x111e7acd0>

        print(list(a))
        # [0, 1, 2, 3, 4]

        print(list(a))
        # []

Which one is better?
--------------------
.. highlights::
    * Comprehensions - Using values more than one
    * Generators - Using values once (for example in the loop iterator)


``yield`` Operator
==================
.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
    ]

    def get_species(species):
        output = []

        for record in DATA:
            if record[4] == species:
                output.append(record)

        return output


    data = get_species('setosa')

    print(data)
    # [(5.1, 3.5, 1.4, 0.2, 'setosa'),
    #  (4.9, 3.0, 1.4, 0.2, 'setosa'),
    #  (5.4, 3.9, 1.7, 0.4, 'setosa')]

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')

.. code-block:: python

    DATA = [
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (4.9, 3.0, 1.4, 0.2, 'setosa'),
        (5.4, 3.9, 1.7, 0.4, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (5.7, 2.8, 4.5, 1.3, 'versicolor'),
        (6.3, 3.3, 6.0, 2.5, 'virginica'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (4.9, 2.5, 4.5, 1.7, 'virginica'),
    ]

    def get_species(species):
        for record in DATA:
            if record[4] == species:
                yield record

    data = get_species('setosa')

    print(data)
    # <generator object get_species at 0x11af257c8>

    for row in data:
        print(row)
    # (5.1, 3.5, 1.4, 0.2, 'setosa')
    # (4.9, 3.0, 1.4, 0.2, 'setosa')
    # (5.4, 3.9, 1.7, 0.4, 'setosa')


Built-in generators
===================
.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    output = {}

    for i, _ in enumerate(header):
        key = header[i]
        value = data[i]
        output[key] = value

    print(output)
    # {'a': 1, 'b': 2, 'c': 3}

``zip()``
---------
.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]

    zip(header, data)
    # <zip object at 0x11cf54b90>

    list(zip(header, data))
    # [('a', 1), ('b', 2), ('c', 3)]

    dict(zip(header, data))
    # {'a': 1, 'b': 2, 'c': 3}

    tuple(zip(header, data))
    # (('a', 1), ('b', 2), ('c', 3))

.. code-block:: python

    header = ['a', 'b', 'c']
    data = [1, 2, 3]
    row = [77,88,99]

    [(k,v,r) for k,v,r in zip(header, data, row)]
    # [('a', 1, 77), ('b', 2, 88), ('c', 3, 99)]

``map()``
---------
.. code-block:: python

    map(float, [1, 2, 3])
    # <map object at 0x11d15a190>

    list(map(float, [1, 2, 3]))
    # [1.0, 2.0, 3.0]

    tuple(map(float, [1, 2, 3]))
    # (1.0, 2.0, 3.0)

.. code-block:: python

    data = [1, 2, 3]

    tuple(map(float, data))
    # (1.0, 2.0, 3.0)

``filter()``
------------
.. code-block:: python

    filter(<callable>, <sequence>)

.. code-block:: python

    data = [1, 2, 3, 4, 5, 6]

    def is_even(x):
        if x % 2 == 0:
            return True
        else:
            return False

    filter(is_even, data)
    # <filter object at 0x11d182990>

    list(filter(is_even, data))
    # [2, 4, 6]

.. code-block:: python

    list(filter(lambda x: not x%2, data))
    # [2, 4, 6]

``enumerate()``
---------------
.. code-block:: python

    header = ['a', 'b', 'c']

    list(enumerate(header))
    # [(0, 'a'), (1, 'b'), (2, 'c')]

    dict(enumerate(header))
    # {0: 'a', 1: 'b', 2: 'c'}


Assignments
===========

Generators vs. Comprehensions - iris
------------------------------------
* Complexity level: medium
* Lines of code to write: 40 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/generator_iris.py`

:English:
    .. todo:: English translation

:Polish:
    #. Zapisz dane :download:`data/iris.csv` do pliku "generator_iris.csv"
    #. Zaczytaj dane pomijając nagłówek
    #. Napisz funkcję która zwraca wszystkie pomiary dla danego gatunku
    #. Gatunek będzie podawany jako ``str`` do funkcji
    #. Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję
    #. Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``
    #. Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``

:The whys and wherefores:
    * Wykorzystanie generatorów
    * Odbieranie danych z lazy evaluation
    * Porównanie wielkości struktur danych
    * Parsowanie pliku
    * Filtrowanie treści w locie

:Hint:
    .. code-block:: python

        fun = function_filter('setosa')
        gen = generator_filter('setosa')

        print('Function', sys.getsizeof(fun))
        print('Generator', sys.getsizeof(gen))

Generators vs. Comprehensions - passwd
--------------------------------------
* Complexity level: medium
* Lines of code to write: 40 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/generator_passwd.py`

:English:
    .. todo:: English translation

:Polish:
    #. Napisz program, który wczyta plik z danymi wejściowymi (patrz sekcja input)
    #. Przefiltruj linie, tak aby nie zawierały komentarzy (zaczynające się od ``#``) oraz pustych linii
    #. Przefiltruj linie, aby wyciągnąć konta systemowe - użytkowników, którzy mają UID (trzecie pole) mniejsze niż 1000
    #. Zwróć listę loginów użytkowników systemowych
    #. Zaimplementuj rozwiązanie wykorzystując zwykłą funkcję
    #. Zaimplementuj rozwiązanie wykorzystując generator i słówko kluczowe ``yield``
    #. Porównaj wyniki jednego i drugiego rozwiązania przez użycie ``sys.getsizeof()``
    #. Dlaczego różnice są tak niewielkie?
    #. Co się stanie, gdy ilość danych się zwiększy?

:The whys and wherefores:
    * Wykorzystanie generatorów
    * Odbieranie danych z lazy evaluation
    * Porównanie wielkości struktur danych
    * Parsowanie pliku
    * Filtrowanie treści w locie

:Input:
    .. code-block:: text

        ##
        # User Database
        #   - User name
        #   - Encrypted password
        #   - User ID number (UID)
        #   - User's group ID number (GID)
        #   - Full name of the user (GECOS)
        #   - User home directory
        #   - Login shell
        ##

        root:x:0:0:root:/root:/bin/bash
        bin:x:1:1:bin:/bin:/sbin/nologin
        daemon:x:2:2:daemon:/sbin:/sbin/nologin
        adm:x:3:4:adm:/var/adm:/sbin/nologin
        shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
        halt:x:7:0:halt:/sbin:/sbin/halt
        nobody:x:99:99:Nobody:/:/sbin/nologin
        sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
        peck:x:1000:1000:Max Peck:/home/peck:/bin/bash
        jimenez:x:1001:1001:José Jiménez:/home/jimenez:/bin/bash
        ivanovic:x:1002:1002:Ivan Иванович:/home/ivanovic:/bin/bash
