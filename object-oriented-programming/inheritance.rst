***********
Inheritance
***********


Simple inheritance
==================
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

    class Flower:
        kingdom = 'plantae'

    class Iris(Flower):
        genus = 'iris'

    class Setosa(Iris):
        species = 'setosa'


Multiple Inheritance
====================
.. code-block:: python
    :caption: Multiple inheritance.

    class JSONMixin:
        def to_json(self):
            return ...

    class CSVMixin:
        def to_csv(self):
            return ...

    class User(JSONMixin, CSVMixin):
        def __init__(self, first_name, last_name):
            ...

Calling object parent
=====================
.. code-block:: python
    :caption: Using ``super()`` on a class

    class Astronaut:
        def say_hello(self):
            print('I am an astronaut')


    class FictionalAstronaut(Astronaut):
        def say_hello(self):
            print(f'My name... José Jiménez')
            super().say_hello()


    jose = FictionalAstronaut()
    jose.say_hello()
    # My name... José Jiménez
    # I am an astronaut
