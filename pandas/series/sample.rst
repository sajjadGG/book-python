*************
Series Sample
*************


Head
====
.. code-block:: python

    s.head(2)
    s.head(n=1)


Tail
=====
.. code-block:: python

    s.tail(2)
    s.tail(n=1)


First
=====
.. code-block:: python

    s.first('Y')
    s.first('M')
    s.first('D')
    s.first('W')


Last
====
.. code-block:: python

    s.last('Y')
    s.last('M')
    s.last('D')
    s.last('W')


Sample
======
* 1/4 is 25%
* .05 is 5%
* 0.5 is 50%
* 1.0 is 100%

.. code-block:: python
    :caption: `n` number or fraction random rows with and without repetition

    s.sample()
    s.sample(2)
    s.sample(n=2, replace=True)
    s.sample(frac=1/4)
    s.sample(frac=0.5)


Reset Index
===========
.. code-block:: python

    s.sample(frac=1.0).reset_index()


Assignments
===========

.. todo:: Convert assignments to literalinclude

Series Sample
--------------
* Assignment: Series Sample
* Filename: :download:`assignments/series_sample.py`
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Set random seed to zero
    2. Create ``pd.Series`` with 100 random numbers from standard normal distribution
    3. Series Index are following dates since 2000
    4. Print values:

        a. first in the series,
        b. last 5 elements in the series,
        c. first two weeks in the series,
        d. last month in the series,
        e. three random elements,
        f. 125% of random elements with replacement.

Polish:
    1. Ustaw ziarno losowości na zero
    2. Stwórz ``pd.Series`` z 100 losowymi liczbami z rozkładu normalnego
    3. Indeksem w serii mają być kolejne dni od 2000 roku
    4. Wypisz wartości:

        a. pierwszy w serii,
        b. ostatnie 5 elementów w serii,
        c. dwa pierwsze tygodnie w serii,
        d. ostatni miesiąc w serii,
        e. trzy losowe element,
        f. 125% losowych elementów z powtórzeniami.

Hints:
    * ``np.random.seed(0)``
    * ``np.random.randn(n)``
