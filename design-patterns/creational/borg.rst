Borg
====
* EN: Borg
* PL: Borg
* Type: object

The real reason that borg is different comes down to subclassing.
If you subclass a borg, the subclass' objects have the same state
as their parents classes objects, unless you explicitly override
the shared state in that subclass. Each subclass of the singleton
pattern has its own state and therefore will produce different objects.
Also in the singleton pattern the objects are actually the same,
not just the state (even though the state is the only thing that
really matters). [#borg]_


Pattern
-------
.. figure:: img/designpatterns-borg-pattern.png

.. literalinclude:: src/designpatterns-borg-pattern.md
    :language: md


Problem
-------
.. figure:: img/designpatterns-borg-problem.png

.. literalinclude:: src/designpatterns-borg-problem.md
    :language: md

.. literalinclude:: src/designpatterns-borg-problem.py
    :language: python


Solution
--------
.. figure:: img/designpatterns-borg-solution.png

.. literalinclude:: src/designpatterns-borg-solution.md
    :language: md

.. literalinclude:: src/designpatterns-borg-solution.py
    :language: python


References
----------
.. [#borg] https://stackoverflow.com/a/1318444
