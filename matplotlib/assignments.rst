Assignments
===========

.. todo:: Convert assignments to literalinclude

Trigonometry
------------
* Assignment: Trigonometry
* Filename: :download:`assignments/matplotlib_trigonometry.py`
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    TODO: English Translation

Polish:
    1. Dla ``x`` z przedziału od 0.0 do 1.0 z próbkowaniem co 0.01 przedstaw przebiegi funkcji ``sin``, ``cos`` dla parametrów ``2 * np.pi * x``
    2. Stwórz dwa osobne obrazki (figure):

        a. Każdy z przebiegów na osobnym subplot
        b. Na jednym plot dwa przebiegi funkcji

    3. Wykresy (``subplot``) mają być jeden nad drugim
    4. Wykresy podpisz nazwą funkcji trygonometrycznej
    5. Tekst etykiety osi ``y`` ustaw na "Wartość funkcji"
    6. Pokoloruj nazwy tików ``x`` dla wykresu ``sin`` na czerwono
    7. Pokoloruj nazwę (label) dla ``cos`` na kolor zielony
    8. Na obu wykresach pokaż grid
    9. Narysuj drugi obrazek z nałożonymi na jeden plot wykresami obu funkcji

Hints:
    * ``np.sin()``
    * ``np.cos()``

Iris Scatter
------------
* Assignment: Iris Scatter
* Filename: :download:`assignments/matplotlib_iris.py`
* Complexity: medium
* Lines of code: 20 lines
* Time: 21 min

English:
    TODO: English Translation

Polish:
    1. Z podanego powyżej adresu URL pobierz dane
    2. Dla każdego gatunku
    3. Dane stosunku ``sepal_length`` do ``sepal_width`` zwizualizuj w formie ``scatter`` za pomocą ``matplotlib``
    4. Każdy gatunek powinien mieć inny kolor

Given:
    .. code-block:: python

        DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/_data/csv/iris.csv'

Hints:
    * ``pd.groupby()``

Random Points
-------------
* Assignment: Random Points
* Filename: :download:`assignments/matplotlib_random_points.py`
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    TODO: English Translation

Polish:
    1. Wygeneruj 100 losowych punktów:

        a. rozkład gaussa o średniej 0
        b. o odchyleniu standardowym równym 0.2

    2. Punkty muszą być wylosowane wokół dwóch wybranych punktów (``A = (0, 1)``, `B = (2, 4)``).
    3. Funkcja musi przechodzić ``doctest``

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

    4. Wyrysuj te punkty na wykresie (możesz użyć funkcji ``plt.axis('equal')`` żeby osie wykresu były w tej samej skali).
    5. Punkt A i punkty wygenerowane na jego podstawie wyrysuj kolorem czerwonym
    6. punkt B i punkty wygenerowane na jego podstawie wyrysuj kolorem niebieskim
    7. Możesz do tego celu napisać funkcję ``plot_point(point, color)``, która przyjmuje punkt (dwuelementowy tuple, lub listę, z czego pierwszy element to współrzędna x, a druga to y), i kolor i doda ten punkt do aktualnie aktywnego rysunku.
    8. Korzystając z funkcji napisanej w ćwiczeniu powyżej oblicz odległość od każdego z punktów do punktów A i B
    9. Na podstawie tej odległości zaklasyfikuj te punkty

        a. jeżeli punkt jest bliżej punktu A to należy do zbioru A
        b. jeżeli jest bliżej do zbioru B to należy do zbioru B

    10. Narysuj nowy wykres, na którym:

        a. punkty ze zbioru A będą narysowane kolorem czerwonym,
        b. punkty ze zbioru B będą narysowane kolorem niebieskim.

    11. Czy dwa wykresy są takie same?
    12. Co się stanie jeżeli będziemy zwiększali odchylenie standardowe przy generacji punktów?
    13. Albo przybliżymy do siebie punkty A i B?

Hints:
    * argument ``color='red'`` w funkcji ``plt.plot``

Color Graph
-----------
* Assignment: Color Graph
* Filename: TODO
* Complexity: medium
* Lines of code: 15 lines
* Time: 21 min

English:
    TODO: English Translation

Polish:
    1. Dokonano pomiarów z urządzeń temperatury
    2. Wygeneruj listę ``dict`` z datami z ostatniego miesiąca oraz wartością pomiarów losowo 10-15 plus szum na poziomie 0.5 stopnia celsiusza (wykorzystaj ``np.gauss()``)
    3. Mając do dyspozycji szereg czasowy, gdzie dla każdego dnia wykonano pomiar temperatury
    4. Przedstaw na wykresie dane szeregu czasowego
    5. Oś z datami przedstaw przekrzywioną o 45 stopni
    6. Na osi y przedstawiaj tylko pełne ``int``
    7. Dodaj Colorbar ze skalą temperatur zimno-ciepło
    8. Użyj kolorów niebieski (zimno), czerwony (ciepło)
    9. Wykres ma mieć grid
