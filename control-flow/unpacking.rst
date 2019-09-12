*******************
Unpacking sequences
*******************


Unpacking values
================
.. code-block:: python

    a, b, c = 1, 2, 3

.. code-block:: python

    a, b, c = (1, 2, 3)
    a, b, c = [1, 2, 3]
    a, b, c = {1, 2, 3}

.. note:: Note, that ``set`` is unordered collection!

.. code-block:: python

    a, b, c = 1, 2, 3

.. code-block:: python

    a, b, c = 1, 2, 3
    a, b, c = (1, 2, 3)

    (a, b, c) = (1, 2, 3)
    (a, b, c) = [1, 2, 3]

    [a, b, c] = [1, 2, 3]
    [a, b, c] = (1, 2, 3)

    {a, b, c} = {1, 2, 3}
    # SyntaxError: can't assign to literal

Too many values to unpack
-------------------------
.. code-block:: python

    a, b, c = [1, 2, 3, 4]
    # ValueError: too many values to unpack (expected 3)

Not enough values to unpack
---------------------------
.. code-block:: python

    a, b, c, d = [1, 2, 3]
    # ValueError: not enough values to unpack (expected 4, got 3)


Unpacking arbitrary number of arguments
=======================================

Unpacking values at the right side
----------------------------------
.. code-block:: python

    a, b, *c = [1, 2, 3, 4]

    a           # 1
    b           # 2
    c           # [3, 4]

Unpacking values at the left side
---------------------------------
.. code-block:: python

    *a, b, c = [1, 2, 3, 4]

    a           # [1, 2]
    b           # 3
    c           # 4

Unpacking values from both sides at once
----------------------------------------
.. code-block:: python

    a, *b, c = [1, 2, 3, 4]

    a           # 1
    b           # [2, 3]
    c           # 4

Cannot unpack from both sides at once
-------------------------------------
.. code-block:: python

    *a, b, *c = [1, 2, 3, 4]
    # SyntaxError: two starred expressions in assignment

Unpacking from variable length
------------------------------
.. code-block:: python

    a, *b, c = [1, 2]

    print(a)    # 1
    print(b)    # []
    print(c)    # 2


Naming convention
=================
.. code-block:: python

    first, *middle, last = [1, 2, 3, 4]

    first           # 1
    middle          # [2, 3]
    last            # 4

.. code-block:: python

    first, second, *others = [1, 2, 3, 4]

    first       # 1
    second      # 2
    others      # [3, 4]

.. code-block:: python

    first, second, *others = range(10)

    first       # 0
    second      # 1
    others      # [2, 3, 4, 5, 6, 7, 8, 9]

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    *measurements, species = line.split(',')

    measurements        # ['4.9', '3.1', '1.5', '0.1']
    species             # 'setosa'

.. code-block:: python

    line = 'astronauts,twardowski,watney,ivanovic'

    group_name, *members = line.split(',')

    group_name      # astronauts
    members         # ['twardowski', 'watney', 'ivanovic']

Omitting values
===============
* ``_`` is regular variable name, not a special Python syntax
* ``_`` by convention is used for data we don't want to access in future

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    *_, species = line.split(',')

    species         # setosa

.. code-block:: python

    line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'

    username, _, _, _, full_name, *_ = line.split(':')

    username        # twardowski
    full_name       # Jan Twardowski

.. code-block:: python

    line = 'twardowski:x:1001:1001:Jan Twardowski:/home/twardowski:/bin/bash'

    username, *_, home, _ = line.split(':')

    username        # twardowski
    home            # /home/twardowski


Using in a loop
===============
.. code-block:: python

    DATA = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ]

    for *measurements, species in DATA:
        print(measurements)

    # [5.8, 2.7, 5.1, 1.9]
    # [5.1, 3.5, 1.4, 0.2]
    # [5.7, 2.8, 4.1, 1.3]

.. code-block:: python

    DATA = [
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    ]

    for *_, species in DATA:
        print(species)

    # virginica
    # setosa
    # versicolor


Assignments
===========

Unpacking from sequence
-----------------------
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min
* Filename: :download:`solution/unpacking_hosts.py`

:English:
    #. Split input data (see below) by white space
    #. Separate ip address and host names
    #. Use asterisk ``*`` notation

:Polish:
    #. Podziel dane wejściowe (patrz poniżej) po białych znakach
    #. Odseparuj adres ip i nazw hostów
    #. Skorzystaj z notacji z gwiazdką ``*``

:Input:
    .. code-block:: python

        INPUT = '10.13.37.1      nasa.gov esa.int roscosmos.ru'

:Output:
    .. code-block:: python

        ip: str
        # 10.13.37.1

        hosts: list
        # ['nasa.gov', 'esa.int', 'roscosmos.ru']

Unpacking from nested sequence
------------------------------
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min
* Filename: :download:`solution/unpacking_iris.py`

:English:
    #. For input data (see below)
    #. Separate header and rekordy
    #. Use asterisk ``*`` notation

:Polish:
    #. Dla danych wejściowych (patrz poniżej)
    #. Oddziel nagłówek i rekordy
    #. Skorzystaj z konstrukcji z gwiazdką ``*``

:Input:
    .. code-block:: python

        INPUT: list = [
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

        header: tuple
        # ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')

        data: list
        # [
        #   (5.8, 2.7, 5.1, 1.9, 'virginica'),
        #   (5.1, 3.5, 1.4, 0.2, 'setosa'),
        #   (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        #   ...
        # ]
