****************
``@classmethod``
****************


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
    :emphasize-lines: 7-10,21,24,30,31

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


    DATA = '{"first_name": "Jan", "last_name": "Twardowski"}'

    guest = Guest.from_json(DATA)
    admin = Admin.from_json(DATA)

    type(guest)     # <class '__main__.Guest'>
    type(admin)      # <class '__main__.Admin'>
