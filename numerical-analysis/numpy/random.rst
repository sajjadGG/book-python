**************
Random numbers
**************


* Since ``numpy v1.17``: BitGenerator for the PCG-64 (Parallel Congruent Generator 64 bit) pseudo-random number generator
* Before``numpy v1.17``: Mersenne Twister algorithm for pseudorandom number generation


Seed
====
* Seed the generator

.. code-block:: python

    import numpy as np


    np.random.seed(0)


Generate pseudorandom numbers
=============================

Generate pseudorandom ``int``
-----------------------------
* Random integers from low (inclusive) to high (exclusive)

.. code-block:: python

    import numpy as np


    np.random.randint(0, 10)
    # 5

.. code-block:: python

    import numpy as np


    np.random.randint(0, 10, size=5)
    # array([4, 3, 0, 4, 3])

    np.random.randint(0, 10, size=(2,3))
    # array([[8, 8, 3],
    #        [8, 2, 8]])

Generate pseudorandom ``float``
-------------------------------
* Random floats in the half-open interval ``[0.0, 1.0)``
* Results are from the "continuous uniform" distribution over the stated interval

.. code-block:: python

    import numpy as np


    np.random.random()
    # 0.8472517387841254

.. code-block:: python

    import numpy as np


    np.random.random(size=5)
    # array([0.88173536, 0.69253159, 0.72525428, 0.50132438, 0.95608363])

    np.random.random(size=(2,3))
    # array([[0.69947928, 0.29743695, 0.81379782],
    #        [0.39650574, 0.8811032 , 0.58127287]])

Generate pseudorandom ``ndarray``
---------------------------------
* Random values in a given shape
* Random samples from a uniform distribution over ``[0, 1)``

.. code-block:: python

    import numpy as np


    np.random.rand(5)
    # array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ])

.. code-block:: python

    import numpy as np


    np.random.rand(2,3)
    # array([[0.5488135 , 0.71518937, 0.60276338],
    #        [0.54488318, 0.4236548 , 0.64589411]])

    np.random.rand(3,2)
    # array([[0.5488135 , 0.71518937],
    #        [0.60276338, 0.54488318],
    #        [0.4236548 , 0.64589411]])


Drawing pseudorandom sample
===========================

Choice
------
.. code-block:: python

    import numpy as np


    np.random.choice([1, 2, 3])
    # 2

.. code-block:: python

    import numpy as np


    np.random.choice([1, 2, 3], size=2)
    # array([3, 1])

    np.random.choice([1, 2, 3], size=2)
    # array([3, 3])

.. code-block:: python

    import numpy as np


    np.random.choice([1, 2, 3], 2, replace=False)
    # array([1, 3])

Sample
------
* alias of ``np.random.random_sample``

.. code-block:: python

    import numpy as np


    np.random.sample(size=5)
    # array([0.44792617, 0.09956909, 0.35231166, 0.46924917, 0.84114013])

    np.random.sample(size=(2,3))
    # array([[0.90464774, 0.03755938, 0.50831545],
    #        [0.16684751, 0.77905102, 0.8649333 ]])

    np.random.sample(size=(3,2))
    # array([[0.41139672, 0.13997259],
    #        [0.03322239, 0.98257496],
    #        [0.37329075, 0.42007537]])

Normal (Gaussian) distribution
------------------------------
* Draw pseudorandom samples from a normal (Gaussian) distribution
* Default:

    * μ - ``loc=0.0``
    * σ - ``scale=1.0``

.. code-block:: python

    import numpy as np


    np.random.normal()
    # 0.9500884175255894

    np.random.normal(0.0, 1.0)
    # 0.4001572083672233

    np.random.normal(loc=0.0, scale=1.0)
    # -0.977277879876411

.. code-block:: python

    import numpy as np


    np.random.normal(size=5)
    # array([-1.67215088, 0.65813053, -0.70150614, 0.91452499, 0.71440557])

    np.random.normal(loc=0.0, scale=1.0, size=(2,3))
    # array([[-0.99090328,  1.01788005,  0.3415874 ],
    #        [-1.25088622,  0.92525075, -0.90478616]])

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


    np.random.poisson(6.0)
    # 5

    np.random.poisson(lam=6.0)
    # 5

.. code-block:: python

    import numpy as np


    np.random.poisson(lam=6.0, size=5)
    # array([5, 7, 3, 5, 6])

    np.random.poisson(lam=6.0, size=(2,3))
    # array([[4, 9, 7],
    #        [8, 5, 5]])

.. figure:: img/poisson-distribution.png
    :scale: 50%
    :align: center

    Poisson distribution :cite:`PoissonDistribution`


Shuffle
=======
* Modify sequence in-place (!!)

1-dimensional Array
-------------------
.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    np.random.shuffle(a)
    # array([3, 1, 2])

2-dimensional Array
-------------------
* Multi-dimensional arrays are only shuffled along the first axis

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

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
