*************
State Machine
*************

* StateMachine imposes a structure to automatically change the implementation from one object to the next
* The current implementation represents the state that a system is in
* System behaves differently from one state to the next
* The code that moves the system from one state to the next
* Each state can be ``run()`` to perform its behavior
* You can pass it an ``input`` object so it can tell you what new state to move to based on that ``input``
* Each State object decides what other states it can move to, based on the ``input``
* Each State object has its own little State table
* There is a single master state transition table for the whole system

.. code-block:: text

    statemachine TrafficLight:
        Red -> Amber
        Amber (if previous == Red) -> Green
        Green -> Amber
        Amber (if previous == Green) -> Red


    Red.wait = sleep(2)
    Amber.wait = sleep(1)
    Green.wait = sleep(2)


.. literalinclude:: src/design-patterns-state-machine.py
    :language: python
    :caption: State Machine
