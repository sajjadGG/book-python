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

    a, b, *others = [1, 2, 3, 4]

    a           # 1
    b           # 2
    others      # [3, 4]

Unpacking values at the left side
---------------------------------
.. code-block:: python

    *others, a, b = [1, 2, 3, 4]

    others      # [1, 2]
    a           # 3
    b           # 4

Unpacking values from both sides at once
----------------------------------------
.. code-block:: python

    first, *middle, last = [1, 2, 3, 4]

    first       # 1
    middle      # [2, 3]
    last        # 4

Cannot unpack from both sides at once
-------------------------------------
.. code-block:: python

    *a, b, *c = [1, 2, 3, 4]
    # SyntaxError: two starred expressions in assignment


Unpacking values from function
==============================

Recap of assignment information
-------------------------------
.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    line.split(',')
    # ['4.9', '3.1', '1.5', '0.1', 'setosa']

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    sepal_length, sepal_width, petal_length, petal_width, species = line.split(',')

    sepal_length    # '4.9'
    sepal_width     # '3.1'
    petal_length    # '1.5'
    petal_width     # '0.1'
    species         # 'setosa'

Unpacking values at the right side
----------------------------------
.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    sepal_length, sepal_width, *others = line.split(',')

    sepal_length    # '4.9'
    sepal_width     # '3.1'
    others          # ['1.5', '0.1', 'setosa']

Unpacking values at the left side
---------------------------------
.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    *features, species = line.split(',')

    features        # ['4.9', '3.1', '1.5', '0.1']
    species         # 'setosa'

Naming convention
-----------------
* if you're not using ``features`` later in your code

.. code-block:: python

    line = '4.9,3.1,1.5,0.1,setosa'

    *_, species = line.split(',')


Example
=======
.. code-block:: python
    :caption: With ``dict`` all values are namespaced

    def get_iris():
        return {'features': [4.9, 3.1, 1.5, 0.1], 'species': 'setosa'}


    data = get_iris()

    data['features']
    # [4.9, 3.1, 1.5, 0.1]

    data['species']
    # 'setosa'

.. code-block:: python
    :caption: In most cases you'll get ``tuple``, because it's a bit faster

    def get_iris():
        return 4.9, 3.1, 1.5, 0.1, 'setosa'


    *features, species = get_iris()

    features
    # 4.9, 3.1, 1.5, 0.1

    species
    # 'setosa'

More advanced topics
====================
.. note:: The topic will be continued in Intermediate and Advanced part of the book


Assignments
===========

Unpacking from sequence
-----------------------
* Filename: ``data-methods/unpacking_hosts.py``
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min

#. Dany jest ciąg znaków:

    .. code-block:: python

        '10.13.37.1      nasa.gov esa.int roscosmos.ru'

#. Podziel go po białych znakach i wydostań wartości:

    * ``ip: str``
    * ``hosts: List[str]``

#. Przy parsowaniu linii skorzystaj z konstrukcji z gwiazdką ``*``

Unpacking from nested sequence
------------------------------
* Filename: ``data-methods/unpacking_iris.py``
* Lines of code to write: 1 lines
* Estimated time of completion: 3 min

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
    * ``data: List[Tuple[float]]``

#. Przy podziale skorzystaj z konstrukcji z gwiazdką ``*``
