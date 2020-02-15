***************
``classmethod``
***************


What it is?
===========
* Using class as namespace
* Will pass class as a first argument
* ``self`` is not required


When use it?
============


Example
=======
.. code-block:: python
    :emphasize-lines: 8-11,22,25,31,32

    import json


    class JSONSerializable:
        def to_json(self):
            return json.dumps(self.__dict__)

        @classmethod
        def from_json(cls, data):
            data = json.loads(data)
            return cls(**data)


    class User:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def __str__(self):
            return f'{self.first_name} {self.last_name}'

    class Guest(User, JSONSerializable):
        pass

    class Admin(User, JSONSerializable):
        pass


    INPUT = '{"first_name": "Jan", "last_name": "Twardowski"}'

    guest = Guest.from_json(INPUT)
    admin = Admin.from_json(INPUT)

    type(guest)     # <class '__main__.Guest'>
    type(admin)      # <class '__main__.Admin'>


Assignments
===========

Pickle
------
* Complexity level: easy
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/classmethod_pickle.py`

:English:
    #. Model class based on input data (see below)
    #. Create class ``PickleSerializable`` with methods ``.to_pickle()`` and ``.from_pickle()``
    #. Use ``@classmethod`` decorator
    #. Create instances for input data
    #. Pickle data and write to file
    #. Unpickle data from file

:Polish:
    #. Zamodeluj klasę na podstawie danych wejściowych (patrz sekcja input)
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
