***********************
K najbliższych sąsiadów
***********************

Jak działa algorytm "K najbliższych sąsiadów"
=============================================
Algorytm polega na:

#. porównaniu wartości zmiennych objaśniających dla obserwacji :math:`C` z wartościami tych zmiennych dla każdej obserwacji w zbiorze uczącym.

#. wyborze :math:`k` (ustalona z góry liczba) najbliższych do :math:`C` obserwacji ze zbioru uczącego.

#. uśrednieniu wartości zmiennej objaśnianej dla wybranych obserwacji, w wyniku czego uzyskujemy prognozę.

Przykład praktyczny
===================

Wykorzystanie ``sklearn.neighbors.KNeighborsClassifier``
--------------------------------------------------------

.. code-block:: python

    from sklearn import datasets
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier


    iris = datasets.load_iris()

    # Features
    x = iris.data

    # Labels
    y = iris.target

    # Split dataset into test and training set in half
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)

    # Create classifier
    k_neighbors = KNeighborsClassifier()

    # Train classifier using training data
    k_neighbors.fit(x_train, y_train)

    # Predict
    predictions = k_neighbors.predict(x_test)

    # How accurate was classifier on testing set
    output = accuracy_score(y_test, predictions)
    print(output)
    # Output: 0.933333333333

.. note:: Because of some variation for each run, it might give different results.

Własna implementacja
--------------------

.. code-block:: python

    from scipy.spatial import distance
    from sklearn import datasets
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split

    iris = datasets.load_iris()

    # Features
    x = iris.data

    # Labels
    y = iris.target

    # Split dataset into test and training set in half
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)


    def euclidean_distance(point_from_numeric_data, point_from_testing_data):
        return distance.euclidean(point_from_numeric_data, point_from_testing_data)


    class MyClassifier():

        def fit(self, x_train, y_train):
            # Memorize
            self.x_train = x_train
            self.y_train = y_train

        def predict(self, x_test):
            predictions = []

            for row in x_test:
                label = self.closest(row)
                predictions.append(label)

            return predictions

        def closest(self, row):
            best_dist = euclidean_distance(row, self.x_train[0])
            best_index = 0

            for i in range(0, len(self.x_train)):
                dist = euclidean_distance(row, self.x_train[i])
                if dist < best_dist:
                    best_dist = dist
                    best_index = i

            return self.y_train[best_index]


    # Create classifier
    clf = MyClassifier()

    # Train classifier using training data
    clf.fit(x_train, y_train)

    # Predict
    predictions = clf.predict(x_test)

    # How accurate was classifier on testing set
    output = accuracy_score(y_test, predictions)
    print(output)
    # Output: 0.946666666667

.. note:: Because of some variation for each run, it might give different results.


Określanie przynależności do zbioru
===================================

.. figure:: img/knn-membership.png
    :scale: 100%
    :align: center

    Przynależność do zbioru

Wyznaczanie równania prostej
============================

.. figure:: img/knn-function.png
    :scale: 100%
    :align: center

    Wyznaczanie równania prostej.

.. figure:: img/knn-parameters.png
    :scale: 100%
    :align: center

    Manipulowanie parametrami prostej (classifiera) w celu określenia funkcji.

Wyznaczanie odległości
======================

.. figure:: img/knn-euclidean-distance.png
    :scale: 100%
    :align: center

    Wyliczanie odległości w celu oszacowania przynależności do zbioru. Zwróć uwagę, że bez względu na ilość wymiarów wzór się niewiele różni.

Krzywe o nieliniowym przebiegu
==============================

.. figure:: img/k-nearest-neighbors.png
    :scale: 50%
    :align: center

    K najbliższych sąsiadów

Zalety i wady
=============

Zalety
------
* Relatywnie prosty
* Dobrze działa dla niektórych problemów

Wady
----
* Wolny i zasobożerny (musi iterować dla każdej predykcji)
* Brak możliwości ważenia features
