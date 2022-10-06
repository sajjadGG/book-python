Observer
========
* EN: Observer
* PL: Obserwator
* Type: object


Pattern
-------
* When the state of the object changes and you need to notify other objects about this change
* Notify chart about changes in data to refresh
* Spreadsheet formulas
* Push or pull style of communication

.. figure:: img/designpatterns-observer-pattern.png

.. literalinclude:: uml/designpatterns-observer-pattern.md
    :language: md

.. figure:: img/designpatterns-observer-push.png
.. figure:: img/designpatterns-observer-pull.png


Problem
-------
.. figure:: img/designpatterns-observer-problem.png

.. literalinclude:: uml/designpatterns-observer-problem.md
    :language: md

.. literalinclude:: src/designpatterns-observer-problem.py
    :language: python


Solution
--------
.. figure:: img/designpatterns-observer-solution.png

.. literalinclude:: uml/designpatterns-observer-solution.md
    :language: md

.. literalinclude:: src/designpatterns-observer-solution-1.py
    :language: python

.. literalinclude:: src/designpatterns-observer-solution-2.py
    :language: python
    :caption: push

.. literalinclude:: src/designpatterns-observer-solution-3.py
    :language: python
    :caption: pull


Assignments
-----------
.. todo:: Assignments
