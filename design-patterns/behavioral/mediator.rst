Mediator
========


Rationale
---------
* EN: Mediator
* PL: Mediator
* Type: object


Use Cases
---------
* Input fields which needs to collaborate
* Cannot submit form if all required fields are not filled
* If you select article in list of articles, editor form with current article content and title gets populated
* Auto slug-field based on title content


Design
------
.. figure:: img/designpatterns-mediator-gof.png

Problem
-------
.. figure:: img/designpatterns-mediator-problem.png


Implementation
--------------
.. figure:: img/designpatterns-mediator-usecase-1.png
.. figure:: img/designpatterns-mediator-usecase-2.png

.. literalinclude:: ../_src/designpatterns-mediator.py
    :language: python

Mediator with Observer Pattern:

.. literalinclude:: ../_src/designpatterns-mediator-observer.py
    :language: python


Assignments
-----------
.. literalinclude:: assignments/designpatterns_mediator.py
    :caption: :download:`Solution <assignments/designpatterns_mediator.py>`
    :end-before: # Solution
