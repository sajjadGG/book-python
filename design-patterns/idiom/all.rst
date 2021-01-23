All
===


Rationale
---------
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:


Implementation
--------------
.. code-block:: python

    def all(iterable):
        if not iterable:
            return False
        for element in iterable:
            if not element:
                return False
        return True
