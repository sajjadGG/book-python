Composite
=========
* EN: Composite
* PL: Kompozyt
* Type: object


Pattern
-------
* Represent a hierarchy of objects
* Groups (and subgroups) objects in Keynote
* Files in a Folder; when you move folder you also move files
* allows you to represent individual entities and groups of entities in the same manner.
* is a structural design pattern that lets you compose objects into a tree.
* is great if you need the option of swapping hierarchical relationships around.
* makes it easier for you to add new kinds of components
* conform to the Single Responsibility Principle in the way that it separates the aggregation of objects from the features of the object.

.. figure:: img/designpatterns-composite-pattern.png

.. literalinclude:: uml/designpatterns-composite-pattern.md
    :language: md


Problem
-------
.. figure:: img/designpatterns-composite-problem.png

.. literalinclude:: uml/designpatterns-composite-problem.md
    :language: md

.. literalinclude:: src/designpatterns-composite-problem.py
    :language: python


Solution
--------
.. figure:: img/designpatterns-composite-solution.png

.. literalinclude:: uml/designpatterns-composite-solution.md
    :language: md

.. literalinclude:: src/designpatterns-composite-solution.py
    :language: python


Assignments
-----------
.. literalinclude:: assignments/structural_composite_a.py
    :language: python
