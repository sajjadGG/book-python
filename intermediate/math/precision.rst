Math Precision
==============


Minimal and Maximal Values
--------------------------
Maximal and minimal ``float`` values:

.. code-block:: python

    import sys

    sys.float_info.min      # 2.2250738585072014e-308
    sys.float_info.max      # 1.7976931348623157e+308


Infinity
--------
Infinity representation:

.. code-block:: python

    1e308                   # 1e+308
    -1e308                  # -1e+308

    1e309                   # inf
    -1e309                  # -inf

    float('inf')            # inf
    float('-inf')           # -inf

    float('Infinity')       # inf
    float('-Infinity')      # -inf


Not-a-Number
------------
.. code-block:: python

    float('nan')
    # nan

    float('-nan')
    # nan


NaN vs Inf
----------
.. code-block:: python

    float('inf') + float('inf')     # inf
    float('inf') + float('-inf')    # nan
    float('-inf') + float('inf')    # nan
    float('-inf') + float('-inf')   # -inf

    float('inf') - float('inf')     # nan
    float('inf') - float('-inf')    # inf
    float('-inf') - float('inf')    # -inf
    float('-inf') - float('-inf')   # nan

    float('inf') * float('inf')     # inf
    float('inf') * float('-inf')    # -inf
    float('-inf') * float('inf')    # -inf
    float('-inf') * float('-inf')   # inf

    float('inf') / float('inf')     # nan
    float('inf') / float('-inf')    # nan
    float('-inf') / float('inf')    # nan
    float('-inf') / float('-inf')   # nan
