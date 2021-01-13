Command
=======


Rationale
---------
* EN: Command
* PL: Polecenie
* Type: object


Use Cases
---------
* GUI Buttons, menus
* Macro recording
* Multi level undo/redo (See Tutorial)
* Networking — send whole command objects across a network, even as a batch
* Parallel processing or thread pools
* Transactional behaviour — Rollback whole set of commands, or defer till later
* Wizards

* Source [medium]_


Design
------
* Receiver — The Object that will receive and execute the command
* Invoker — Which will send the command to the receiver
* Command Object — Itself, which implements an execute, or action method, and contains all required information
* Client — The main application or module which is aware of the Receiver, Invoker and Commands

.. figure:: ../_img/designpatterns-command-usecase.png
.. figure:: ../_img/designpatterns-command-gof.png


Example
-------
.. literalinclude:: ../_src/designpatterns-command.py
    :language: python


Assignments
-----------
.. todo:: Create assignments


References
----------
.. [medium] https://medium.com/design-patterns-in-python/command-design-pattern-in-python-2f15b09f3774
