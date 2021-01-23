Any
===


Rationale
---------
Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:


Implementation
--------------
.. code-block:: python

    def any(iterable):
        if not iterable:
            return False
        for element in iterable:
            if element:
                return True
        return False
