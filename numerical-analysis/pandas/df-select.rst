****************
DataFrame Select
****************


.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)

    df = pd.DataFrame(
        columns=['Morning', 'Noon', 'Evening', 'Midnight'],
        index=pd.date_range('1999-12-30', periods=7),
        data=np.random.randn(7, 4))

    df
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Select Records
==============

First records
-------------
.. code-block:: python

    df.head(2)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357

    df.head(n=1)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893

.. code-block:: python

    df.first('Y')
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357

    df.first('M')
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357

    df.first('D')
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893

    df.first('W')
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674

Last records
------------
.. code-block:: python

    df.tail(2)
    #              Morning      Noon   Evening  Midnight
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.tail(n=1)
    #              Morning      Noon   Evening  Midnight
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

.. code-block:: python

    df.last('Y')
    #              Morning      Noon   Evening  Midnight
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.last('M')
    #              Morning      Noon   Evening  Midnight
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.last('D')
    #              Morning      Noon   Evening  Midnight
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.last('W')
    #              Morning      Noon   Evening  Midnight
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Query Records
=============
* ``df.where()`` Works with ``inplace=True``
* Use ``df.dropna()`` to remove ``NaN``
* Use ``df.fillna()`` to substitute value for ``NaN``

Simple select
-------------
.. code-block:: python

    df[df['Morning'] > 0.0]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

.. code-block:: python

    query = df['Morning'] > 0.0

    df[query]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

.. code-block:: python

    query = df['Morning'] > 0.0

    df.where(query)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01       NaN       NaN       NaN       NaN
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04       NaN       NaN       NaN       NaN
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

Logical NOT
-----------
.. code-block:: python

    query = df['Midnight'] < 0.0

    df[~query]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674

    df.where(~query)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31       NaN       NaN       NaN       NaN
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03       NaN       NaN       NaN       NaN
    # 2000-01-04       NaN       NaN       NaN       NaN
    # 2000-01-05       NaN       NaN       NaN       NaN

Logical AND
-----------
* In first and in second query

.. code-block:: python

    df[ (df['Morning']<0.0) & (df['Midnight']<0.0) ]
    #             Morning      Noon   Evening  Midnight
    # 2000-01-04 -2.55299  0.653619  0.864436 -0.742165

.. code-block:: python

    query = (df['Morning'] < 0.0) & (df['Midnight'] < 0.0)

    df[query]
    #             Morning      Noon   Evening  Midnight
    # 2000-01-04 -2.55299  0.653619  0.864436 -0.742165

.. code-block:: python

    query1 = df['Morning'] < 0.0
    query2 = df['Midnight'] < 0.0

    df[query1 & query2]
    #             Morning      Noon   Evening  Midnight
    # 2000-01-04 -2.55299  0.653619  0.864436 -0.742165

    df.where(query1 & query2)
    #             Morning      Noon   Evening  Midnight
    # 1999-12-30      NaN       NaN       NaN       NaN
    # 1999-12-31      NaN       NaN       NaN       NaN
    # 2000-01-01      NaN       NaN       NaN       NaN
    # 2000-01-02      NaN       NaN       NaN       NaN
    # 2000-01-03      NaN       NaN       NaN       NaN
    # 2000-01-04 -2.55299  0.653619  0.864436 -0.742165
    # 2000-01-05      NaN       NaN       NaN       NaN

Logical OR
----------
* In first or in second query

.. code-block:: python

    query1 = df['Morning'] < 0.0
    query2 = df['Midnight'] < 0.0

    df[query1 | query2]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.where(query1 | query2)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30       NaN       NaN       NaN       NaN
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02       NaN       NaN       NaN       NaN
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

Logical XOR
-----------
* In first or in second, but not in both queries

.. code-block:: python

    query1 = df['Morning'] < 0.0
    query2 = df['Midnight'] < 0.0

    df[query1 ^ query2]
    #              Morning      Noon   Evening  Midnight
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.where(query1 ^ query2)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30       NaN       NaN       NaN       NaN
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02       NaN       NaN       NaN       NaN
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04       NaN       NaN       NaN       NaN
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Assignments
===========

Iris Clean
----------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/df_select.py`

:Polish:
    #. Pobierz zbiór danych Iris Dataset :download:`data/iris.csv`
    #. Korzystając z Pandas i kodowania UTF-8 wczytaj plik
    #. Przekonwertuj dane na ``pd.DataFrame``
    #. Zmień nazwy kolejnych kolumn na:

        * Sepal length
        * Sepal width
        * Petal length
        * Petal width
        * Species

    #. Przefiltruj ``inplace`` kolumnę 'Petal length' i pozostaw wartości powyżej 2.0
    #. Wyświetl 5 pierwszych wierszy
