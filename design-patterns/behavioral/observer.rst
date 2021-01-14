Observer
========


Rationale
---------
* EN: Observer
* PL: Obserwator
* Type: object


Use Cases
---------
* When the state of the object changes and you need to notify other objects about this change
* Notify chart about changes in data to refresh
* Spreadsheet formulas
* Push or pull style of communication


Design
------
.. figure:: ../_img/designpatterns-observer-usecase.png
.. figure:: ../_img/designpatterns-observer-gof.png
.. figure:: ../_img/designpatterns-observer-push.png
.. figure:: ../_img/designpatterns-observer-pull.png


Implementation
--------------
.. literalinclude:: ../_src/designpatterns-observer.py
    :language: python

.. literalinclude:: ../_src/designpatterns-observer-push.py
    :language: python

.. literalinclude:: ../_src/designpatterns-observer-pull.py
    :language: python


Assignments
-----------
.. todo:: Create assignments
