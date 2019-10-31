**************
Random numbers
**************


* Mersenne Twister algorithm for pseudorandom number generation


Seed
====
* Seed the generator

.. code-block:: python

    import numpy as np


    np.random.seed(0)


Generate
========

Random ``int``
--------------
* Random integers from low (inclusive) to high (exclusive)

.. code-block:: python

    import numpy as np


    np.random.randint(0, 10)
    # 9

Random ``float``
----------------
* Random floats in the half-open interval ``[0.0, 1.0)``
* Results are from the "continuous uniform" distribution over the stated interval

.. code-block:: python

    import numpy as np


    np.random.random()
    # 0.70110427435769551

Random ``np.array``
-------------------
* Random values in a given shape
* Random samples from a uniform distribution over ``[0, 1)``

.. code-block:: python

    import numpy as np


    np.random.rand(5)
    # array([0.93123551, 0.75755626, 0.68828294, 0.5335651 , 0.98728456])

    np.random.rand(2,3)
    # array([[0.39576466, 0.39324239, 0.99116573],
    #        [0.69457363, 0.28033562, 0.43549806]])


Sample
======

Normal (Gaussian) distribution
------------------------------
* Draw random samples from a normal (Gaussian) distribution

.. code-block:: python

    import numpy as np


    np.random.normal(1.5, 4.0)  # continuous normal (Gaussian) distribution with mean micro=1.5 and standard deviation sigma=4.0
    # 0.83636555041094318

    np.random.normal()  # micro=0.0, sigma=1.0
    # 0.27548716940682932

    np.random.normal(size=5)
    # array([-1.67215088, 0.65813053, -0.70150614, 0.91452499, 0.71440557])

.. figure:: img/normal-distribution.png
    :scale: 50%
    :align: center

    Normal (Gaussian) distribution :cite:`NormalDistribution`

.. figure:: img/normal-distribution-scale.gif
    :scale: 50%
    :align: center

    Normal (Gaussian) distribution scale :cite:`NormalDistribution`

Poisson distribution
--------------------
* Draw samples from a Poisson distribution

.. code-block:: python

    import numpy as np


    np.random.poisson(6.0)  # Poisson distribution with lambda = 6.0
    # 5

.. figure:: img/poisson-distribution.png
    :scale: 50%
    :align: center

    Poisson distribution :cite:`PoissonDistribution`


Shuffle
=======
* Modify sequence in-place

1-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([3, 1, 2])

    np.random.shuffle(a)
    # array([3, 1, 2])

2-dimensional Array
-------------------
* Multi-dimensional arrays are only shuffled along the first axis

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    np.random.shuffle(a)
    # array([[7, 8, 9],
    #        [1, 2, 3],
    #        [4, 5, 6]])


Assignments
===========

Random numbers
--------------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 10 min
* Filename: :download:`solution/random_sample.py`

:English:
    #. Print 6 random integers without repetition in range from 1 to 49

:Polish:
    #. Wyświetl 6 losowych i nie powtarzających się liczb całkowitych z zakresu od 1 do 49.

:Hint:
    * ``np.append(a, ELEMENT)``
    * ``np.array.size``
    * ``NUMBER in np.array``
