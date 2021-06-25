Math Random
===========


``random``
----------
.. csv-table:: ``random``
    :header-rows: 1

    "Function", "Description"
    "``random.random()``", "Random float:  0.0 <= x < 1.0"
    "``random.randint(min, max)``", "Return a random integer N such that ``min <= N <= max``. Max is included"
    "``random.gauss(mu, sigma)``", "Gaussian distribution. mu is the mean, and sigma is the standard deviation"
    "``random.shuffle(list)``", "Randomize order of list (in place)"
    "``random.choice(list)``", "Single random element from a sequence"
    "``random.sample(list, k)``", "k random elements from list without replacement"
    "``random.seed(a=None, version=2)``", "Initialize the random number generator. If a is omitted or None, the current system time is used"


Pseudo and Pure random numbers
------------------------------
* What are pseudorandom numbers?
* Why it is not possible to generate a pure random number?
* What is ``random.seed(0)``?


Assignments
-----------
.. literalinclude:: assignments/math_random_sample.py
    :caption: :download:`Solution <assignments/math_random_sample.py>`
    :end-before: # Solution

.. literalinclude:: assignments/math_random_matrix.py
    :caption: :download:`Solution <assignments/math_random_matrix.py>`
    :end-before: # Solution

.. figure:: img/random-inner-sum.png

    Sum of inner elements
