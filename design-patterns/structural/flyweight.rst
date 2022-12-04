Flyweight
=========
* EN: Flyweight
* PL: Pyłek
* Type: object


Pattern
-------
* In applications with large number of objects
* Objects take significant amount of memory
* Reduce memory consumed by objects

.. figure:: img/designpatterns-flyweight-pattern.png

.. literalinclude:: uml/designpatterns-flyweight-pattern.md
    :language: md


Problem
-------
* Imagine mapping application, such as: Open Street Maps, Google Maps, Yelp, Trip Advisor etc.
* There are thousands points of interests such as Cafe, Shops, Restaurants, School etc.
* Icons can take a lot of memory, times number of points on the map
* It might crash with out of memory error (especially on mobile devices)

.. figure:: img/designpatterns-flyweight-problem.png

.. literalinclude:: uml/designpatterns-flyweight-problem.md
    :language: md

.. literalinclude:: src/designpatterns-flyweight-problem.py
    :language: python


Solution
--------
* Separate the data you want to share from other data
* Pattern will create a dict with point type and its icon
* It will reuse icon for each type
* So it will prevent from storing duplicated data in memory

.. figure:: img/designpatterns-flyweight-solution.png

.. literalinclude:: uml/designpatterns-flyweight-solution.md
    :language: md

.. literalinclude:: src/designpatterns-flyweight-solution.py
    :language: python


Assignments
-----------
.. todo:: Assignments
