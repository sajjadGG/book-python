************
scikit-learn
************


Loading Sample Datasets
=======================
.. literalinclude:: src/ml-sklearn-datasets.py
    :language: python
    :caption: Loading Sample Datasets


Fit and Predict
===============
.. literalinclude:: src/ml-sklearn-fit-predict.py
    :language: python
    :caption: Fit and Predict


Classifier
==========
.. literalinclude:: src/ml-sklearn-classifier.py
    :language: python
    :caption: Classifier


Feature Selection
=================
* http://scikit-learn.org/stable/modules/feature_selection.html
* :math:`\mathrm{Var}[X] = p(1 - p)`

.. code-block:: python

    from sklearn.feature_selection import VarianceThreshold

    features = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 1]
    ]

    # Remove all features below 80% change variance in the samples
    sel = VarianceThreshold(threshold=(.8 * (1 - .8)))

    sel.fit_transform(X)
    # array([[0, 1],
    #        [1, 0],
    #        [0, 0],
    #        [1, 1],
    #        [1, 0],
    #        [1, 1]])

.. code-block:: python

    from sklearn.datasets import load_iris
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import chi2

    iris = load_iris()
    X, y = iris.data, iris.target

    X.shape
    # (150, 4)

    X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
    X_new.shape
    # (150, 2)


Evaluation
==========

Score
-----
.. literalinclude:: src/ml-sklearn-score.py
    :language: python
    :caption: Score

Cross Validation
----------------
.. literalinclude:: src/ml-sklearn-cross-validation.py
    :language: python
    :caption: Cross Validation


Label Encoder
=============
.. literalinclude:: src/ml-sklearn-label-encoder.py
    :language: python
    :caption: Label Encoder


Writing Own Classifier
======================

Random Classifier
-----------------

.. code-block:: python

    import random


    class RandomNeighborClassifer:
        def fit(self, features, labels):
            self.features_train = features
            self.labels_train = labels

        def predict(self, features_test):
            predictions = []

            for row in features_test:
                label = random.choice(self.labels_train)
                predictions.append(label)

            return predictions

Accuracy for Iris dataset: 0.346666666667

Zadania praktyczne
==================

Nearest Neighbor Classifier
---------------------------
#. Napisz klafyfikator najbliższego sąsiada
#. Podziel dane treningowe i testowe pół-na-pół
#. Dla zbioru Iris ma osiągać accuracy na poziomie powyżej 90%
#. Klasa ``NearestNeighborClassifier`` powina mieć interfejs zgodny z ``scikit-learn``:

    - ``.fit()`` - do uczenia funkcji
    - ``.predict()`` - do predykcji

#. Do porównania użyj ``accuracy = metrics.accuracy_score(labels_test, labels_predicted)``

:Podpowiedź:
    * Dla każdego feature sprawdzasz jaka jest najmniejsza odległość
    * Wybierasz najmniejszą odległość ze wszystkich
    * Do obliczania odległości skorzystaj z algorytmu Euclidesa.
    * ``scipy.spatial.distance.euclidean``

:About assignment:
    * Filename: ``ml-sklearn-classifier.py``
    * Linii kodu do napisania: około 15 linii
    * Estimated time of completion: 30 min

Porównanie classifierów
-----------------------
* Pobierz dane Brest Cancer Dataset (``datasets.load_breast_cancer()``)
* Podziel zestaw na dane testowe (15%) i dane treningowe (85%) i ustaw ``random_state=0``
* Dla danych przeprowadź analizę wykorzystując różne modele danych
* Wyświetl nazwę, dokładność oraz odchylenie standardowe modelu

.. code-block:: text

   Nearest Neighbors | Accuracy: 71.18% (+/- 3.78%)
          Linear SVM | Accuracy: 76.04% (+/- 2.79%)
             RBF SVM | Accuracy: 64.24% (+/- 0.22%)
    Gaussian Process | Accuracy: 68.58% (+/- 3.07%)
       Decision Tree | Accuracy: 68.24% (+/- 4.53%)
       Random Forest | Accuracy: 73.96% (+/- 3.28%)
          Neural Net | Accuracy: 65.28% (+/- 2.75%)
            AdaBoost | Accuracy: 72.57% (+/- 4.16%)
         Naive Bayes | Accuracy: 73.62% (+/- 2.89%)
                 QDA | Accuracy: 73.97% (+/- 4.42%)

:Podpowiedź:
    .. code-block:: python

        classifiers = [
            {'name': "Nearest Neighbors", 'model': KNeighborsClassifier()},
            {'name': "Linear SVM",        'model': SVC(kernel="linear")},
            {'name': "RBF SVM",           'model': SVC(kernel="rbf")},
            {'name': "Gaussian Process",  'model': GaussianProcessClassifier()},
            {'name': "Decision Tree",     'model': DecisionTreeClassifier()},
            {'name': "Random Forest",     'model': RandomForestClassifier()},
            {'name': "Neural Net",        'model': MLPClassifier(max_iter=1500)},
            {'name': "AdaBoost",          'model': AdaBoostClassifier()},
            {'name': "Naive Bayes",       'model': GaussianNB()},
            {'name': "QDA",               'model': QuadraticDiscriminantAnalysis()},
        ]

:Zadanie z gwiazdką:
    * Zrównoleglij uruchamianie predykcji za pomocą modułu ``threading`` oraz architektury opartej na Workerach.
    * Wyświetl posortowaną malejąco listę wg. dokładności

:About assignment:
    * Filename: ``ml-sklearn-comparision.py``
    * Linii kodu do napisania: około 15 linii
    * Estimated time of completion: 20 min
