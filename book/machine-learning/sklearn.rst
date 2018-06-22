************
scikit-learn
************

Datasets
========
.. literalinclude:: src/ml-sklearn-datasets.py
    :language: python
    :caption: Classifier


Classifier
==========
.. literalinclude:: src/ml-sklearn-classifier.py
    :language: python
    :caption: Classifier


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


Nearest Neighbor Classifier
---------------------------
- Napisz klafyfikator najbliższego sąsiada osiągający dla zbioru Iris accuracy na poziomie około 0.96 dla ``test_size=0.5``.

- Klasa ``NearestNeighborClassifier`` powina mieć interfejs zgodny z ``scikit-learn``:

    - ``.fit()`` - do uczenia funkcji
    - ``.predict()`` - do predykcji

:Podpowiedź:
    * Do załadowania danych skorzystaj z ``load_iris()``
    * Do obliczania odległości skorzystaj z algorytmu Euclidesa.

    .. code-block:: python

        >>> from scipy.spatial import distance

        >>> distance.euclidean(point_from_numeric_data, point_from_testing_data)
