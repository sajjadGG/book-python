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
* Filename: ``math_trigonometry.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min

#. Program wczytuje od użytkownika wielkość kąta w stopniach
#. Użytkownik zawsze podaje ``int`` albo ``float``
#. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
#. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta podnieś stosowny wyjątek

Euclidean distance 2D
---------------------
* Filename: ``math_euclidean_2d.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 15 min
* Input data: :numref:`listing-math-euclidean-distance-2D`

#. Dane są dwa punkty :math:`A` i :math:`B` o podanych koordynatach ``tuple``
#. Punkty :math:`A` i :math:`B` są dwuwymiarowe ``(x, y)``
#. Oblicz odległość między nimi
#. Wykorzystaj algorytm Euklidesa
#. Funkcja musi przechodzić ``doctest`` :numref:`listing-math-euclidean-distance-2D`

.. code-block:: python
    :name: listing-math-euclidean-distance-2D
    :caption: Euclidean distance 2D

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

    Wyliczanie odległości w celu oszacowania przynależności do zbioru. Zwróć uwagę, że bez względu na ilość wymiarów wzór się niewiele różni.

Euclidean distance ``n`` dimensions
-----------------------------------
* Filename: ``math_euclidean_multi_dim.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 15 min
* Input data: :numref:`listing-math-euclidean-distance-n-dimensions`

#. Dane są dwa punkty :math:`A` i :math:`B` o podanych koordynatach ``tuple``
#. Punkty :math:`A` i :math:`B` są na :math:`N`-wymiarowej przestrzeni ``(x, y, ...)``
#. Punkty :math:`A` i :math:`B` muszą być równo-wymiarowe
#. Funkcja musi przechodzić ``doctest`` :numref:`listing-math-euclidean-distance-n-dimensions`

.. code-block:: python
    :name: listing-math-euclidean-distance-n-dimensions
    :caption: Euclidean distance N-dimension

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
        ValueError: Punkty muszą być w przestrzeni tylu-samo wymiarowej
        """
        x1 = ...
        y1 = ...
        x2 = ...
        y2 = ...
        return ...

Matrix multiplication
---------------------
* Filename: ``math_matrix_multiplication.py``
* Lines of code to write: 6 lines
* Estimated time of completion: 20 min

#. Napisz program mnożący macierze wykorzystując zagnieżdżone pętle ``for``

.. code-block:: python

    A = [
        [1, 0],
        [0, 1]
    ]

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
    * macierz zerowa
    * trzy pętle

Triangle
--------
* Filename: ``math_triangle.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Napisz program, który obliczy pole trójkąta.
#. Użytkownik poda wysokość i długość podstawy tego trójkąta.
#. Wysokość i długość podstawy mogą być liczbami niecałkowitymi.
#. Wykorzystaj doctest do przetestowania funkcji.

:The whys and wherefores:
    * Umiejętność wykorzystania gotowych funkcji w zewnętrznej bibliotece
    * Umiejętność wyszukania informacji na temat API funkcji w dokumentacji języka i jego odpowiedniej wersji
    * Stworzenie dwóch alternatywnych podejść do rozwiązania zadania
    * Porównanie czytelności obu rozwiązań
