*********
Built-ins
*********


Pi number
=========
.. code-block:: python

    import numpy as np


    np.pi
    # 3.1415926535897931

Euler number
============
.. code-block:: python

    import numpy as np


    np.e
    # 2.7182818284590451


Infinite
========
.. code-block:: python

    import numpy as np


    np.inf
    # inf

.. code-block:: python

    import numpy as np


    np.inf + 1          # inf
    np.inf + np.inf     # inf
    np.inf - np.inf     # nan
    np.inf - np.nan     # nan

    np.inf * np.inf     # inf
    np.inf / np.inf     # nan

    0 / np.inf          # 0.0
    np.inf / 0          # ZeroDivisionError: float division by zero

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, np.Inf])
    # array([ 1.,  2., inf])

    np.isfinite(a)
    # array([ True,  True, False])

    np.isinf(a)
    # array([False, False,  True])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, np.Inf])
    # array([ 1.,  2., inf])

    np.isnan(a)
    # array([False, False, False])


Not-a-Number
============
* Special ``float`` value
* Propagates in calculations

.. code-block:: python

    import numpy as np


    np.nan
    # nan

.. code-block:: python

    import numpy as np


    np.nan + 1          # nan
    np.nan + np.nan     # nan
    np.nan - np.nan     # nan
    np.nan - np.inf     # nan

    np.nan / np.nan     # nan
    0 / np.nan          # nan
    np.nan / 0          # ZeroDivisionError: float division by zero

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, np.NaN])
    # array([ 1.,  2., nan])

    np.isnan(a)
    # array([False, False,  True])

.. code-block:: python

    import numpy as np


    a = np.array([1, 2, np.NaN])
    # array([ 1.,  2., nan])

    np.isfinite(a)
    # array([ True,  True, False])

    np.isinf(a)
    # array([False, False, False])



Assignments
===========
.. todo:: Create assignments
