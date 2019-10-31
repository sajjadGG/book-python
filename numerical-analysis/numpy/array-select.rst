************
Array Select
************


Unique
======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3, 1], [1, 4, 5, 6]])
    # array([[1, 2, 3, 1],
    #        [1, 4, 5, 6]])

    np.unique(a)
    # array([1, 2, 3, 4, 5, 6])

    np.unique(a, axis=0)
    # array([[1, 2, 3, 1],
    #        [1, 4, 5, 6]])

    np.unique(a, axis=1)
    # array([[1, 1, 2, 3],
    #        [1, 6, 4, 5]])


Diagonal
========
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2], [3, 4]])
    # array([[1, 2],
    #        [3, 4]])

    a.diagonal()
    # array([1, 4])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.diagonal()
    # array([1, 5])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])

    a.diagonal()
    # array([1, 5, 9])


Where
=====

Single argument
---------------
* ``where(boolarray)``
* indexes of elements

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])
    # array([1, 2, 3])

    np.where(a != 2)
    # (array([0, 2]),)

    np.where(a > 1)
    # (array([1, 2]),)

    np.where(a % 2 != 0)
    # (array([0, 2]),)


.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.where(a != 3)
    # (array([0, 0, 1, 1, 1]), array([0, 1, 0, 1, 2]))

    np.where(a % 2 != 0)
    # (array([0, 0, 1]), array([0, 2, 1]))

Multiple argument
-----------------
* ``where(boolarray, truearray, falsearray)``:

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.where(a % 2, 'odd', 'even')
    # array([['odd', 'even', 'odd'],
    #        ['even', 'odd', 'even']], dtype='<U4')

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.where(a > 4, 99, 77)
    # array([[77, 77, 77],
    #        [77, 99, 99]])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    np.where(a != 3, a, None)       # for element ``a != 3`` return such element, otherwise ``None``
    # array([[1, 2, None],
    #        [4, 5, 6]], dtype=object)

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    b = np.logical_and(a > 0, a % 3 == 0)
    # array([[False, False,  True],
    #        [False, False,  True]])

    a[b]
    # array([3, 6])


Nonzero
=======
.. code-block:: python

    import numpy as np


    a = np.array([[1, 0, 2], [3, 0, 4]])
    # array([[1, 0, 2],
    #        [3, 0, 4]])

    a.nonzero()
    # (array([0, 0, 1, 1]), array([0, 2, 0, 2]))


Array item selection
====================
.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a > 2
    # array([[False, False,  True],
    #        [ True,  True,  True]])

    a[a > 2]
    # array([3, 4, 5, 6])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    even = (a % 2 == 0)
    a[even]
    # array([2, 4, 6])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3], [4, 5, 6]])
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a[np.logical_and(a > 2, a <= 5)]
    # array([3, 4, 5])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    indexes = np.array([0, 1, 0])
    a[indexes]
    # array([1, 2, 1])

    indexes = np.array([0, 2])
    a[indexes]
    # array([1, 3])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    a[[0,2]]
    # array([1, 3])

.. code-block:: python

    import numpy as np


    a = np.array([[1, 4], [9, 16]], float)
    b = np.array([0, 0, 1, 1, 0], int)
    c = np.array([0, 1, 1, 1, 1], int)

    a[b,c]
    # array([ 1., 4., 16., 16., 4.])

.. code-block:: python

    import numpy as np


    a = np.array([2, 4, 6, 8], float)
    b = np.array([0, 0, 1, 3, 2, 1], int)

    a.take(b)
    # array([ 2., 2., 4., 8., 6., 4.])

.. code-block:: python

    import numpy as np


    a = np.array([[0, 1], [2, 3]], float)
    b = np.array([0, 0, 1], int)

    a.take(b, axis=0)
    # array([[ 0., 1.],
    #        [ 0., 1.],
    #        [ 2., 3.]])

    a.take(b, axis=1)
    # array([[ 0., 0., 1.],
    #        [ 2., 2., 3.]])


Assignments
===========

Array filtering
---------------
* Complexity level: easy
* Lines of code to write: 10 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/numpy_array_filtering.py`

#. Ustaw ziarno losowości na 0
#. Wygeneruj macierz (50x50) o nazwie ``A``
#. Macierz ma składać się z losowych liczb całkowitych z zakresu od 0 do 1024 włącznie.
#. Stwórz macierz ``B``, która będzie zawierała liczby z macierzy ``A`` będące potęgami dwójki.
#. Pozostaw tylko i wyłącznie unikalne wartości.
#. Uporządkuj macierz B w kolejności malejącej (od największej do najmniejszej).

:Hint:
    * ``np.random.randint()``
    * ``np.isin(a, b)``
    * ``np.flip(a)``
