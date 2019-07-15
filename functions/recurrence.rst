**********
Recurrence
**********

    Aby zrozumieć rekurencję – musisz najpierw zrozumieć rekursję


What is recurrence?
===================
* Also known as recursion
* Python isn't a functional language
* CPython implementation doesn't optimize tail recursion
* Tail recursion is not a particularly efficient technique in Python
* Unbridled recursion causes stack overflows!
* Rewriting the algorithm iteratively, is generally a better idea

.. code-block:: python

    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

.. code-block:: python

    factorial(5)
        return 5 * factorial(4)
            return 4 * factorial(3)
                return 3 * factorial(2)
                    return 2 * factorial(1)
                        return 1 * factorial(0)
                            return 1


Limit
=====
* Default recursion depth limit is 1000
* Warning: Anaconda sets default recursion depth limit to 2000
* Set limit ``sys.setrecursionlimit(limit)``
