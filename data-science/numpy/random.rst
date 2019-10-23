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

    np.random.randint(5, 10)
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
    # array([ 0.40783762, 0.7550402 , 0.00919317, 0.01713451, 0.95299583])

    np.random.rand(2,3)
    # array([[ 0.50431753, 0.48272463, 0.45811345],
    #        [ 0.18209476, 0.48631022, 0.49590404]])

    np.random.rand(6).reshape((2,3))
    # array([[ 0.72915152, 0.59423848, 0.25644881],
    #        [ 0.75965311, 0.52151819, 0.60084796]])


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

Sequences
---------
* Modify a sequence in-place by shuffling its contents

.. code-block:: python

    import numpy as np

    a = list(range(10))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    np.random.shuffle(a)
    # [4, 9, 5, 0, 2, 7, 6, 8, 1, 3]

``np.array``
------------
* Multi-dimensional arrays are only shuffled along the first axis:

.. code-block:: python

    import numpy as np

    a = np.arange(9).reshape((3, 3))

    np.random.shuffle(a)
    # array([[3, 4, 5],
    #       [6, 7, 8],
    #       [0, 1, 2]])


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
