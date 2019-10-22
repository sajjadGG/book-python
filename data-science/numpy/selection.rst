
Array item selection and manipulation
-------------------------------------
.. code-block:: python

    a = np.array([[6, 4], [5, 9]], float)

    a >= 6
    # array([[ True, False],
    #        [False, True]], dtype=bool)

    a[a >= 6]
    # array([ 6., 9.])

.. code-block:: python

    a = np.array([[6, 4], [5, 9]], float)

    sel = (a >= 6)
    a[sel]
    # array([ 6., 9.])

    a[np.logical_and(a > 5, a < 9)]
    # array([ 6.])

.. code-block:: python

    a = np.array([2, 4, 6, 8], float)
    b = np.array([0, 0, 1, 3, 2, 1], int)

    a[b]
    # array([ 2., 2., 4., 8., 6., 4.])

.. code-block:: python

    a = np.array([2, 4, 6, 8], float)

    a[[0, 0, 1, 3, 2, 1]]
    # array([ 2., 2., 4., 8., 6., 4.])

.. code-block:: python

    a = np.array([[1, 4], [9, 16]], float)
    b = np.array([0, 0, 1, 1, 0], int)
    c = np.array([0, 1, 1, 1, 1], int)

    a[b,c]
    # array([ 1., 4., 16., 16., 4.])

.. code-block:: python

    a = np.array([2, 4, 6, 8], float)
    b = np.array([0, 0, 1, 3, 2, 1], int)

    a.take(b)
    # array([ 2., 2., 4., 8., 6., 4.])

.. code-block:: python

    a = np.array([[0, 1], [2, 3]], float)
    b = np.array([0, 0, 1], int)

    a.take(b, axis=0)
    # array([[ 0., 1.],
    #        [ 0., 1.],
    #        [ 2., 3.]])

    a.take(b, axis=1)
    # array([[ 0., 0., 1.],
    #        [ 2., 2., 3.]])

.. code-block:: python

    a = np.array([0, 1, 2, 3, 4, 5], float)
    b = np.array([9, 8, 7], float)

    a.put([0, 3], b)
    # array([ 9., 1., 2., 8., 4., 5.])

.. code-block:: python

    a = np.array([0, 1, 2, 3, 4, 5], float)

    a.put([0, 3], 5)
    # array([ 5., 1., 2., 5., 4., 5.])


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
