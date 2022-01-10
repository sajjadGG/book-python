Array Random
============


Rationale
---------
* Since ``numpy v1.17``: BitGenerator for the PCG-64 (Parallel Congruent
  Generator 64 bit) pseudo-random number generator

* Before ``numpy v1.17``: Mersenne Twister algorithm for pseudorandom
  number generation


Pseudorandom Generator
----------------------
>>> from time import time
>>>
>>>
>>> def randint(maximum=10):
...     return int(time()) % maximum
>>>
>>>
>>> randint()  # doctest: +SKIP
3
>>> randint()  # doctest: +SKIP
4
>>> randint()  # doctest: +SKIP
5
>>> randint()  # doctest: +SKIP
6

>>> from time import time
>>>
>>>
>>> def randint(maximum=10):
...     cpu_temperature = 52.4123123
...     return int(time() * cpu_temperature) % maximum
>>>
>>>
>>> randint()  # doctest: +SKIP
7
>>> randint()  # doctest: +SKIP
2
>>> randint()  # doctest: +SKIP
5
>>> randint()  # doctest: +SKIP
1

>>> from time import time
>>>
>>>
>>> def randint(maximum=10):
...     cpu_temperature = 52.4123123
...     fan_speed = 1200
...     ram_voltage = 1.42321321
...     network_crc = 9876
...     return int(time() * cpu_temperature * fan_speed * ram_voltage * network_crc) % maximum
>>>
>>>
>>> randint()  # doctest: +SKIP
3
>>> randint()  # doctest: +SKIP
0
>>> randint()  # doctest: +SKIP
2
>>> randint()  # doctest: +SKIP
8


Seed
----
* Seed the generator
* Using setting seed to the same value will always generate the same
  pseudorandom values

>>> import numpy as np
>>>
>>>
>>> np.random.seed(0)


Assignments
-----------
.. literalinclude:: assignments/numpy_random_a.py
    :caption: :download:`Solution <assignments/numpy_random_a.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_random_b.py
    :caption: :download:`Solution <assignments/numpy_random_b.py>`
    :end-before: # Solution

.. literalinclude:: assignments/numpy_random_c.py
    :caption: :download:`Solution <assignments/numpy_random_c.py>`
    :end-before: # Solution
