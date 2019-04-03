.. _Mathematics:

***********
Mathematics
***********


Builtin
=======
* ``abs()``
* ``round()``
* ``pow()``


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

    # Return the Euclidean distance, sqrt(x*x + y*y).
    math.hypot(x, y)

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

Sum of inner elements
---------------------
* Filename: ``math_inner_sum.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Ustaw ``random.seed(0)``
#. Za pomocą biblioteki ``random`` wygeneruj ``List[List[int]]`` (cyfry z przedziału <0,9> włącznie)
#. Tablica ma mieć 16 wierszy i 16 kolumn
#. Policz sumę środkowych 4x4 elementów
#. Środkowych = centralna macierz 4x4 dokładnie w środku większej

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

Trigonometry
------------
* Filename: ``math_trigonometry.py``
* Lines of code to write: 10 lines
* Estimated time of completion: 10 min

#. Program wczytuje od użytkownika wielkość kąta w stopniach
#. Użytkownik zawsze podaje ``int`` albo ``float``
#. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
#. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta wypisz "For this angle function does not exist." i zakończ program

Random numbers
--------------
* Filename: ``math_random_numbers.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Napisz program, który wyświetli 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.
#. Czym sa liczby pseudolosowe?
#. Czy da się stworzyć program czysto losowy?
#. Dlaczego?

:Hints:
    * ``random.randrange()``
    * ``random.sample()``
    * Czytelny cod obu przykładów wraz z białymi liniami nie powinien zająć więcej niż 10 linii.

:The whys and wherefores:
    * Umiejętność wykorzystania gotowych funkcji w zewnętrznej bibliotece
    * Umiejętność wyszukania informacji na temat API funkcji w dokumentacji języka i jego odpowiedniej wersji
    * Stworzenie dwóch alternatywnych podejść do rozwiązania zadania
    * Porównanie czytelności obu rozwiązań
    * Umiejętność sprawdzania czy coś znajduje się w liście oraz ``continue``

Triangle
--------
* Filename: ``math_triangle.py``
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min

#. Napisz program, który obliczy pole trójkąta.
#. Użytkownik poda wysokość i długość podstawy tego trójkąta. Uwzględnij, że wysokość i długość podstawy mogą być liczbami niecałkowitymi. Wykorzystaj doctest do przetestowania funkcji.

:The whys and wherefores:
    * Umiejętność wykorzystania gotowych funkcji w zewnętrznej bibliotece
    * Umiejętność wyszukania informacji na temat API funkcji w dokumentacji języka i jego odpowiedniej wersji
    * Stworzenie dwóch alternatywnych podejść do rozwiązania zadania
    * Porównanie czytelności obu rozwiązań
