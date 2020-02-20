*************
Inner Classes
*************


.. code-block:: python

    class User:
        class DoesNotExists(Exception):
            pass

        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def find_in_databse(self):
            if not in DATABASE:
                raise User.DoesNotExists


    try:
        user = User('Mark', 'Watney')
        user.find_in_database()
    except User.DoesNotExists:
        print('User does not exists')
