.. _Math Precision:

Math Precision
**************


Minimal and Maximal Values
==========================
Maximal and minimal ``float`` values:

.. code-block:: python

    import sys

    sys.float_info.min      # 2.2250738585072014e-308
    sys.float_info.max      # 1.7976931348623157e+308


Infinity
========
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
============
.. code-block:: python

    float('nan')
    # nan

    float('-nan')
    # nan


NaN vs Inf
==========
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


Floating Numbers Precision
==========================

.. code-block:: python

    0.1
    # 0.1

    0.2
    # 0.2

    0.3
    # 0.3

.. code-block:: python

    0.1 + 0.2 == 0.3
    # False

.. code-block:: python

    0.1 + 0.2
    # 0.30000000000000004

.. code-block:: python

    0.1 + 0.1
    # 0.2

    0.1 + 0.1 + 0.1
    # 0.30000000000000004

.. code-block:: python

    round(0.1+0.2, 16)
    # 0.3

    round(0.1+0.2, 17)
    # 0.30000000000000004

.. code-block:: python

    round(0.1+0.2, 16)
    # True

    round(0.1+0.2, 17) == 0.3
    # False


IEEE 754 standard
=================
.. figure:: img/float-anatomy.png

    What is ``float`` as defined by IEEE 754 standard

.. figure:: img/float-expression.png

    Points chart

.. figure:: img/float-mantissa-1.png

    How computer store ``float``?
    As defined by IEEE 754 standard

.. figure:: img/float-mantissa-2.png

    How to read/write ``float`` from/to memory?

.. figure:: img/float-normalized.png

    Normalized Line


Floats in Doctest
=================
.. code-block:: python

    def add(a, b):
        """
        >>> add(1.0, 2.0)
        3.0

        >>> add(0.1, 0.2)
        0.30000000000000004

        >>> add(0.1, 0.2)   # doctest: +ELLIPSIS
        0.3000...
        """
        return a + b


Decimal Type
============
.. code-block:: python

    from decimal import Decimal


    a = Decimal('0.1')
    b = Decimal('0.2')

    a + b
    # Decimal('0.3')

.. code-block:: python

    from decimal import Decimal


    a = Decimal('0.3')

    float(a)
    # 0.3

