****************
Array Data Types
****************


* Array can have only one data type (``dtype``)
* Type can be "non-primitive" - any class


Signed int
==========
* Signed (positive and negative)
* ``np.int`` alias for ``np.int64``
* ``np.int0`` alias for ``np.int64`` - Integer used for indexing
* ``np.int8`` (max: 127)
* ``np.int16`` (max: 32,767)
* ``np.int32`` (max: 2,147,483,647)
* ``np.int64`` (max: 184,46,744,073,709,551,615)

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, 3])

    type(a)
    # <class 'numpy.ndarray'>

    a.dtype
    # dtype('int64')

.. code-block:: python

    import numpy as np


    a = np.array([[1., 2., 3.],
                  [4., 5., 6.]])

    a.astype(int)
    # array([[1, 2, 3],
    #        [4, 5, 6]])

    a.astype(np.int8)
    # array([[1, 2, 3],
    #        [4, 5, 6]], dtype=int8)

    a.astype(np.int64)
    # array([[1, 2, 3],
    #        [4, 5, 6]])


Unsigned int
============
* Unsigned (non-negative only)
* ``np.uint0``
* ``np.uint8``
* ``np.uint16``
* ``np.uint32``
* ``np.uint64``

.. code-block:: python

    import numpy as np


    a = np.array([-1, 0, 1])

    type(a)
    # <class 'numpy.ndarray'>

    a.dtype
    # dtype('int64')

.. code-block:: python

    import numpy as np


    a = np.array([-1, 0, 1])

    a.astype(int)
    # array([-1, 0, 1])

    a.astype(np.uint8)
    # array([255, 0, 1], dtype=uint8)

    a.astype(np.uint64)
    # array([18446744073709551615, 0, 1], dtype=uint64)


float
=====
* ``np.float``
* ``np.float16``
* ``np.float32``
* ``np.float64``
* ``np.float128``

.. code-block:: python

    import numpy as np


    a = np.array([1., 2., 3.])

    type(a)
    # <class 'numpy.ndarray'>

    a.dtype
    # dtype('float64')

.. code-block:: python

    import numpy as np


    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    a.astype(float)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

    a.astype(np.float16)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]], dtype=float16)

    a.astype(np.float32)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]], dtype=float32)

    a.astype(np.float64)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]])

    a.astype(np.float128)
    # array([[1., 2., 3.],
    #        [4., 5., 6.]], dtype=float128)


complex
=======
* ``np.complex``
* ``np.complex64``
* ``np.complex128``
* ``np.complex256``

.. code-block:: python

    import numpy as np


    a = np.array([1+2j])

    a.dtype
    # dtype('complex128')

.. code-block:: python

    import numpy as np


    a = np.array([1.1+2.2j])
    # array([1.1+2.2j])

    a.dtype
    # dtype('complex128')


bool
====
.. code-block:: python

    import numpy as np


    a = np.array([True, False, True])

    a.dtype
    # dtype('bool')

.. code-block:: python

    import numpy as np


    a = np.array([1, 0, 1], bool)

    a.dtype
    # dtype('bool')

    repr(a)
    # array([ True, False,  True])


str
===
.. code-block:: python

    import numpy as np


    np.array(['a', 'b', 'c'])
    # array(['a', 'b', 'c'], dtype='<U1')

    np.array(['one', 'two', 'three'])
    # array(['one', 'two', 'three'], dtype='<U5')


Assignments
===========

As Type
-------
* Complexity level: easy
* Lines of code to write: 4 lines
* Estimated time of completion: 5 min
* Filename: :download:`solution/numpy_astype.py`

:English:
    #. Given ``a: ndarray`` (see below)
    #. Convert to ``int`` type
    #. The result convert to ``bool`` type
    #. What happened in each of those steps?

:Polish:
    #. Dany ``a: ndarray`` (patrz sekcja input)
    #. Przekonwertuj do typu ``int``
    #. Rezultat rzutuj na typ ``bool``
    #. Co się stało w każdym z tych kroków?

:Input:
    .. code-block:: python

        a = np.array([[-1.1, 0.0, 1.1],
                      [ 2.2, 3.3, 4.4]])

:The whys and wherefores:
    * Defining ``np.array``
