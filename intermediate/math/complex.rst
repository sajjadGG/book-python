.. _Math Complex Numbers:

********************
Math Complex Numbers
********************


* Complex number with real and imaginary parts
* Engineering notation ``j`` not mathematical ``i``
* No space inside the expression

Defining ``complex``
====================
.. code-block:: python

    complex()                # 0j
    complex(real=0, imag=0)  # 0+0j

.. code-block:: python

    complex(1)              # (1+0j)
    complex(imag=1)         # 1j
    complex(real=1)         # (1+0j)

.. code-block:: python

    complex(real=1, imag=2) # (1+2j)
    complex(1, 2)           # (1+2j)
    complex(1.12, 2.34)     # (1.12+2.34j)
    complex(1, 2.34)        # (1+2.34j)

.. code-block:: python

    complex(1+2j)           # (1+2j)
    complex(1+2j, 3+4j)     # (-3+5j)

.. code-block:: python

    complex('1+2j')         # (1+2j)
    complex('1.5+2.7j')     # (1.5+2.7j)
    complex('1 + 2j')       # ValueError: complex() arg is a malformed string


Arithmetic on ``complex``
=========================
.. code-block:: python

    a = complex(1, 2)       # (1+2j)
    b = 3+4j                # (3+4j)

    a + b                   # (4+6j)
    a - b                   # (-2-2j)
    a * b                   # (-5+10j)
    a / b                   # (0.44+0.08j)

Builtin functions
=================

Absolute
--------
.. code-block:: python

    abs(1+2j)
    # 2.23606797749979

    abs(3+4j)
    # 5.0
