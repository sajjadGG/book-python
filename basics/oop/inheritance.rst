.. _OOP Inheritance:

***************
OOP Inheritance
***************


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


    setosa = Setosa()

    setosa.species     # setosa
    setosa.genus       # iris
    setosa.kingdom     # plantae


Multiple Inheritance
====================
.. code-block:: python

    class Flower:
        kingdom = 'plantae'

    class Iris:
        genus = 'iris'

    class Setosa(Flower, Iris):
        species = 'setosa'


    setosa = Setosa()

    setosa.species     # setosa
    setosa.genus       # iris
    setosa.kingdom     # plantae


Calling parent methods
======================
.. code-block:: python
    :caption: Using ``super()`` on a class

    class Iris:
        def __init__(self):
            self.sepal_length=5.1
            self.sepal_width=3.5
            self.petal_length=1.4
            self.petal_width=0.2


    class Setosa(Iris):
        def __init__(self):
            super().__init__()
            self.species = 'setosa'


    flower = Setosa()

    flower.sepal_length     # 5.1
    flower.sepal_width      # 3.4
    flower.petal_length     # 1.4
    flower.petal_width      # 0.2
    flower.species          # setosa


Assignments
===========

Objects and relations
---------------------
* Complexity level: medium
* Lines of code to write: 60 lines
* Estimated time of completion: 20 min
* Filename: :download:`solution/basic_relations.py`

:English:
    #. Client can open a bank account
    #. Client can have many accounts
    #. Bank has many clients
    #. Each account has unique number generated when opening an account
    #. Client can ask about number of all of his accounts
    #. Client can add money to the account
    #. Client can withdraw money from the account

:Polish:
    #. Klient może otworzyć konto w banku
    #. Klient może mieć wiele kont
    #. Bank może mieć wielu klientów
    #. Każde konto ma unikalny numer, który jest generowany przy zakładaniu
    #. Klient może odpytać o numery wszystkich swoich kont
    #. Klient może wpłacić pieniądze na swoje konto
    #. Klient może wybrać pieniądze z bankomatu
