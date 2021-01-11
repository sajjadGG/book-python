State Machine
=============

Rationale
---------
* EN: State Machine
* PL: Maszyna Stanów
* Type: class

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


Use Cases
---------


Design
------


Example
-------
.. code-block:: python

    from time import sleep


    class Light:
        def __init__(self, previous=None):
            self.previous = previous

        def run(self):
            raise NotImplementedError

        def __next__(self):
            raise NotImplementedError


    class Red(Light):
        color = 'Red'
        wait = 2

        def run(self):
            print(self.color)
            sleep(self.wait)

        def __next__(self):
            return Amber(previous=self)


    class Amber(Light):
        color = 'Amber'
        wait = 1

        def run(self):
            print(self.color)
            sleep(self.wait)

        def __next__(self):
            if isinstance(self.previous, Red):
                return Green(previous=self)
            else:
                return Red(previous=self)


    class Green(Light):
        color = 'Green'
        wait = 2

        def run(self):
            print(self.color)
            sleep(self.wait)

        def __next__(self):
            return Amber(previous=self)


    class TrafficLights:
        def __init__(self, initial_state=Green(), max_changes=10):
            self.state = initial_state
            self.max_changes = max_changes

        def __iter__(self):
            self.changes = 0
            return self

        def __next__(self):
            if self.changes >= self.max_changes:
                raise StopIteration

            self.changes += 1
            self.state.run()
            self.state = next(self.state)
            return self


    for light in TrafficLights(max_changes=10):
        pass


Assignments
-----------
.. todo:: Create assignments


