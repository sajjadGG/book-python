State
=====


Rationale
---------
* EN: State
* PL: Stan
* Type: object


Use Cases
---------
* Changes based on class
* Open/Close principle
* Using polymorphism


Design
------
* Canvas object can behave differently depending on selected Tool
* All behaviors are represented by subclass of the tool interface

.. figure:: ../_img/designpatterns-state-usecase.png
.. figure:: ../_img/designpatterns-state-gof.png


Example
-------
.. literalinclude:: ../_src/designpatterns-state.py
    :language: python


Assignments
-----------
.. todo:: Create assignments
