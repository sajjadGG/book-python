.. testsetup::

    # doctest: +SKIP_FILE


Dragon ADR Position Set
=======================
* ADR - Architecture Design Records


Problem
-------
* Set new position to x=10, y=20


Option 1
--------
>>> dragon.fly(10, 20)
>>> dragon.teleport(10, 20)

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: method names are too use-case specific
* Bad: arguments are implicit, require knowledge of an API what are the values provided as arguments
* Verdict: rejected, too use-case specific names


Option 2
--------
>>> dragon.fly(x=10, y=20)
>>> dragon.teleport(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: method names are too use-case specific
* Verdict: rejected, too use-case specific names


Option 3
--------
>>> dragon.set_position(10, 20)

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Bad: arguments are implicit, require knowledge of an API what are the values provided as arguments
* Verdict: rejected, could be done better


Option 4
--------
>>> dragon.set_position_xy(10, 20)

* Good: easy to use
* Good: encapsulation
* Good: easy to add validation if needed
* Bad: name ``set_position_xy()`` ties you to 2D point
* Verdict: rejected, could be done better


Option 5
--------
>>> dragon.set_position(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: encapsulation
* Good: easy to add validation if needed
* Good: easy to extend to 3D - add parameter with default value ``0``
* Verdict: candidate


Option 6
--------
>>> dragon.set(position_x=10, position_y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: easy to add validation if needed
* Bad: ``set()`` is to generic
* Bad: gateway to abuse
* Bad: encapsulation is question
* Verdict: rejected, possibility of abuse


Option 7
--------
>>> dragon.x = 10
>>> dragon.y = 20

>>> dragon.x, dragon.y = 10, 20

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Bad: encapsulation
* Bad: names ``x`` and ``y`` are weakly related to ``dragon``
* Verdict: rejected, bad names

Example:

>>> knn = KNearestNeighbors(k=3)
>>> knn.w = [1, 2, 3]


Option 8
--------
>>> dragon.position_x = 10
>>> dragon.position_y = 20

>>> dragon.position_x, dragon.position_y = 10, 20

* Good: easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed in future
* Bad: violates encapsulation - OOP good practices
* Verdict: rejected, violates encapsulation

Example:

>>> knn = KNearestNeighbors(k=3)
>>> knn.weights = [1, 2, 3]


Option 9
--------
>>> dragon.position = (10, 20)
>>> dragon.position @ (10, 20)

* Good: easy to use
* Good: can use ``@property`` for validation if needed
* Good: using ``@`` (matmul) it is easy to validation
* Bad: ``@`` (at) makes sense only in English
* Bad: arguments are implicit
* Bad: require knowledge of an API
* Bad: always 2D
* Bad: not extensible, hard to refactor to 3D
* Bad: violates encapsulation - OOP good practices
* Verdict: rejected, violates encapsulation


Option 10
---------
>>> dragon.position = Point(x=10, y=20)
>>> dragon.position @ Point(x=10, y=20)

* Good: easy to use
* Good: can use ``@property`` for validation if needed
* Good: arguments are explicit
* Good: readability
* Bad: ``@`` (at) makes sense only in English
* Bad: require knowledge of an API
* Bad: extensible, easy to refactor to 3D
* Bad: violates encapsulation - OOP good practices
* Verdict: rejected, violates encapsulation


Option 11
---------
>>> dragon.position.x = 10
>>> dragon.position.y = 20

>>> dragon.position.x, dragon.position.y = 10, 20

* Good: more or less easy to use
* Good: arguments are explicit
* Good: can use ``@property`` for validation if needed
* Good: namespace
* Good: more or less readable
* Good: extensible, easy to refactor to 3D
* Bad: violates encapsulation - OOP good practices
* Bad: nested objects
* Bad: require knowledge of an API
* Verdict: rejected, violates encapsulation


Decision
--------
>>> dragon.set_position(x=10, y=20)

* Good: easy to use
* Good: arguments are explicit
* Good: provides encapsulation
* Good: easy to add validation if needed
* Good: extensible, easy to refactor to 3D
