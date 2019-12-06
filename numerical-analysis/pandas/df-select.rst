****************
DataFrame Select
****************


First ``n`` records
===================
.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    data = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(data, index, columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

    df.head(2)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209


Last ``n`` records
==================
.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    data = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(data, index, columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

    df.tail(3)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663


By Value
========
* ``inplace=True``

.. code-block:: python

    import numpy as np
    import pandas as pd

    np.random.seed(0)


    data = np.random.randn(6, 4)
    columns = ['Morning', 'Noon', 'Evening', 'Midnight']
    index = pd.date_range('1970-01-01', periods=6)

    df = pd.DataFrame(data, index, columns)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-01   0.486726  -0.291364  -1.105248  -0.333574
    # 1970-01-02   0.301838  -0.603001   0.069894   0.309209
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-04   0.909958  -0.986246   0.122176   1.205697
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875
    # 1970-01-06   0.047059   0.359687   0.531386  -0.587663

    df.where(df['Petal length'] > 2.0)
    #               Morning       Noon    Evening   Midnight
    # 1970-01-03  -0.424429   0.845898  -1.460294   0.109749
    # 1970-01-05  -0.172540  -0.974159  -0.848519   1.691875


Assignments
===========

Iris Clean
----------
* Complexity level: easy
* Lines of code to write: 25 lines
* Estimated time of completion: 25 min
* Filename: :download:`solution/df_select.py`

#. Pobierz zbiór danych Iris Dataset :download:`data/iris.csv`
#. Korzystając z Pandas i kodowania UTF-8 wczytaj plik
#. Przekonwertuj dane na ``pd.DataFrame``
#. Pierwsza linijka stanowi metadane (nie wyświetlaj jej)
#. Nazwy poszczególnych kolumn:

    * Sepal length
    * Sepal width
    * Petal length
    * Petal width
    * Species

#. Przefiltruj ``inplace`` kolumnę 'Petal length' i pozostaw wartości powyżej 2.0
#. Wyświetl 5 pierwszych wierszy
