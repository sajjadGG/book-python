OOP Abstract Protocol
=====================
* :pep:`544` -- Protocols: Structural subtyping (static duck typing)
* Since Python 3.8
* Protocol describe an interface, not an implementation
* Protocol classes should not have method implementations
* Protocol can describe both methods and attributes

A class object is considered an implementation of a protocol if accessing
all members on it results in types compatible with the protocol members.


Syntax
------
>>> from typing import Protocol
>>>
>>>
>>> class Message(Protocol):
...     recipient: str
...     body: str
...
...     def send() -> None: ...
...     def receive() -> Message: ...


Terminology
-----------
:pep:`544` propose to use the term protocols for types supporting structural
subtyping. The reason is that the term iterator protocol, for example, is
widely understood in the community, and coming up with a new term for this
concept in a statically typed context would just create confusion
[#PEP544]_.

This has the drawback that the term protocol becomes overloaded with two
subtly different meanings: the first is the traditional, well-known but
slightly fuzzy concept of protocols such as iterator; the second is the
more explicitly defined concept of protocols in statically typed code. The
distinction is not important most of the time, and in other cases we
propose to just add a qualifier such as protocol classes when referring to
the static type concept. [#PEP544]_

If a class includes a protocol in its MRO, the class is called an explicit
subclass of the protocol.

If a class is a structural subtype of a protocol, it is said to implement
the protocol and to be compatible with a protocol. If a class is compatible
with a protocol but the protocol is not included in the MRO, the class is
an implicit subtype of the protocol. (Note that one can explicitly subclass
a protocol and still not implement it if a protocol attribute is set to
None in the subclass, see Python data-model for details.) [#PEP544]_

The attributes (variables and methods) of a protocol that are mandatory for
other class in order to be considered a structural subtype are called
protocol members. [#PEP544]_


Explicit Subtyping
------------------
* ``Email`` is explicit subclass of the protocol

If a class includes a protocol in its MRO, the class is called an explicit
subclass of the protocol.

>>> from typing import Protocol
>>>
>>>
>>> class Message(Protocol):
...     recipient: str
...     body: str
>>>
>>>
>>> class Email(Message):
...     sender: str
...     recipient: str
...     subject: str
...     body: str
>>>
>>>
>>> def send(message: Message):
...     ...
>>>
>>>
>>> email = Email()
>>> email.sender = 'mwatney@nasa.gov',
>>> email.recipient = 'mlewis@nasa.gov',
>>> email.subject = 'I am alive!'
>>> email.body = 'I survived the storm. I am alone on Mars.')
>>>
>>> send(email)  # will pass the checker


Structural Subtyping
--------------------
* If an object that has all the protocol attributes it implements it
* Structural subtyping is natural for Python programmers
* Matches the runtime semantics of duck typing
* ``Email`` is structural subtype of a protocol (it conforms to structure)
* ``Email`` is implicit subtype of the protocol ``Message`` (not inherits)
* ``Email`` implement the protocol ``Message``
* ``Email`` is compatible with a protocol ``Message``

If a class is a structural subtype of a protocol, it is said to implement
the protocol and to be compatible with a protocol. If a class is compatible
with a protocol but the protocol is not included in the MRO, the class is
an implicit subtype of the protocol. (Note that one can explicitly subclass
a protocol and still not implement it if a protocol attribute is set to
None in the subclass, see Python data-model for details.) [#PEP544]_

>>> from typing import Protocol
>>>
>>>
>>> class Message(Protocol):
...     recipient: str
...     body: str
>>>
>>>
>>> class Email:
...     sender: str
...     recipient: str
...     subject: str
...     body: str
>>>
>>>
>>> def send(message: Message):
...     ...
>>>
>>>
>>> email = Email()
>>> email.sender = 'mwatney@nasa.gov',
>>> email.recipient = 'mlewis@nasa.gov',
>>> email.subject = 'I am alive!'
>>> email.body = 'I survived the storm. I am alone on Mars.')
>>>
>>> send(email)  # will pass the checker


What Protocols are Not?
-----------------------
* At runtime, protocol classes is simple ABC
* No runtime type check
* Protocols are completely optional

At runtime, protocol classes will be simple ABCs. There is no intent to
provide sophisticated runtime instance and class checks against protocol
classes. This would be difficult and error-prone and will contradict the
logic of :pep:`484`. As well, following :pep:`484` and :pep:`526` Python
steering committee states that protocols are completely optional [#PEP544]_:

* No runtime semantics will be imposed for variables or parameters
  annotated with a protocol class.
* Any checks will be performed only by third-party type checkers and other
  tools.
* Programmers are free to not use them even if they use type annotations.
* There is no intent to make protocols non-optional in the future.


Covariance, Contravariance, Invariance
--------------------------------------
Covariance and contravariance are terms that refer to the ability to use a
more derived type (more specific) or a less derived type (less specific)
than originally specified. Generic type parameters support covariance and
contravariance to provide greater flexibility in assigning and using
generic types [#MicrosoftGenericsCovContra]_

In general, a covariant type parameter can be used as the return type of a
delegate, and contravariant type parameters can be used as parameter types.

>>> def echo(what: int):
...     print(what)

.. glossary::

    Covariance
        Enables you to use a more derived type than originally specified
        [#MicrosoftGenericsCovContra]_

        >>> check(True)  # True derives from int

    Contravariance
        Enables you to use a more generic (less derived) type than
        originally specified [#MicrosoftGenericsCovContra]_

        >>> check(object)  # int inherits from object

    Invariance
        Means that you can use only the type originally specified. An
        invariant generic type parameter is neither covariant nor
        contravariant [#MicrosoftGenericsCovContra]_

        >>> check(1)  # 1 is int


Default Value
-------------
>>> from typing import Protocol
>>>
>>>
>>> class Astronaut(Protocol):
...     firstname: str
...     lastname: str
...     job: str = 'astronaut'


Merging and extending protocols
-------------------------------
>>> from typing import Sized, Protocol
>>>
>>>
>>> class Closable(Protocol):
...     def close(self) -> None:
>>>         ...
>>>
>>> class SizableAndClosable(Sized, Closable, Protocol):
...     pass


Generic Protocols
-----------------
>>> from abc import abstractmethod
>>> from typing import Protocol
>>>
>>>
>>> class Iterable(Protocol[T]):
...     @abstractmethod
...     def __iter__(self) -> Iterator[T]:
...         ...


Recursive Protocols
-------------------
* Since 3.11 :pep:`673` –- Self Type
* Since 3.7 ``from __future__ import annotations``
* Future :pep:`563` -- Postponed Evaluation of Annotations

>>> from typing import Protocol
>>>
>>>
>>> class Tree(Protocol):
...     def get_node(self) -> Iterable['Tree']:
...         ...

>>> from typing import Protocol
>>>
>>>
>>> class Graph(Protocol):
...     def get_node(self) -> Iterable['Graph']:
...         ...


Unions
------
>>> from typing import Protocol
>>>
>>>
>>> class Exitable(Protocol):
...     def exit(self) -> int:
...         ...
>>>
>>> class Quittable(Protocol):
...     def quit(self) -> int | None:
...         ...
>>>
>>>
>>> def finish(task: Exitable | Quittable) -> None:
...     task.exit()
...     task.quit()


>>> from typing import Any, Protocol
>>>
>>>
>>> class ProtocolA(Protocol):
...     def meth(self, x: int) -> int: ...
>>>
>>>
>>> class ProtocolB(Protocol):
...     def meth(self, obj: Any, x: int) -> int: ...
>>>
>>>
>>> class C:
...     def meth(self, x: int) -> int: ...
>>>
>>>
>>> a: ProtocolA = C  # Error: Expected type 'ProtocolA', got 'Type[C]' instead
>>> b: ProtocolB = C  # OK


Modules as implementations of protocols
---------------------------------------
A module object is accepted where a protocol is expected if the public
interface of the given module is compatible with the expected protocol. For
example:

File ``config.py``:

>>> timeout = 100
>>> debug = True
>>> other_flag = False

File ``main.py``:

>>> import config
>>> from typing import Protocol
>>>
>>>
>>> class Config(Protocol):
...     timeout: int
...     debug: bool
...     other_flag: bool
>>>
>>>
>>> def setup(conf: Config) -> None:
...     ...
>>>
>>>
>>> setup(config)  # Passes type check


Callbacks
---------
File ``callbacks.py``:

>>> def on_error(x: int) -> None:
...     ...
>>>
>>> def on_success() -> None:
...     ...

File ``main.py``:

>>> import callbacks
>>> from typing import Protocol
>>>
>>>
>>> class Reporter(Protocol):
...     def on_error(self, x: int) -> None: ...
...     def on_success(self) -> None: ...
>>>
>>>
>>> result: Reporter = callbacks  # Passes type check


Runtime Checkable
-----------------
* By default ``isinstance()`` and ``issubclass()`` won't work with protocols
* You can use ``typing.runtime_checkable`` decorator to make it work

The default semantics is that ``isinstance()`` and ``issubclass()`` fail for
protocol types. This is in the spirit of duck typing -- protocols basically
would be used to model duck typing statically, not explicitly at runtime.

However, it should be possible for protocol types to implement custom instance
and class checks when this makes sense, similar to how ``Iterable`` and other
ABCs in ``collections.abc`` and ``typing`` already do it, but this is limited
to non-generic and unsubscripted generic protocols (``Iterable`` is statically
equivalent to ``Iterable[Any]``).

The typing module will define a special ``@runtime_checkable`` class decorator
that provides the same semantics for class and instance checks as for
``collections.abc`` classes, essentially making them 'runtime protocols':

>>> from typing import Protocol, runtime_checkable
>>>
>>>
>>> @runtime_checkable
... class Person(Protocol):
...     firstname: str
...     lastname: str
>>>
>>>
>>> class Astronaut:
...     firstname: str = 'Mark'
...     lastname: str = 'Watney'
...     job: str = 'astronaut'
>>>
>>> isinstance(Astronaut, Person)
True



>>> from typing import Protocol
>>>
>>>
>>> class Message(Protocol):
...     recipient: str
...     body: str
>>>
>>>
>>> class Email(Message):
...     sender: str
...     recipient: str
...     subject: str
...     body: str
>>>
>>> email = Email()
>>> isinstance(email, Message)
Traceback (most recent call last):
TypeError: Instance and class checks can only be used with @runtime_checkable protocols

>>> from typing import Protocol, runtime_checkable
>>>
>>>
>>> @runtime_checkable
... class Message(Protocol):
...     recipient: str
...     body: str
>>>
>>>
>>> class Email(Message):
...     sender: str
...     recipient: str
...     subject: str
...     body: str
>>>
>>> email = Email()
>>> isinstance(email, Message)
True


>>> from typing import Protocol, runtime_checkable
>>>
>>>
>>> @runtime_checkable
... class SupportsClose(Protocol):
...     def close(self): ...
>>>
>>>
>>> file = open('/tmp/myfile.txt')
>>> isinstance(file, SupportsClose)
True
>>> file.close()


Use Case - 0x01
---------------
>>> from typing import Protocol
>>>
>>>
>>> class SupportsClose(Protocol):
...     def close(self) -> None:
...         ...


Use Case - 0x02
---------------
>>> from abc import abstractmethod
>>> from typing import Protocol
>>>
>>>
>>> class RGB(Protocol):
...     rgb: Tuple[int, int, int]
...
...     @abstractmethod
...     def intensity(self) -> int:
...         return 0
>>>
>>>
>>> class Point(RGB):
...     def __init__(self, red: int, green: int, blue: float) -> None:
...         self.rgb = red, green, blue  # Error, 'blue' must be 'int'
...
...     # Type checker might warn that 'intensity' is not defined


Use Case - 0x03
---------------
File ``myview.py``

>>> def get(request):
...     ...
>>>
>>> def post(request):
...     ...
>>>
>>> def put(request):
...     ...
>>>
>>> def delete(request):
...     ...

File ``main.py``

>>> from typing import Protocol
>>> import myview
>>>
>>>
>>> class HttpView(Protocol):
...     def get(request): ...
...     def post(request): ...
...     def put(request): ...
...     def delete(request): ...
>>>
>>>
>>> view: HttpView = myview


References
----------
.. [#MicrosoftGenericsCovContra] https://docs.microsoft.com/en-us/dotnet/standard/generics/covariance-and-contravariance

.. [#PEP544] Levkivskyi, I. and Lehtosalo, J. and Langa, Ł. PEP 544 -- Protocols: Structural subtyping (static duck typing). Year: 2017. Retrieved: 2022-03-09. URL: https://www.python.org/dev/peps/pep-0544/
