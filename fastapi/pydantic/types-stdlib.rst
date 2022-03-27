Pydantic Types Stdlib
=====================

Where possible *pydantic* uses `standard library
types <#standard-library-types>`_ to define fields, thus smoothing the
learning curve. For many useful applications, however, no standard
library type exists, so *pydantic* implements `many commonly used
types <#pydantic-types>`_.


Standard Library Types
----------------------
*pydantic* supports many common types from the python standard library.
If you need stricter processing see `Strict Types <#strict-types>`_; if
you need to constrain the values allowed (e.g. to require a positive
int) see `Constrained Types <#constrained-types>`_.

``None``, ``type(None)`` or ``Literal[None]`` (equivalent according to `PEP 484 <https://www.python.org/dev/peps/pep-0484/#using-none>`_)
   allows only ``None`` value

``bool``
   see `Booleans <#booleans>`_ below for details on how bools are
   validated and what values are permitted

``int``
   *pydantic* uses ``int(v)`` to coerce types to an ``int``; see
   `models#data-conversion`_ warning on loss of information
   during data conversion

``float``
   similarly, ``float(v)`` is used to coerce values to floats

``str``
   strings are accepted as-is, ``int`` ``float`` and ``Decimal`` are
   coerced using ``str(v)``, ``bytes`` and ``bytearray`` are converted
   using ``v.decode()``, enums inheriting from ``str`` are converted
   using ``v.value``, and all other types cause an error

``bytes``
   ``bytes`` are accepted as-is, ``bytearray`` is converted using
   ``bytes(v)``, ``str`` are converted using ``v.encode()``, and
   ``int``, ``float``, and ``Decimal`` are coerced using
   ``str(v).encode()``

``list``
   allows ``list``, ``tuple``, ``set``, ``frozenset``, ``deque``, or
   generators and casts to a list; see ``typing.List`` below for
   sub-type constraints

``tuple``
   allows ``list``, ``tuple``, ``set``, ``frozenset``, ``deque``, or
   generators and casts to a tuple; see ``typing.Tuple`` below for
   sub-type constraints

``dict``
   ``dict(v)`` is used to attempt to convert a dictionary; see
   ``typing.Dict`` below for sub-type constraints

``set``
   allows ``list``, ``tuple``, ``set``, ``frozenset``, ``deque``, or
   generators and casts to a set; see ``typing.Set`` below for sub-type
   constraints

``frozenset``
   allows ``list``, ``tuple``, ``set``, ``frozenset``, ``deque``, or
   generators and casts to a frozen set; see ``typing.FrozenSet`` below
   for sub-type constraints

``deque``
   allows ``list``, ``tuple``, ``set``, ``frozenset``, ``deque``, or
   generators and casts to a deque; see ``typing.Deque`` below for
   sub-type constraints

``datetime.date``
   see `Datetime Types <#datetime-types>`_ below for more detail on
   parsing and validation

``datetime.time``
   see `Datetime Types <#datetime-types>`_ below for more detail on
   parsing and validation

``datetime.datetime``
   see `Datetime Types <#datetime-types>`_ below for more detail on
   parsing and validation

``datetime.timedelta``
   see `Datetime Types <#datetime-types>`_ below for more detail on
   parsing and validation

``typing.Any``
   allows any value including ``None``, thus an ``Any`` field is
   optional

``typing.Annotated``
   allows wrapping another type with arbitrary metadata, as per
   `PEP-593 <https://www.python.org/dev/peps/pep-0593/>`_. The
   ``Annotated`` hint may contain a single call to the ```Field``
   function <schema-typingannotated-fields>`_, but otherwise the
   additional metadata is ignored and the root type is used.

``typing.TypeVar``
   constrains the values allowed based on ``constraints`` or ``bound``,
   see `TypeVar <#typevar>`_

``typing.Union``
   see `Unions <#unions>`_ below for more detail on parsing and
   validation

``typing.Optional``
   ``Optional[x]`` is simply short hand for ``Union[x, None]``; see
   `Unions <#unions>`_ below for more detail on parsing and validation
   and `Required Fields <models-required-fields>`_ for details about
   required fields that can receive ``None`` as a value.

``typing.List``
   see `Typing Iterables <#typing-iterables>`_ below for more detail on
   parsing and validation

``typing.Tuple``
   see `Typing Iterables <#typing-iterables>`_ below for more detail on
   parsing and validation

``subclass of typing.NamedTuple``
   Same as ``tuple`` but instantiates with the given namedtuple and
   validates fields since they are annotated. See `Annotated
   Types <#annotated-types>`_ below for more detail on parsing and
   validation

``subclass of collections.namedtuple``
   Same as ``subclass of typing.NamedTuple`` but all fields will have
   type ``Any`` since they are not annotated

``typing.Dict``
   see `Typing Iterables <#typing-iterables>`_ below for more detail on
   parsing and validation

``subclass of typing.TypedDict``
   Same as ``dict`` but *pydantic* will validate the dictionary since
   keys are annotated. See `Annotated Types <#annotated-types>`_ below
   for more detail on parsing and validation

``typing.Set``
   see `Typing Iterables <#typing-iterables>`_ below for more detail on
   parsing and validation

``typing.FrozenSet``
   see `Typing Iterables <#typing-iterables>`_ below for more detail on
   parsing and validation

``typing.Deque``
   see `Typing Iterables <#typing-iterables>`_ below for more detail on
   parsing and validation

``typing.Sequence``
   see `Typing Iterables <#typing-iterables>`_ below for more detail on
   parsing and validation

``typing.Iterable``
   this is reserved for iterables that shouldn't be consumed. See
   `Infinite Generators <#infinite-generators>`_ below for more detail
   on parsing and validation

``typing.Type``
   see `Type <#type>`_ below for more detail on parsing and validation

``typing.Callable``
   see `Callable <#callable>`_ below for more detail on parsing and
   validation

``typing.Pattern``
   will cause the input value to be passed to ``re.compile(v)`` to
   create a regex pattern

``ipaddress.IPv4Address``
   simply uses the type itself for validation by passing the value to
   ``IPv4Address(v)``; see `Pydantic Types <#pydantic-types>`_ for
   other custom IP address types

``ipaddress.IPv4Interface``
   simply uses the type itself for validation by passing the value to
   ``IPv4Address(v)``; see `Pydantic Types <#pydantic-types>`_ for
   other custom IP address types

``ipaddress.IPv4Network``
   simply uses the type itself for validation by passing the value to
   ``IPv4Network(v)``; see `Pydantic Types <#pydantic-types>`_ for
   other custom IP address types

``ipaddress.IPv6Address``
   simply uses the type itself for validation by passing the value to
   ``IPv6Address(v)``; see `Pydantic Types <#pydantic-types>`_ for
   other custom IP address types

``ipaddress.IPv6Interface``
   simply uses the type itself for validation by passing the value to
   ``IPv6Interface(v)``; see `Pydantic Types <#pydantic-types>`_ for
   other custom IP address types

``ipaddress.IPv6Network``
   simply uses the type itself for validation by passing the value to
   ``IPv6Network(v)``; see `Pydantic Types <#pydantic-types>`_ for
   other custom IP address types

``enum.Enum``
   checks that the value is a valid Enum instance

``subclass of enum.Enum``
   checks that the value is a valid member of the enum; see `Enums and
   Choices <#enums-and-choices>`_ for more details

``enum.IntEnum``
   checks that the value is a valid IntEnum instance

``subclass of enum.IntEnum``
   checks that the value is a valid member of the integer enum; see
   `Enums and Choices <#enums-and-choices>`_ for more details

``decimal.Decimal``
   *pydantic* attempts to convert the value to a string, then passes the
   string to ``Decimal(v)``

``pathlib.Path``
   simply uses the type itself for validation by passing the value to
   ``Path(v)``; see `Pydantic Types <#pydantic-types>`_ for other more
   strict path types

``uuid.UUID``
   strings and bytes (converted to strings) are passed to ``UUID(v)``,
   with a fallback to ``UUID(bytes=v)`` for ``bytes`` and ``bytearray``;
   see `Pydantic Types <#pydantic-types>`_ for other stricter UUID
   types

``ByteSize``
   converts a bytes string with units to bytes



Datetime Types
--------------
* ``datetime`` fields
* ``date`` fields
* ``time`` fields
* ``timedelta`` fields
* https://docs.python.org/library/datetime.html#available-types

*Pydantic* supports the following datetime types

* ``datetime`` fields can be:

  * ``datetime``, existing ``datetime`` object
  * ``int`` or ``float``, assumed as Unix time, i.e. seconds (if >= ``-2e10`` or <= ``2e10``) or milliseconds (if < ``-2e10``or > ``2e10``) since 1 January 1970
  * ``str``, following formats work:

    * ``YYYY-MM-DD[T]HH:MM[:SS[.ffffff]][Z or [±]HH[:]MM]]]``
    * ``int`` or ``float`` as a string (assumed as Unix time)

* ``date`` fields can be:

  * ``date``, existing ``date`` object
  * ``int`` or ``float``, see ``datetime``
  * ``str``, following formats work:

    * ``YYYY-MM-DD``
    * ``int`` or ``float``, see ``datetime``

* ``time`` fields can be:

  * ``time``, existing ``time`` object
  * ``str``, following formats work:

    * ``HH:MM[:SS[.ffffff]][Z or [±]HH[:]MM]]]``

* ``timedelta`` fields can be:

  * ``timedelta``, existing ``timedelta`` object
  * ``int`` or ``float``, assumed as seconds
  * ``str``, following formats work:

    * ``[-][DD ][HH:MM]SS[.ffffff]``
    * ``[±]P[DD]DT[HH]H[MM]M[SS]S`` (ISO 8601 format for timedelta)


Booleans
--------
A standard ``bool`` field will raise a ``ValidationError`` if the value is
not one of the following:

* A valid boolean (i.e. ``True`` or ``False``),
* The integers ``0`` or ``1``,
* a ``str`` which when converted to lower case is one of
  ``'0', 'off', 'f', 'false', 'n', 'no', '1', 'on', 't', 'true', 'y', 'yes'``
* a ``bytes`` which is valid (per the previous rule) when decoded to ``str``

If you want stricter boolean logic (e.g. a field which only permits ``True`` and ``False``) you can
use ```StrictBool`` <#strict-types>`_.

Here is a script demonstrating some of these behaviors:


Callable
--------
Fields can also be of type ``Callable``:

Callable fields only perform a simple check that the argument is
callable; no validation of arguments, their types, or the return
type is performed.


Type
----
*pydantic* supports the use of ``Type[T]`` to specify that a field may only
accept classes (not instances) that are subclasses of ``T``.

You may also use ``Type`` to specify that any class is allowed.


TypeVar
-------
``TypeVar`` is supported either unconstrained, constrained or with a bound.


Literal Type
------------
*pydantic* supports the use of ``typing.Literal`` as a lightweight way to
specify that a field may accept only specific literal values:

One benefit of this field type is that it can be used to check for equality
with one or more specific values without needing to declare custom validators:

With proper ordering in an annotated ``Union``, you can use this to parse
types of decreasing specificity:


Annotated Types
---------------


NamedTuple
----------


TypedDict
---------


Typing Iterables
----------------
*pydantic* uses standard library ``typing`` types as defined in PEP 484
to define complex objects.


Infinite Generators
-------------------
If you have a generator you can use ``Sequence`` as described above. In
that case, the generator will be consumed and stored on the model as a
list and its values will be validated with the sub-type of ``Sequence``
(e.g. ``int`` in ``Sequence[int]``).

But if you have a generator that you don't want to be consumed, e.g. an
infinite generator or a remote data loader, you can define its type with
``Iterable``:

Warning ``Iterable`` fields only perform a simple check that the
argument is iterable and won't be consumed. No validation of their values is performed as it cannot be done without consuming the iterable.

If you want to validate the values of an infinite generator you
can create a separate model and use it while consuming the generator,
reporting the validation errors as appropriate.

pydantic can't validate the values automatically for you because it would require consuming the infinite generator.


Validating the first value
--------------------------
You can create a `validator <validators>`_ to validate the first
value in an infinite generator and still not consume it entirely.


Unions
------
The ``Union`` type allows a model attribute to accept different types,
e.g.:

You may get unexpected coercion with ``Union``; see below. Know
that you can also make the check slower but stricter by using `Smart
Union <model_config-smart-union>`_

However, as can be seen above, *pydantic* will attempt to 'match' any of
the types defined under ``Union`` and will use the first one that
matches. In the above example the ``id`` of ``user_03`` was defined as a
``uuid.UUID`` class (which is defined under the attribute's ``Union``
annotation) but as the ``uuid.UUID`` can be marshalled into an ``int``
it chose to match against the ``int`` type and disregarded the other
types.

``typing.Union`` also ignores order when
`defined <https://docs.python.org/3/library/typing.html#typing.Union>`_,
so ``Union[int, float] == Union[float, int]`` which can lead to
unexpected behaviour when combined with matching based on the ``Union``
type order inside other type definitions, such as ``List`` and ``Dict``
types (because python treats these definitions as singletons). For
example,
``Dict[str, Union[int, float]] == Dict[str, Union[float, int]]`` with
the order based on the first time it was defined. Please note that this
can also be `affected by third party
libraries <https://github.com/samuelcolvin/pydantic/issues/2835>`_ and
their internal type definitions and the import orders.

As such, it is recommended that, when defining ``Union`` annotations,
the most specific type is included first and followed by less specific
types.

In the above example, the ``UUID`` class should precede the ``int`` and
``str`` classes to preclude the unexpected representation as such:

The type ``Optional[x]`` is a shorthand for ``Union[x, None]``.

`Optional[x]` can also be used to specify a required field that can take `None` as a value.

See more details in `Required Fields`


Discriminated Unions (a.k.a. Tagged Unions)
-------------------------------------------
When ``Union`` is used with multiple submodels, you sometimes know
exactly which submodel needs to be checked and validated and want to
enforce this. To do that you can set the same field - let's call it
``my_discriminator`` - in each of the submodels with a discriminated
value, which is one (or many) ``Literal`` value(s). For your ``Union``,
you can set the discriminator in its value:
``Field(discriminator='my_discriminator')``.

Setting a discriminated union has many benefits:

* validation is faster since it is only attempted against one model
* only one explicit error is raised in case of failure
* the generated JSON schema implements the `associated OpenAPI
   specification <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#discriminatorObject>`_

Using the `Annotated Fields
syntax <../schema/#typingannotated-fields>`_ can be handy to regroup
the ``Union`` and ``discriminator`` information. See below for an
example!


Nested Discriminated Unions
---------------------------
Only one discriminator can be set for a field but sometimes you want to
combine multiple discriminators. In this case you can always create
"intermediate" models with ``_root__`` and add your discriminator.


Enums and Choices
-----------------
*pydantic* uses python's standard ``enum`` classes to define choices.


Generic Classes as Types
-------------------------------
This is an advanced technique that you might not need in the
beginning. In most of the cases you will probably be fine with standard
*pydantic* models.

You can use `Generic
Classes <https://docs.python.org/3/library/typing.html#typing.Generic>`_
as field types and perform custom validation based on the "type
parameters" (or sub-types) with ``_get_validators__``.

If the Generic class that you are using as a sub-type has a classmethod
``_get_validators__`` you don't need to use ``arbitrary_types_allowed``
for it to work.

Because you can declare validators that receive the current ``field``,
you can extract the ``sub_fields`` (from the generic class type
parameters) and validate data with them.
