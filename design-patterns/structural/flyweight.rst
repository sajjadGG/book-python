Flyweight
=========


Rationale
---------
* EN: Flyweight
* PL: Pyłek
* Type: object


Use Cases
---------
* In applications with large number of objects
* Objects take significant amount of memory
* Reduce memory consumed by objects


Problem
-------
* Imagine mapping application, such as: Open Street Maps, Google Maps, Yelp, Trip Advisor etc.
* There are thousands points of interests such as Cafe, Shops, Restaurants, School etc.
* Icons can take a lot of memory, times number of points on the map
* It might crash with out of memory error (especially on mobile devices)

.. literalinclude:: ../_src/designpatterns-flyweight-problem.py
    :language: python


Design
------
.. figure:: img/designpatterns-flyweight-gof.png


Implementation
--------------
* Separate the data you want to share from other data
* Pattern will create a dict with point type and its icon
* It will reuse icon for each type
* So it will prevent from storing duplicated data in memory

.. figure:: img/designpatterns-flyweight-usecase.png

.. literalinclude:: ../_src/designpatterns-flyweight-impl.py
    :language: python


Assignments
-----------
.. todo:: Create assignments
