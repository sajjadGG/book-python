Math IEEE-754
=============

Floating-point numbers are not real numbers, so the result of ``1.0/3.0``
cannot be represented exactly without infinite precision. In the decimal
(base 10) number system, one-third is a repeating fraction, so it has an
infinite number of digits. Even simple non-repeating decimal numbers can
be a problem. One-tenth (0.1) is obviously non-repeating, so we can express
it exactly with a finite number of digits. As it turns out, since numbers
within computers are stored in binary (base 2) form, even one-tenth cannot
be represented exactly with floating-point numbers. [#Halterman2018]_

When should you use integers and when should you use floating-point numbers?
A good rule of thumb is this: use integers to count things and use
floating-point numbers for quantities obtained from a measuring device.
As examples, we can measure length with a ruler or a laser range finder;
we can measure volume with a graduated cylinder or a flow meter; we can
measure mass with a spring scale or triple-beam balance. In all of these
cases, the accuracy of the measured quantity is limited by the accuracy
of the measuring device and the competence of the person or system
performing the measurement. Environmental factors such as temperature
or air density can affect some measurements. In general, the degree
of inexactness of such measured quantities is far greater than that
of the floating-point values that represent them. [#Halterman2018]_

Despite their inexactness, floating-point numbers are used every day
throughout the world to solve sophisticated scientific and engineering
problems. The limitations of floating-point numbers are unavoidable since
values with infinite characteristics cannot be represented in a finite way.
Floating-point numbers provide a good trade-off of precision for practicality.
[#Halterman2018]_

>>> 0.1
0.1
>>>
>>> 0.2
0.2
>>>
>>> 0.3
0.3
>>>
>>> 0.1 + 0.2 == 0.3
False

>>> round(0.1+0.2, 16) == 0.3
True
>>>
>>> round(0.1+0.2, 17) == 0.3
False

>>> 0.1 + 0.2
0.30000000000000004


Problem
-------
>>> candy = 0.10      # price in dollars
>>> cookie = 0.20     # price in dollars
>>>
>>> result = candy + cookie
>>> print(result)
0.30000000000000004

>>> (candy+cookie) * 1
0.30000000000000004
>>>
>>> (candy+cookie) * 10
3.0000000000000004
>>>
>>> (candy+cookie) * 100
30.000000000000004
>>>
>>> (candy+cookie) * 1000
300.00000000000006
>>>
>>> (candy+cookie) * 10000
3000.0000000000005
>>>
>>> (candy+cookie) * 100000
30000.000000000004


IEEE 754 standard
-----------------
>>> import numpy as np

>>> a = 1.234
>>> b = 1234 * 10**-3
>>>
>>> a == b
True
>>>
>>> 1234 * 10**-3
1.234
>>>
>>> 1.234 == 1234 * 10e-4
True

Write to memory:

>>> sign = 0  # 0 is plus; 1 is minus
>>> mantissa = 1234
>>> exponent = -3
>>>
>>> sign, exponent, mantissa
(0, -3, 1234)
>>>
>>> sign = np.binary_repr(0, width=1)          # '0'
>>> exponent = np.binary_repr(-3, width=8)     # '11111101'
>>> mantissa = np.binary_repr(1234, width=23)  # '00000000000010011010010'
>>>
>>> print(sign, exponent, mantissa, sep='')
01111110100000000000010011010010

Read from memory:

>>> sign = 0  # 0 is plus; 1 is minus
>>> mantissa = 1234
>>> exponent = -3
>>>
>>> mantissa * 10 ** exponent
1.234

.. warning:: This is only demonstration for such conversion.
             I used simplified formula, to demonstrate how it could be done.
             Actual formula varies from above example.

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
-----------------
>>> def add(a, b):
...     """
...     >>> add(1.0, 2.0)
...     3.0
...
...     >>> add(0.1, 0.2)
...     0.30000000000000004
...
...     >>> add(0.1, 0.2)   # doctest: +ELLIPSIS
...     0.3000...
...     """
...     return a + b


Decimal Type
------------
>>> from decimal import Decimal

>>> a = Decimal('0.1')
>>> b = Decimal('0.2')
>>>
>>> a + b
Decimal('0.3')

>>> a = Decimal('0.1')
>>> b = Decimal('0.2')
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... a + b
...
105 ns ± 36.4 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> a = 0.1
>>> b = 0.2
>>>
>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... a + b
...
53.6 ns ± 18.7 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... Decimal('0.1') + Decimal('0.2')
...
531 ns ± 136 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

>>> %%timeit -r 1000 -n 1000  # doctest: +SKIP
... 0.1 + 0.2
...
11.6 ns ± 6.22 ns per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


Solutions
---------
* Round values to 4 decimal places (generally acceptable)
* Store values as ``int``, do operation and then divide. For example instead of 1.99 USD, store price as 199 US cents
* Use ``Decimal`` type
* ``Decimal`` type is much slower

Problem:

>>> candy = 0.10      # price in dollars
>>> cookie = 0.20     # price in dollars
>>>
>>> result = candy + cookie
>>> print(result)
0.30000000000000004

Round values to 4 decimal places (generally acceptable):

>>> candy = 0.10      # price in dollars
>>> cookie = 0.20     # price in dollars
>>>
>>> result = round(candy + cookie, 4)
>>> print(result)
0.3

Store values as ``int``, do operation and then divide:

>>> CENT = 1
>>> DOLLAR = 100 * CENT
>>>
>>> candy = 10*CENT
>>> cookie = 20*CENT
>>>
>>> result = (candy + cookie) / DOLLAR
>>> print(result)
0.3

Use ``Decimal`` type:

>>> from decimal import Decimal
>>>
>>>
>>> candy = Decimal('0.10')     # price in dollars
>>> cookie = Decimal('0.20')    # price in dollars
>>>
>>> result = candy + cookie
>>> print(result)
0.30


References
----------
.. [#Halterman2018] Halterman, R.L. Fundamentals of Python Programming. Publisher: Southern Adventist University. Year: 2018.
