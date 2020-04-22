.. _OOP Inheritance:

***********
Inheritance
***********


About
=====
* Parent - superclass
* Child - subclass
* Inherit all fields and methods from parent


Simple Inheritance
==================
.. code-block:: python

    class Engineer:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

    class Astronaut(Engineer):
        pass

    class Cosmonaut(Engineer):
        pass


    mark = Astronaut('Mark', 'Watney')
    ivan = Cosmonaut('Ivan', 'Ivanovic')

.. code-block:: python

    class Vehicle:
        pass


    class Car(Vehicle):
        pass

    class Truck(Vehicle):
        pass

.. code-block:: python

    class Iris:
        def __init__(self, sepal_length, sepal_width,
                     petal_length, petal_width, species):

            self.sepal_length = sepal_length
            self.sepal_width = sepal_width
            self.petal_length = petal_length
            self.petal_width = petal_width
            self.species = species


    class Setosa(Iris):
        pass

    class Versicolor(Iris):
        pass

    class Virginica(Iris):
        pass


    setosa = Setosa(
        sepal_length=5.1,
        sepal_width=3.5,
        petal_length=1.4,
        petal_width=0.2,
        species='setosa'
    )


Multilevel Inheritance
======================
.. code-block:: python
    :caption: Multilevel Inheritance

    class Scientist:
        pass

    class Engineer(Scientist):
        pass

    class Astronaut(Engineer):
        pass


    watney = Astronaut()

    isinstance(watney, Scientist)   # True
    isinstance(watney, Engineer)    # True
    isinstance(watney, Astronaut)   # True

    type(watney)                    # <class '__main__.Astronaut'>

.. code-block:: python

    class Vehicle:
        pass

    class VehicleWithWindows(Vehicle):
        pass


    class Car(VehicleWithWindows):
        pass

    class Truck(VehicleWithWindows):
        pass

    class Motorcycle(Vehicle):
        pass

Multiple Inheritance
====================
.. code-block:: python
    :caption: Multiple Inheritance

    class Scientist:
        pass

    class Engineer:
        pass

    class Astronaut(Scientist, Engineer):
        pass


    watney = Astronaut()

    isinstance(watney, Scientist)   # True
    isinstance(watney, Engineer)    # True
    isinstance(watney, Astronaut)   # True

    type(watney)                    # <class '__main__.Astronaut'>

.. code-block:: python

    class Vehicle:
        pass

    class HasWindows:
        pass


    class Car(Vehicle, HasWindows):
        pass

    class Truck(Vehicle, HasWindows):
        pass

    class Motorcycle(Vehicle):
        pass


Calling parent methods
======================
.. code-block:: python

    class Engineer:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name
            self.education = 'Engineer'
            self.profession = 'Engineer'

    class Astronaut(Engineer):
        def __init__(self, first_name, last_name):
            super().__init__(first_name, last_name)
            self.profession = 'Astronaut'


    mark = Astronaut('Mark', 'Watney')

    print(mark.__dict__)
    # {'first_name': 'Mark',
    #  'last_name': 'Watney',
    #  'education': 'Engineer',
    #  'profession': 'Astronaut'}


Assignments
===========
.. todo:: Create Assignments
