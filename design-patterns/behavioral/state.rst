State
=====
* EN: State
* PL: Stan
* Type: object


Pattern
-------
* Changes based on class
* Open/Close principle
* Using polymorphism

.. figure:: img/designpatterns-state-pattern.png

.. literalinclude:: uml/designpatterns-state-pattern.md
    :language: md


Problem
-------
* Canvas object can behave differently depending on selected Tool
* All behaviors are represented by subclass of the tool interface

.. figure:: img/designpatterns-state-problem.png

.. literalinclude:: uml/designpatterns-state-problem.md
    :language: md

.. literalinclude:: src/designpatterns-state-problem.py
    :language: python


Solution
--------
.. figure:: img/designpatterns-state-solution.png

.. literalinclude:: uml/designpatterns-state-solution.md
    :language: md

.. literalinclude:: src/designpatterns-state-solution.py
    :language: python


Assignments
-----------
.. literalinclude:: assignments/designpatterns_state.py
    :caption: :download:`Solution <assignments/designpatterns_state.py>`
    :end-before: # Solution
