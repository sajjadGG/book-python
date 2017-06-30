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
    # Because of some variation for each run, it might give different results
    output = accuracy_score(y_test, predictions)
    print(output)
    # Output: 0.933333333333


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

.. figure:: img/knn-euclidean-distanse.png
    :scale: 100%
    :align: center

    Wyliczanie odległości w celu oszacowania przynależności do zbioru. Zwróć uwagę, że bez względu na ilość wymiarów wzór się niewiele różni.

Krzywe o nieliniowym przebiegu
==============================

.. figure:: img/k-nearest-neighbors.png
    :scale: 50%
    :align: center

    K najbliższych sąsiadów
