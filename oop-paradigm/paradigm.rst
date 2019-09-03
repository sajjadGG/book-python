************
OOP Paradigm
************


Good Engineering Practises
==========================

Tell - don't ask
----------------
* Tell-Don't-Ask is a principle that helps people remember that object-orientation is about bundling data with the functions that operate on that data.
* It reminds us that rather than asking an object for data and acting on that data, we should instead tell an object what to do.
* This encourages to move behavior into an object to go with the data.

.. code-block:: python
    :caption: Tell - don't ask (Bad)

    class Rocket:
        status = 'off'


    soyuz = Rocket()
    soyuz.status = 'on'

.. code-block:: python
    :caption: Tell - don't ask (Good)

    class Rocket:
        status = 'off'

        def ignite(self):
            self.status = 'on'


    soyuz = Rocket()
    soyuz.ignite()


Do not run methods in ``__init__()``
------------------------------------
* Nie powinniśmy uruchamiać innych metod na obiekcie
* Lepiej aby użytkownik sam wykonał metodę jawnie

.. code-block:: python
    :caption: Let user to call method

    class Server:

        def __init__(self, host, username, password=None):
            self.host = host
            self.username = username
            self.password = password
            self.connect()    # Better ask user to ``connect()`` explicitly

        def connect(self):
            print(f'Logging to {self.host} using: {self.username}:{self.password}')


    localhost = Server(
        host='localhost',
        username='admin',
        password='admin'
    )

    # This is better
    localhost.connect()


S.O.L.I.D.
==========

Single responsibility principle
-------------------------------
a class should have only a single responsibility (i.e. changes to only one part of the software's specification should be able to affect the specification of the class)

The single responsibility principle is a computer programming principle that states that every module or class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility. Robert C. Martin expresses the principle as, "A class should have only one reason to change."

Open/closed principle
---------------------
software entities … should be open for extension, but closed for modification

The name open/closed principle has been used in two ways. Both ways use generalizations (for instance, inheritance or delegate functions) to resolve the apparent dilemma, but the goals, techniques, and results are different.

Liskov substitution principle
-----------------------------
objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program. See also design by contract.

Substitutability is a principle in object-oriented programming stating that, in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S (i.e. an object of type T may be substituted with any object of a subtype S) without altering any of the desirable properties of the program (correctness, task performed, etc.).

Interface segregation principle
-------------------------------
many client-specific interfaces are better than one general-purpose interface

The interface-segregation principle (ISP) states that no client should be forced to depend on methods it does not use. ISP splits interfaces that are very large into smaller and more specific ones so that clients will only have to know about the methods that are of interest to them. Such shrunken interfaces are also called role interfaces. ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy. ISP is one of the five SOLID principles of object-oriented design, similar to the High Cohesion Principle of GRASP.

Dependency inversion principle
------------------------------
one should depend upon abstractions, [not] concretions

In object-oriented design, the dependency inversion principle refers to a specific form of decoupling software modules. When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details. The principle states:

    #. High-level modules should not depend on low-level modules. Both should depend on abstractions.
    #. Abstractions should not depend on details. Details should depend on abstractions.

By dictating that both high-level and low-level objects must depend on the same abstraction this design principle inverts the way some people may think about object-oriented programming.


GRASP
=====
**General responsibility assignment software patterns (or principles)**, abbreviated GRASP, consist of guidelines for assigning responsibility to classes and objects in object-oriented design.

The different patterns and principles used in GRASP are controller, creator, indirection, information expert, high cohesion, low coupling, polymorphism, protected variations, and pure fabrication. All these patterns answer some software problem, and these problems are common to almost every software development project. These techniques have not been invented to create new ways of working, but to better document and standardize old, tried-and-tested programming principles in object-oriented design.

