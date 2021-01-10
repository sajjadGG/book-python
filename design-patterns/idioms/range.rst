Range
=====

Built-in
--------
* It is not a generator
* optional ``start``, inclusive, default: ``0``
* required ``stop``, exclusive,
* optional ``step``, default: ``1``

``range()`` syntax:

.. code-block:: python

    range([start], <stop>, [step])

>>> range(0,3)
range(0, 3)
>>> list(range(0,3))
[0, 1, 2]
>>> tuple(range(0,3))
(0, 1, 2)
>>> set(range(0,3))
{0, 1, 2}
>>> list(range(4,11,2))
[4, 6, 8, 10]











Itertools
---------
* More information https://docs.python.org/3/library/itertools.html
* More information :ref:`Itertools`
* ``itertools.count(start=0, step=1)``
* ``itertools.cycle(iterable)``
* ``itertools.repeat(object[, times])``
* ``itertools.accumulate(iterable[, func, *, initial=None])``
* ``itertools.chain(*iterables)``
* ``itertools.compress(data, selectors)``
* ``itertools.islice(iterable, start, stop[, step])``
* ``itertools.starmap(function, iterable)``
* ``itertools.product(*iterables, repeat=1)``
* ``itertools.permutations(iterable, r=None)``
* ``itertools.combinations(iterable, r)``
* ``itertools.combinations_with_replacement(iterable, r)``
* ``itertools.groupby(iterable, key=None)``


