.. _Mathematics:

***********
Mathematics
***********


Builtin
=======

Constans
--------
* ``inf`` or ``Infinity``
* ``-inf`` or ``-Infinity``
* ``1E10`` or ``1E-5``

Functions
---------
* ``abs()``
* ``round()``
* ``pow()``
* ``sum()``
* ``min()``
* ``max()``
* ``divmod()``
* ``complex()``

``math``
========

Constants
---------
.. code-block:: python

    import math


    math.pi
    math.e

Degree/Radians Conversion
-------------------------
.. code-block:: python

    import math


    math.degrees(x)
    math.radians(x)

Rounding to lower
-----------------
.. code-block:: python

    import math


    math.floor(3.14)                # 3
    math.floor(3.00000000000000)    # 3
    math.floor(3.00000000000001)    # 3
    math.floor(3.99999999999999)    # 3

Rounding to higher
------------------
.. code-block:: python

    import math


    math.ceil(3.14)                 # 4
    math.ceil(3.00000000000000)     # 3
    math.ceil(3.00000000000001)     # 4
    math.ceil(3.99999999999999)     # 4

Logarithms
----------
.. code-block:: python

    import math


    math.log(x)     # if base is not set, then ``e``
    math.log(x, base=2)
    math.log10()

    math.exp(x)

Linear Algebra
--------------
.. code-block:: python

    import math


    math.sqrt()
    math.pow(x, y)

    math.hypot()    # 2D, since Python 3.8 also multiple dimensions
    math.dist()     # Euclidean distance, Since Python 3.8

Trigonometry
------------
.. code-block:: python

    import math


    math.sin()
    math.cos()
    math.tan()

    math.sinh()
    math.cosh()
    math.tanh()

    math.asin(x)
    math.acos(x)
    math.atan(x)
    math.atan2(x)

    math.asinh(x)
    math.acosh(x)

Other functions
---------------
.. code-block:: python

    import math


    math.isinf(x)
    math.fabs(x)



Assignments
===========

Trigonometry
------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/math_trigonometry.py`

:English:
    #. Read input (angle in degrees) from user
    #. User will type ``int`` or ``float``
    #. Print all trigonometric functions (sin, cos, tg, ctg)
    #. If there is no value for this angle, raise an exception

:Polish:
    #. Program wczytuje od użytkownika wielkość kąta w stopniach
    #. Użytkownik zawsze podaje ``int`` albo ``float``
    #. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
    #. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta podnieś stosowny wyjątek

:Hint:
    * ``input('Type angle [deg]: ')``

Euclidean distance 2D
---------------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/math_euclidean_2d.py`

:English:
    #. Given are two points ``A: Tuple[int, int]`` and ``B: Tuple[int, int]``
    #. Coordinates are in cartesian system
    #. Points :math:`A` and :math:`B` are in two dimensional space
    #. Calculate distance between points using Euclidean algorithm
    #. Function must pass ``doctest``

:Polish:
    #. Dane są dwa punkty ``A: Tuple[int, int]`` i ``B: Tuple[int, int]``
    #. Koordynaty są w systemie kartezjańskim
    #. Punkty :math:`A` i :math:`B` są w dwuwymiarowej przestrzeni
    #. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    #. Funkcja musi przechodzić ``doctest``

:Input:
    .. code-block:: python

        def euclidean_distance(A, B):
            """
            >>> A = (1, 0)
            >>> B = (0, 1)
            >>> euclidean_distance(A, B)
            1.4142135623730951

            >>> euclidean_distance((0,0), (1,0))
            1.0

            >>> euclidean_distance((0,0), (1,1))
            1.4142135623730951

            >>> euclidean_distance((0,1), (1,1))
            1.0

            >>> euclidean_distance((0,10), (1,1))
            9.055385138137417
            """
            x1 = ...
            y1 = ...
            x2 = ...
            y2 = ...
            return ...

.. figure:: ../machine-learning/img/k-nearest-neighbors-euclidean-distance.png
    :scale: 100%
    :align: center

    Calculate Euclidean distance in Cartesian coordinate system

Euclidean distance ``n`` dimensions
-----------------------------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/math_euclidean_multi_dim.py`

:English:
    #. Given are two points ``A: Tuple[int, int]`` and ``B: Tuple[int, int]``
    #. Coordinates are in cartesian system
    #. Points :math:`A` and :math:`B` are in :math:`N`-dimensional space
    #. Points :math:`A` and :math:`B` must be in the same space
    #. Calculate distance between points using Euclidean algorithm
    #. Function must pass ``doctest``

:Polish:
    #. Dane są dwa punkty ``A: Tuple[Sequence[int]]`` i ``B: Tuple[Sequence[int]]``
    #. Koordynaty są w systemie kartezjańskim
    #. Punkty :math:`A` i :math:`B` są w :math:`N`-wymiarowej przestrzeni
    #. Punkty :math:`A` i :math:`B` muszą być w tej samej przestrzeni
    #. Oblicz odległość między nimi wykorzystując algorytm Euklidesa
    #. Funkcja musi przechodzić ``doctest``

:Input:
    .. code-block:: python

        def euclidean_distance(A, B):
            """
            >>> A = (0,1,0,1)
            >>> B = (1,1,0,0)
            >>> euclidean_distance(A, B)
            1.4142135623730951

            >>> euclidean_distance((0,0,0), (0,0,0))
            0.0

            >>> euclidean_distance((0,0,0), (1,1,1))
            1.7320508075688772

            >>> euclidean_distance((0,1,0,1), (1,1,0,0))
            1.4142135623730951

            >>> euclidean_distance((0,0,1,0,1), (1,1,0,0,1))
            1.7320508075688772

            >>> euclidean_distance((0,0,1,0,1), (1,1))
            Traceback (most recent call last):
                ...
            ValueError: Points must be in the same dimensions
            """
            return ...

:Hint:
    * ``zip(A, B)``

Matrix multiplication
---------------------
* Complexity level: hard
* Lines of code to write: 6 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/math_matmul.py`

:English:
    #. Multiply matrices using nested ``for`` loops
    #. Function must pass ``doctest``

:Polish:
    #. Pomnóż macierze wykorzystując zagnieżdżone pętle ``for``
    #. Funkcja musi przechodzić ``doctest``

:Input:
    .. code-block:: python

        def matrix_multiplication(A, B):
            """
            >>> A = [[1, 0], [0, 1]]
            >>> B = [[4, 1], [2, 2]]
            >>> matrix_multiplication(A, B)
            [[4, 1], [2, 2]]

            >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
            >>> B = [[4,1], [2,2], [5,1], [2,3]]
            >>> matrix_multiplication(A, B)
            [[9, 2], [7, 3], [21, 8], [28, 8]]
            """
            return

:Hints:
    * Zero matrix
    * Three nested ``for`` loops

Triangle
--------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/math_triangle.py`

:English:
    #. Calculate triangle area
    #. User will input base and height
    #. Input numbers will be only ``int`` and ``float``
    #. Function must pass ``doctest``

:Polish:
    #. Obliczy pole trójkąta
    #. Użytkownik poda wysokość i długość podstawy
    #. Wprowadzone dane będą tylko ``int`` lub ``float``
    #. Funkcja musi przechodzić ``doctest``
