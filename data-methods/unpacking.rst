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


Naming convention
=================
* if you're not using in those values later in your code

.. code-block:: python

    first, *middle, last = [1, 2, 3, 4]

    first           # 1
    middle          # [2, 3]
    last            # 4

.. code-block:: python

    first, *middle, last = [1, 2]

    print(first)           # 1
    print(middle)          # []
    print(last)            # 2


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


Examples
========
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

.. code-block:: python

    a, b, *c = range(10)

    a       # 0
    b       # 1
    c       # [2, 3, 4, 5, 6, 7, 8, 9]

More advanced topics
====================
.. note:: The topic will be continued in Intermediate and Advanced part of the book


Assignments in Polish
=====================

Unpacking from sequence
-----------------------
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min
* Filename: :download:`solution/unpacking_hosts.py`

#. Dany jest ciąg znaków:

    .. code-block:: python

        '10.13.37.1      nasa.gov esa.int roscosmos.ru'

#. Podziel go po białych znakach i wydostań wartości:

    * ``ip: str``
    * ``hosts: List[str]``

#. Przy parsowaniu linii skorzystaj z konstrukcji z gwiazdką ``*``

Unpacking from nested sequence
------------------------------
* Complexity level: easy
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min
* Filename: :download:`solution/unpacking_iris.py`

#. Dany jest zbiór:

    .. code-block:: python

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

#. Ze zbioru oddziel nagłówek i dane:

    * ``header: Tuple[str]``
    * ``data: List[tuple]``

#. Przy podziale skorzystaj z konstrukcji z gwiazdką ``*``
