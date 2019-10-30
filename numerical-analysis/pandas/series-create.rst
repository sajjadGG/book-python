*************
Series Create
*************

Values
======
.. code-block:: python

    pd.Timestamp('1961-04-12')
    pd.Categorical(["test", "train", "test", "train"])


Creating
========
* 1-dimentional data structure similar to ``ndarray``

.. code-block:: python

    values = [1, 3, 5, np.nan, 6, 8]

    pd.Series(values)
    # 0    1.0
    # 1    3.0
    # 2    5.0
    # 3    NaN
    # 4    6.0
    # 5    8.0
    # dtype: float64


Assignments
===========

Even Numbers
------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/pandas_series_even_numbers.py`

#. Stwórz ``pd.Series`` z 10 liczbami parzystymi
#. Podnieś wszystkie elementy do kwadratu
#. Dodaj 5 do każdego z elementów
