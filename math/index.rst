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
.. code-block:: python

    import math

    math.isinf(x)
    math.floor(x)
    math.ceil(x)
    math.fabs(x)

    math.log(x)
    math.log(x, base=2)
    math.sqrt()
    math.pow(x, y)
    math.exp(x)
    math.log10()

    math.sin()
    math.cos()
    math.tan()

    math.atan(x)
    math.asin(x)
    math.acos(x)

    # Return the Euclidean distance, sqrt(x*x + y*y).
    math.hypot(x, y)

    math.degrees(x)
    math.radians(x)

    math.pi
    math.e


``statistics``
==============
.. code-block:: python

    import statistics

    statistics.avg()
    statistics.mean()
    statistics.stdev()
    statistics.median()


``random``
==========
.. csv-table:: ``random``
    :header-rows: 1
    :file: data/random.csv


``collections.Counter``
=======================
.. code-block:: python

    import random

    random_numbers = [random.randint(0, 10) for a in range(0, 50)]
    counter = dict()

    for number in random_numbers:
        if number in counter:
            counter[number] += 1
        else:
            counter[number] = 1

    counter
    # [(7, 12), (4, 8), (9, 6), (1, 5), (2, 4)]

.. code-block:: python

    import random
    from collections import Counter

    random_numbers = [random.randint(0, 10) for a in range(0, 50)]
    counter = Counter(random_numbers)

    counter.most_common(5)
    # [(7, 12), (4, 8), (9, 6), (1, 5), (2, 4)]


``matplotlib``
==============
* biblioteka zewnętrzna ``pip install matplotlib``

.. note:: Moduł jest szczegółowo opisany w :ref:`Matplotlib`.

Moduł ``matplotlib`` pozwala na rysowanie wykresów i diagramów. Jest to bardzo rozbudowana biblioteka z setkami opcji konfiguracyjnych. Najczęściej używanym modułem biblioteki ``matplotlib`` jest moduł ``pyplot``, który implementuje szereg funkcji umożliwiających rysowanie wykresów 2d.

Points
------
.. figure:: img/matplotlib-01.png
    :scale: 50%
    :align: center

    Points chart

.. literalinclude:: src/matplotlib-01.py
    :language: python
    :caption: Matplotlib example

Sinusoid on grid
----------------

.. figure:: img/matplotlib-02.png
    :scale: 50%
    :align: center

    Sinusoid on grid

.. literalinclude:: src/matplotlib-02.py
    :language: python
    :caption: Matplotlib example

Multiple charts
---------------
.. figure:: img/matplotlib-03.png
    :scale: 50%
    :align: center

    Multiple charts

.. literalinclude:: src/matplotlib-03.py
    :language: python
    :caption: Matplotlib example


Assignments
===========

Euclidean distance 2D
---------------------
#. Dane są dwa punkty :math:`A` i :math:`B` o podanych koordynatach ``tuple``
#. Punkty :math:`A` i :math:`B` są dwuwymiarowe ``(x, y)``
#. Oblicz odległość między nimi
#. Wykorzystaj algorytm Euklidesa
#. Funkcja musi przechodzić ``doctest``

.. literalinclude:: src/math-euclidean-2d.py
    :language: python
    :caption: Euclidean distance 2D

:About:
    * Filename: ``math_euclidean_2d.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 15 min

.. figure:: ../machine-learning/img/k-nearest-neighbors-euclidean-distance.png
    :scale: 100%
    :align: center

    Wyliczanie odległości w celu oszacowania przynależności do zbioru. Zwróć uwagę, że bez względu na ilość wymiarów wzór się niewiele różni.

Euclidean distance multi dimensions
-----------------------------------
#. Dane są dwa punkty :math:`A` i :math:`B` o podanych koordynatach ``tuple``
#. Punkty :math:`A` i :math:`B` są na :math:`N`-wymiarowej przestrzeni ``(x, y, ...)``
#. Punkty :math:`A` i :math:`B` muszą być równo-wymiarowe
#. Funkcja musi przechodzić ``doctest``

.. literalinclude:: src/math-euclidean-ndim.py
    :language: python
    :caption: Euclidean distance N-dimension

:About:
    * Filename: ``math_euclidean_multi_dim.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 15 min

Matrix multiplication
---------------------
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

:About:
    * Filename: ``math_matrix_multiplication.py``
    * Lines of code to write: 6 lines
    * Estimated time of completion: 20 min

:Hints:
    * macierz zerowa
    * trzy pętle

Trigonometry
------------
#. Program wczytuje od użytkownika wielkość kąta w stopniach
#. Użytkownik zawsze podaje ``int`` albo ``float``
#. Wyświetl wartość funkcji trygonometrycznych (sin, cos, tg, ctg)
#. Jeżeli funkcja trygonometryczna nie istnieje dla danego kąta wypisz "For this angle function does not exist." i zakończ program

:About:
    * Filename: ``math_trigonometry.py``
    * Lines of code to write: 10 lines
    * Estimated time of completion: 10 min

Random numbers
--------------
#. Napisz program, który wyświetli 6 losowych i nie powtarzających się liczb z zakresu od 1 do 49.
#. Czym sa liczby pseudolosowe?
#. Czy da się stworzyć program czysto losowy?
#. Dlaczego?

:About:
    * Filename: ``math_random_numbers.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min

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
#. Napisz program, który obliczy pole trójkąta.
#. Użytkownik poda wysokość i długość podstawy tego trójkąta. Uwzględnij, że wysokość i długość podstawy mogą być liczbami niecałkowitymi. Wykorzystaj doctest do przetestowania funkcji.

:About:
    * Filename: ``math_triangle.py``
    * Lines of code to write: 5 lines
    * Estimated time of completion: 10 min

:The whys and wherefores:
    * Umiejętność wykorzystania gotowych funkcji w zewnętrznej bibliotece
    * Umiejętność wyszukania informacji na temat API funkcji w dokumentacji języka i jego odpowiedniej wersji
    * Stworzenie dwóch alternatywnych podejść do rozwiązania zadania
    * Porównanie czytelności obu rozwiązań

Random points
-------------
#. Wygeneruj 100 losowych punktów (rozkład gaussa o średniej 0, dowolnym odchyleniu standardowym(np. 0.2))
#. Punkty muszą być wylosowane wokół dwóch dowolnie wybranych punktów (np. A=[0, 1], B=[2, 4]).
#. Funkcja musi przechodzić ``doctest``

.. code-block:: python

    def random_point(center, std: int = 0.2):
        """
        >>> random.seed(1); random_point((0,0), std=0.2)
        (0.2576369506310926, 0.2898891217399542)

        >>> random.seed(1); random_point((0,0))
        (0.2576369506310926, 0.2898891217399542)

        >>> random.seed(1); random_point((2,5), std=10)
        (14.881847531554628, 19.494456086997708)

        >>> random.seed(1); random_point((2,5), std=(0.1, 12))
        (2.1288184753155464, 22.393347304397253)
        """
        pass


Wyrysuj te punkty na wykresie (możesz użyć funkcji ``plt.axis('equal')`` żeby osie wykresu były w tej samej skali). Punkt A i punkty wygenerowane na jego podstawie wyrysuj kolorem czerwonym (argument ``color='red'`` w funkcji ``plt.plot``), a punkt B i punkty wygenerowane na jego podstawie wyrysuj kolorem niebieskim. Możesz do tego celu napisać funkcję ``plot_point(point, color)``, która przyjmuje punkt (dwuelementowy tuple, lub listę, z czego pierwszy element to współrzędna x, a druga to y), i kolor i doda ten punkt do aktualnie aktywnego rysunku.

Korzystając z funkcji napisanej w ćwiczeniu powyżej oblicz odległość od każdego z punktów do punktów A i B oraz na podstawie tej odległości zaklasyfikuj te punkty (jeżeli punkt jest bliżej punktu A to należy do zbioru A, jeżeli jest bliżej do zbioru B to należy do zbioru B). Narysuj nowy wykres, na którym punkty ze zbioru A będą narysowane kolorem czerwonym, a punkty ze zbioru B kolorem niebieskim.

Czy dwa wykresy są takie same? Co się stanie jeżeli będziemy zwiększali odchylenie standardowe przy generacji punktów? Albo przybliżymy do siebie punkty A i B?

:About:
    * Filename: ``math_random_points.py``
    * Lines of code to write: 15 lines
    * Estimated time of completion: 20 min
