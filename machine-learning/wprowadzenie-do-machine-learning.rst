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

Skąd wziąć dane testowe?
========================

SCI-Kit Datasets
----------------
* http://scikit-learn.org/stable/datasets/

The ``sklearn.datasets`` package embeds some small toy datasets. To evaluate the impact of the scale of the dataset (``n_samples`` and ``n_features``) while controlling the statistical properties of the data (typically the correlation and informativeness of the features), it is also possible to generate synthetic data.

This package also features helpers to fetch larger datasets commonly used by the machine learning community to benchmark algorithm on data that comes from the 'real world'.

ML Data
-------
* http://mldata.org

`mldata.org <http://mldata.org>`_ is a public repository for machine learning data, supported by the `PASCAL network <http://www.pascal-network.org>`_.

The sklearn.datasets package is able to directly download data sets from the repository using the function ``sklearn.datasets.fetch_mldata``.

For example, to download the MNIST digit recognition database:

.. code-block:: python

    >>> from sklearn.datasets import fetch_mldata
    >>> mnist = fetch_mldata('MNIST original', data_home=custom_data_home)

PASCAL
------
* http://www.pascal-network.org

PASCAL is a Network of Excellence funded by the European Union. It has established a distributed institute that brings together researchers and students across Europe, and is now reaching out to countries all over the world.

PASCAL is developing the expertise and scientific results that will help create new technologies such as intelligent interfaces and adaptive cognitive systems. To achieve this, it supports and encourages collaboration between experts in Machine Learning, Statistics and Optimization. It also promotes the use of machine learning in many relevant application domains such as:

* Machine Vision
* Speech
* Haptics
* Brain-Computer Interface
* User-modeling for computer human interaction
* Multimodal integration
* Natural Language Processing
* Information Retrieval
* Textual Information Access

Public datasets in svmlight / libsvm format
-------------------------------------------

* http://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/

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
