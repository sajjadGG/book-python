************************
Machine Learning Recipes
************************

Machine learning was defined in 1959 by Arthur Samuel as the "field of study that gives computers the ability to learn without being explicitly programmed." This means imbuing knowledge to machines without hard-coding it.

Ważne pytania przed przystąpieniem do tworzenia algorytmu
=========================================================

* How does this work in real world?
* How much training data do you need?
* How is the tree created?
* What makes a good feature?

Jak to wygląda w praktyce?
==========================
1. Sparametryzuj swój problem używając rozkładów statystycznych
2. Uzasadnij strukturę swojego modelu
3. Napisz swój model używając PyMC3 i dokonaj obliczeń za pomocą Inference Button
4. Zinterpretuj wynik bazując na rozkładach wynikowych
5. (opcjonalnie) z nowymi wynikami dostosuj swój model statystyczny


Słownictwo
==========

Classifier:
    Like function, takes data as imput and produces data as output.
    Zachowuje się jak funkcja, pobiera dane i przypisuje im labelki.

Features:
    Are attributes that make the labels.
    Dane do trenowania algorytmu opisujące objekt.

Labels:
    Prediction into the future

Learning Algorithm:
    Procedure that creates classifiers. Finds patterns in training data.

Preprocessing:
    Is the module used to do some cleaning/scaling of data prior to machine learning.

Cross_validation:
    Is used in the testing stages.

Supervised Learning:
    Create classifier by finding patterns in examples

Regression:
    Is a form of supervised machine learning, which is where the scientist teaches the machine by showing it features and then showing it was the correct answer is, over and over, to teach the machine. Once the machine is taught, the scientist will usually "test" the machine on some unseen data, where the scientist still knows what the correct answer is, but the machine doesn't. The machine's answers are compared to the known answers, and the machine's accuracy can be measured. If the accuracy is high enough, the scientist may consider actually employing the algorithm in the real world.



Algorytmy uczenia maszynowego
=============================

Z nadzorem
----------
* Regresja liniowa (ang. Linear Regression)
* Regresja logisyczna
* K najbliższych sąsiadów (ang. K Nearest Neighbors)
* Support Vector Machines (SVM)
* Naive Bayes
* Drzewa decyzyjne
* Sztuczne sieci neuronowe

Bez nadzoru
-----------
* Klastrowanie (ang. flat clustering, hierarchical clustering)
* Principal Component Analysis (PCA)
* Sztuczne sieci neuronowe (ang. neural networks)
* Metody doboru modelu i poprawienia jakości
* Walidacje
* Poszukiwanie parametrów
* Regularyzacja
* Ensemble

* K Nearest Neighbors


Biblioteki
==========

Machine Learning
----------------

:Scikit-learn: A set of python modules for machine learning and data mining
:TensorFlow: TensorFlow helps the tensors flow
:PyMC3: PyMC3

Data
----

:Pandas: Powerful data structures for data analysis, time series,and statistics
:NumPy: Array processing for numbers, strings, records, and objects.
:Quandl: Package for quandl API access https://www.quandl.com/topics

Math and Plots
--------------

:SciPy: Scientific Library for Python
:Matplotlib: Python plotting package

Other
-----

:Jupyter:
