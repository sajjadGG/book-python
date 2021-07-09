Accessor About
==============


Rationale
---------
* Disable attribute modification
* Logging value access
* Check boundary
* Raise exceptions (TypeError)
* Check argument type


Problem
-------
.. code-block:: python

    class Point:
        x: int

        def get_x(self): pass
        def set_x(self, newvalue): pass
        def del_x(self): pass


    pt = Point()
    pt.set_x(1)

.. code-block:: python

    class Point:
        x: int
        y: int

        def get_x(self): pass
        def set_x(self, newvalue): pass
        def del_x(self): pass
        def get_y(self): pass
        def set_y(self, newvalue): pass
        def del_y(self): pass


    pt = Point()
    pt.set_x(1)
    pt.set_y(1)

.. code-block:: python

    class Point:
        x: int
        y: int
        z: int

        def get_x(self) -> int: pass
        def get_x(self): pass
        def set_x(self, newvalue): pass
        def del_x(self): pass
        def get_y(self): pass
        def set_y(self, newvalue): pass
        def del_y(self): pass
        def get_z(self): pass
        def set_z(self, newvalue): pass
        def del_z(self): pass


    pt = Point()
    pt.set_x(1)
    pt.set_y(1)
    pt.set_z(1)


Encapsulation
-------------
.. code-block:: python

    class Point:
        x: int
        y: int
        z: int

        def set_position(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def get_position(self):
            return self.x, self.y, self.z


        pt = Point()
        pt.set_position(1, 2, 3)
        pt.get_position()

Works for point.
How about astronauts

.. code-block:: python

    class Astronaut:
        firstname: str
        middlename: str
        lastname: str

        def get_name(self):
            return f'{self.firstname} {self.middlename} {self.lastname}'

        def set_name(self, name):
            first, mid, last = name.split()
            self.firstname = first
            self.middlename = mid
            self.lastname = last

* Do everyone have a middle name?
* Do everyone have first or lastname?
* Why split by space?
* What if someone has firstname like `Merry Jane`?
* Or lastname like `Jan Twardowski III`? (Twardowski is not his
  middlename, and `III` is only a part of his lastname)

We can do better:

.. code-block:: python

    class Astronaut:
        firstname: str
        middlename: str
        lastname: str

        def get_name(self):
            return self.firstname, self.middlename, self.lastname

        def set_name(self, firstname, middlename, lastname):
            self.firstname = firstname
            self.middlename = middlename
            self.lastname = lastname

But what if we have a classes:

.. code-block:: python

    class Mission:
        year: int
        name: str


    class Astronaut:
        firstname: str
        middlename: str
        lastname: str
        agency: str
        age: int
        height: float
        weight: float
        missions: list['Mission']
        friends: list['Astronaut']

We can either create one big setter, one big getter and one big deleter
(which is by the way not a good idea) or create setter, getter and deleter
one per each field. This way we ends up with many methods just in case
if we need to implement validation later on in the system, which virtually
never happens.


Solution
--------
Why not to directly interact with attributes? Let's break the
encapsulation. That would make everything much simpler. No setters,
getters and deletes required.

.. code-block:: python

    class Point:
        x: int
        y: int
        z: int

    pt = Point()
    pt.x = 1
    pt.y = 2
    pt.z = 3

But what if we want to make validation:

.. code-block:: python

    class Point:
        x: int
        y: int
        z: int

        def set_x(self, newvalue):
            if newvalue < 0:
                raise ValueError
            self.x = newvalue

        def set_y(self, newvalue):
            if newvalue < 0:
                raise ValueError
            self.y = newvalue

        def set_z(self, newvalue):
            if newvalue < 0:
                raise ValueError
            self.z = newvalue

We can refactor this code:

.. code-block:: python

    class Point:
        x: int
        y: int
        z: int

        def _valid(self, value):
            if newvalue < 0:
                raise ValueError
            return value

        def set_x(self, newvalue):
            self.x = self._valid(newvalue)

        def set_y(self, newvalue):
            self.y = self._valid(newvalue)

        def set_z(self, newvalue):
            self.z = self._valid(newvalue)

But problem persist.

What if all parameters can have different ranges:

    - age between 0 and 130
    - height between 150 and 210
    - name first capital letter, then lowercased letters
