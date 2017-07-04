.. _Classifiers:

***********
Classifiers
***********

Co to jest Classifier?
======================
A mapping from unlabeled instances to (discrete) classes. Classifiers have a form (e.g., decision tree) plus an interpretation procedure (including how to handle unknowns, etc.). Some classifiers also provide probability estimates (scores), which can be thresholded to yield a discrete class decision thereby taking into account a utility function.


Schemat działania classifiera
=============================
#. Collect Training Data
#. Train Classifier
#. Make Predictions

.. figure:: img/classification-spam.png
    :scale: 75%
    :align: center

    Schemat działania classifiera. Wiadomości email przechodząc przez classifer są oznaczane jako spam, lub nie spam.


Writing Own Classifier
======================

Random Classifier
-----------------

.. code-block:: python

    import random


    class MyClassifier():
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
* Pobierz dane Pima Diabetes Dataset
* Podziel zestaw na dane testowe (25%) i dane treningowe (75%) i ustaw ``random_state=0``
* Dla danych przeprowadź analizę wykorzystując różne modele danych
* Wyświetl nazwę, dokładność oraz odchylenie standardowe modelu

.. code-block:: txt

                 RBF SVM | Accuracy: 64.24% (+/- 0.44%)
              Linear SVM | Accuracy: 76.04% (+/- 5.58%)
              Neural Net | Accuracy: 60.06% (+/- 23.16%)
           Decision Tree | Accuracy: 66.85% (+/- 4.62%)
        Gaussian Process | Accuracy: 68.58% (+/- 6.14%)
       Nearest Neighbors | Accuracy: 71.18% (+/- 7.56%)
                     QDA | Accuracy: 73.97% (+/- 8.84%)
                AdaBoost | Accuracy: 72.57% (+/- 8.32%)
             Naive Bayes | Accuracy: 73.62% (+/- 5.78%)
           Random Forest | Accuracy: 73.44% (+/- 3.69%)

:Dataset:
    https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data

:Zadanie z gwiazdką:
    * Zrównoleglij uruchamianie predykcji za pomocą modułu ``threading`` oraz architektury opartej na Workerach.

:Podpowiedź:
    .. code-block:: python

        classifiers = [
            {'name': "Nearest Neighbors", 'model': KNeighborsClassifier()},
            {'name': "Linear SVM",        'model': SVC(kernel="linear")},
            {'name': "RBF SVM",           'model': SVC(kernel="rbf")},
            {'name': "Gaussian Process",  'model': GaussianProcessClassifier()},
            {'name': "Decision Tree",     'model': DecisionTreeClassifier()},
            {'name': "Random Forest",     'model': RandomForestClassifier()},
            {'name': "Neural Net",        'model': MLPClassifier()},
            {'name': "AdaBoost",          'model': AdaBoostClassifier()},
            {'name': "Naive Bayes",       'model': GaussianNB()},
            {'name': "QDA",               'model': QuadraticDiscriminantAnalysis()},
        ]

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
