*************
Inner Classes
*************


.. code-block:: python

    class User:
        class DoesNotExists(Exception):
            pass

        def __init__(self, firstname, lastname):
            if not login(firstname, lastname):
                raise User.DoesNotExists

