Borg
====
* EN: Borg
* PL: Borg
* Type: object


Implementation
--------------
.. literalinclude:: ../_src/designpatterns-borg.py
    :language: python


Borg vs Singleton
-----------------
* Source [#borg]_

The real reason that borg is different comes down to subclassing.

If you subclass a borg, the subclass' objects have the same state as their parents classes objects, unless you explicitly override the shared state in that subclass. Each subclass of the singleton pattern has its own state and therefore will produce different objects.

Also in the singleton pattern the objects are actually the same, not just the state (even though the state is the only thing that really matters).


References
----------
.. [#borg] https://stackoverflow.com/a/1318444
