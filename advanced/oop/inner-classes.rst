*************
Inner Classes
*************


.. code-block:: python

    class User:
        def __init__(self, firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname

        def find_in_database(self):
            if not in DATABASE:
                raise User.DoesNotExists

        class DoesNotExists(Exception):
            pass


    try:
        user = User('Mark', 'Watney')
        user.find_in_database()
    except User.DoesNotExists:
        print('User does not exists')
