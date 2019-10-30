****************
DataFrame Sample
****************

Sample ``n`` elements
---------------------
.. code-block:: python

    df.sample()
    #                     A          B          C         D
    # 1970-01-05   0.589973   0.748417  -1.680741  0.510512

.. code-block:: python

    df.sample(2)
    #                     A          B          C         D
    # 1970-01-04  -0.974425   1.327082  -0.435516  1.328745
    # 1970-01-01  0.131926  -1.825204  -1.909562   1.274718

.. code-block:: python

    df.sample(n=2, repeat=True)
    #                     A          B          C         D
    # 1970-01-05   0.589973   0.748417  -1.680741  0.510512
    # 1970-01-05   0.589973   0.748417  -1.680741  0.510512

Sample ``n`` percent of elements
--------------------------------
* 0.05 is 5%
* 1.0 is 100%

.. code-block:: python

    df.sample(frac=0.05)
    #      Sepal length  Sepal width  Petal length  Petal width     Species
    # 146           5.9          3.0           4.2          1.5  Versicolor
    # 135           4.7          3.2           1.3          0.2      Setosa
    # 15            6.6          3.0           4.4          1.4  Versicolor
    # 68            5.0          3.6           1.4          0.2      Setosa
    # 42            6.2          2.8           4.8          1.8   Virginica
    # 10            6.5          3.0           5.2          2.0   Virginica
    # 17            5.8          2.7           5.1          1.9   Virginica
    # 66            5.4          3.4           1.7          0.2      Setosa


.. code-block:: python

    df.sample(frac=0.05).reset_index(drop=True)
    #      Sepal length  Sepal width  Petal length  Petal width     Species
    # 0             5.9          3.0           4.2          1.5  Versicolor
    # 1             4.7          3.2           1.3          0.2      Setosa
    # 2             6.6          3.0           4.4          1.4  Versicolor
    # 3             5.0          3.6           1.4          0.2      Setosa
    # 4             6.2          2.8           4.8          1.8   Virginica
    # 5             6.5          3.0           5.2          2.0   Virginica
    # 6             5.8          2.7           5.1          1.9   Virginica
    # 7             5.4          3.4           1.7          0.2      Setosa


Assignments
===========
.. todo:: Create assignments
