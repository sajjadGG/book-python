***********
Classmethod
***********


Rationale
=========
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required


Examples
========
.. code-block:: python

    import json


    class JSONSerializable:
        def to_json(self):
            return json.dumps(self.__dict__)

        @classmethod
        def from_json(cls, data):
            data = json.loads(data)
            return cls(**data)


    class User:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def __str__(self):
            return f'{self.firstname} {self.lastname}'

    class Guest(User, JSONSerializable):
        pass

    class Admin(User, JSONSerializable):
        pass


    DATA = '{"firstname": "Jan", "lastname": "Twardowski"}'

    guest = Guest.from_json(DATA)
    admin = Admin.from_json(DATA)

    type(guest)     # <class '__main__.Guest'>
    type(admin)      # <class '__main__.Admin'>


Assignments
===========

Protocol Classmethod
--------------------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 13 min
* Solution: :download:`solution/protocol_classmethod.py`

.. warning:: Assinmnent is to complex and has issues with pickling object, with does not demonstrate ``@classmethod``
.. todo:: Rewrite the assignment

:English:
    #. Use data from "Input" section (see below)
    #. Model class based on input data
    #. Create class ``PickleSerializable`` with methods ``.to_pickle()`` and ``.from_pickle()``
    #. Use ``@classmethod`` decorator
    #. Create instances for input data
    #. Pickle data and write to file
    #. Unpickle data from file

:Polish:
    #. Użyj danych z sekcji "Input" (patrz poniżej)
    #. Zamodeluj klasę na podstawie danych wejściowych
    #. Stwórz klasę ``PickleSerializable`` z metodami ``.to_pickle()`` i ``.from_pickle()``
    #. Użyj dekoratora ``@classmethod``
    #. Stwórz instancje dla danych wejściowych (see below)
    #. Spikluj dane do pliku
    #. Rozpikluj dane z pliku

:Input Data:
    .. code-block:: text

        Mark, Watney, Astronaut
        Jan, Twardowski, Cosmonaut
        Melissa, Lewis, Astronaut
        Ivan, Ivanovic, Cosmonaut
