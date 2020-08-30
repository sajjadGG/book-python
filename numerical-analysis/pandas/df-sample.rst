****************
DataFrame Sample
****************

.. code-block:: python

    import pandas as pd
    import numpy as np
    np.random.seed(0)

    df = pd.DataFrame(
        columns = ['Morning', 'Noon', 'Evening', 'Midnight'],
        index = pd.date_range('1999-12-30', periods=7),
        data = np.random.randn(7, 4))

    df
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


Head
====
.. code-block:: python

    df.head(2)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357

    df.head(n=1)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893


Tail
=====
.. code-block:: python

    df.tail(2)
    #              Morning      Noon   Evening  Midnight
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184

    df.tail(n=1)
    #              Morning      Noon   Evening  Midnight
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184


First
=====
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


Last
====
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


Sample
======
* 1/4 is 25%
* .05 is 5%
* 0.5 is 50%
* 1.0 is 100%

.. code-block:: python
    :caption: `n` number or fraction random rows with and without repetition

    df.sample()
    #                  Morning      Noon   Evening  Midnight
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274

    df.sample(2)
    #              Morning      Noon   Evening  Midnight
    # 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2000-01-04 -2.552990  0.653619  0.864436 -0.742165

    df.sample(n=2, replace=True)
    #              Morning      Noon   Evening  Midnight
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357

    df.sample(frac=1/4)
    #              Morning      Noon   Evening  Midnight
    # 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357

    df.sample(frac=0.5)
    #              Morning      Noon   Evening  Midnight
    # 2000-01-05  2.269755 -1.454366  0.045759 -0.187184
    # 1999-12-30  1.764052  0.400157  0.978738  2.240893
    # 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 1999-12-31  1.867558 -0.977278  0.950088 -0.151357


Reset Index
===========
.. code-block:: python

    df.sample(frac=1.0).reset_index()
    #        index   Morning      Noon   Evening  Midnight
    # 0 2000-01-02  0.761038  0.121675  0.443863  0.333674
    # 1 2000-01-03  1.494079 -0.205158  0.313068 -0.854096
    # 2 2000-01-01 -0.103219  0.410599  0.144044  1.454274
    # 3 1999-12-31  1.867558 -0.977278  0.950088 -0.151357
    # 4 2000-01-05  2.269755 -1.454366  0.045759 -0.187184
    # 5 2000-01-04 -2.552990  0.653619  0.864436 -0.742165
    # 6 1999-12-30  1.764052  0.400157  0.978738  2.240893

.. code-block:: python

    import pandas as pd

    DATA = 'https://raw.githubusercontent.com/AstroMatt/book-python/master/numerical-analysis/pandas/data/iris.csv'

    df = pd.read_csv(DATA)

    selected = df.sample(frac=0.02)
    #      sepal_length  sepal_width  petal_length  petal_width     species
    # 98            5.0          3.0           1.6          0.2      setosa
    # 64            5.0          3.5           1.6          0.6      setosa
    # 105           6.1          2.8           4.0          1.3  versicolor

    selected.reset_index()
    #    index  sepal_length  sepal_width  petal_length  petal_width     species
    # 0     98           5.0          3.0           1.6          0.2      setosa
    # 1     64           5.0          3.5           1.6          0.6      setosa
    # 2    105           6.1          2.8           4.0          1.3  versicolor

    selected.reset_index(drop=True)
    #    sepal_length  sepal_width  petal_length  petal_width     species
    # 0           5.0          3.0           1.6          0.2      setosa
    # 1           5.0          3.5           1.6          0.6      setosa
    # 2           6.1          2.8           4.0          1.3  versicolor



Assignments
===========

DataFrame Sample
----------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 8 min
* Solution: :download:`solution/df_sample.py`

:English:
    .. todo:: English translation

:Polish:
    #. Pobierz zbiór danych Iris Dataset :download:`data/astronauts.csv`
    #. Korzystając z Pandas wczytaj go do ``pd.DataFrame``
    #. W danych kolumna "Order" kolejność astronauty/kosmonauty w kosmosie (czasami kilka osób leciało tym samym statkiem i ich numery powinny być takie same, a w danych jest ``pd.Na``).
    #. Wypełnij brakujące indeksy (kolumna "Order") stosując ``ffill``
    #. Ustaw wszystkie wiersze w losowej kolejności
    #. Zresetuj index nie pozostawiając kopii zapasowej starego
