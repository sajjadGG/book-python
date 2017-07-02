********************************
Wprowadzenie do Machine Learning
********************************

Machine learning was defined in 1959 by Arthur Samuel as the "field of study that gives computers the ability to learn without being explicitly programmed." This means imbuing knowledge to machines without hard-coding it.

Wprowadzenie
============
* Czym jest uczenie maszynowe?
* Regresja i klasyfikacja
* Miary jakości


Ważne pytania przed przystąpieniem do tworzenia algorytmu
=========================================================
* How does this work in real world?
* How much training data do you need?
* How is the tree created?
* What makes a good feature?

Jak to wygląda w praktyce?
==========================
#. Sparametryzuj swój problem używając rozkładów statystycznych
#. Uzasadnij strukturę swojego modelu
#. Napisz swój model używając PyMC3 lub SCIKit-Learn i dokonaj obliczeń
#. Zinterpretuj wynik bazując na rozkładach wynikowych
#. (opcjonalnie) z nowymi wynikami dostosuj swój model statystyczny

Co trzeba umieć aby rozpocząć?
------------------------------
* Podstawy NumPy
* Podstawy Scikit-learn
* Otwarte źródła danych
* Praca z danymi z użyciem NumPy i Scikit-learn


Algorytmy uczenia maszynowego
=============================

Supervised Learning - Z nadzorem
--------------------------------
* Drzewa decyzyjne
* K najbliższych sąsiadów (ang. K Nearest Neighbors)
* Regresja liniowa (ang. Linear Regression)
* Regresja logisyczna
* Support Vector Machines (SVM)
* Naive Bayes
* Sztuczne sieci neuronowe (ang. neural networks)

Unsupervised Learning - Bez nadzoru
-----------------------------------
* Klastrowanie (ang. flat clustering, hierarchical clustering)
* Principal Component Analysis (PCA)
* Sztuczne sieci neuronowe (ang. neural networks)

Semi-Supervised Learning
------------------------
* połączenie obu światów
* nie wszystkie dane są olabelkowane
* przyszłość machine learning
* ze względu na wolumen danych, nie wszystkie mogą mieć olabelkowane
* man (human) in the loop:

    * ekspert labelkuje część danych
    * komputer dokonuje wstępnej analizy części danych
    * przedstawia iterację człowiekowi
    * człowiek interaktywnie poprawia i określa jakość oznaczania
    * komputer dokonuje kolejnej analizy


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

Math, Plots, Graphs
-------------------

:SciPy: Scientific Library for Python
:Matplotlib: Python plotting package
:PyDotPlus: Python interface to Graphviz's Dot language
:Graphviz: Simple Python interface for Graphviz

Other
-----

:Jupyter:
