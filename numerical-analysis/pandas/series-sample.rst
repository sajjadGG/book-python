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
