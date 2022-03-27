Pydantic Types Custom
=====================
* ``FilePath`` - like ``Path``, but the path must exist and be a file
* ``DirectoryPath`` - like ``Path``, but the path must exist and be a directory
* ``PastDate`` - like ``date``, but the date should be in the past
* ``FutureDate`` - like ``date``, but the date should be in the future
* ``EmailStr`` - the input string must be a valid email address, and the output is a simple string
* ``NameEmail`` - the input string must be either a valid email address or in the format ``Fred Bloggs <fred.bloggs@example.com>``, and the output is a ``NameEmail`` object which has two properties: ``name`` and ``email``.
* ``PyObject`` - expects a string and loads the python object importable at that dotted path; e.g. if ``'math.cos'`` was provided, the resulting field value would be the function ``cos``
* ``Color`` - for parsing HTML and CSS colors
* ``Json`` - a special type wrapper which loads JSON before parsing
* ``PaymentCardNumber`` - for parsing and validating payment cards
* ``AnyUrl`` - any URL
* ``AnyHttpUrl`` - an HTTP URL
* ``HttpUrl`` - a stricter HTTP URL
* ``FileUrl`` - a file path URL
* ``PostgresDsn`` - a postgres DSN style URL
* ``RabbitMqDsn`` - an ``AMQP`` DSN style URL as used by RabbitMQ, StormMQ, ActiveMQ etc.
* ``RedisDsn`` - a redis DSN style URL
* ``stricturl`` - a type method for arbitrary URL constraints
* ``UUID1`` - requires a valid UUID of type 1
* ``UUID3`` - requires a valid UUID of type 3
* ``UUID4`` - requires a valid UUID of type 4
* ``UUID5`` - requires a valid UUID of type 5
* ``SecretBytes`` - bytes where the value is kept partially secret
* ``SecretStr`` - string where the value is kept partially secret
* ``IPvAnyAddress`` - allows either an ``IPv4Address`` or an ``IPv6Address``
* ``IPvAnyInterface`` - allows either an ``IPv4Interface`` or an ``IPv6Interface``
* ``IPvAnyNetwork`` - allows either an ``IPv4Network`` or an ``IPv6Network``
* ``NegativeFloat`` - allows a float which is negative; uses standard ``float`` parsing then checks the value is less than 0
* ``NegativeInt`` - allows an int which is negative; uses standard ``int`` parsing then checks the value is less than 0
* ``PositiveFloat`` - allows a float which is positive; uses standard ``float`` parsing then checks the value is greater than 0
* ``PositiveInt`` - allows an int which is positive; uses standard ``int`` parsing then checks the value is greater than 0

If no existing type suits your purpose you can also implement your `own
pydantic-compatible types <#custom-data-types>`_ with custom properties
and validation.


Email Types
-----------
``EmailStr``
    requires `email-validator <https://github.com/JoshData/python-email-validator>`_ to be installed;
    the input string must be a valid email address, and the output is a simple string

``NameEmail``
    requires `email-validator <https://github.com/JoshData/python-email-validator>`_ to be installed;
    the input string must be either a valid email address or in the format ``Fred Bloggs <fred.bloggs@example.com>``,
    and the output is a ``NameEmail`` object which has two properties: ``name`` and ``email``.
    For ``Fred Bloggs <fred.bloggs@example.com>`` the name would be ``"Fred Bloggs"``;
    for ``fred.bloggs@example.com`` it would be ``"fred.bloggs"``.


URL Fields
----------
For URI/URL validation the following types are available:

* ``AnyUrl``: any scheme allowed, TLD not required, host required
* ``AnyHttpUrl``: scheme ``http`` or ``https``, TLD not required, host required
* ``HttpUrl``: scheme ``http`` or ``https``, TLD required, host required, max length 2083
* ``FileUrl``: scheme ``file``, host not required
* ``PostgresDsn``: scheme ``postgres``, ``postgresql``, user info required, TLD not required, host required. Also, its supported DBAPI dialects:

  - ``postgresql+asyncpg``
  - ``postgresql+pg8000``
  - ``postgresql+psycopg2``
  - ``postgresql+psycopg2cffi``
  - ``postgresql+py-postgresql``
  - ``postgresql+pygresql``

* ``AmqpDsn``: schema ``amqp`` or ``amqps``, user info not required, TLD not required, host not required
* ``RedisDsn``: scheme ``redis`` or ``rediss``, user info not required, tld not required, host not required (CHANGED: user info
  not required from **v1.6** onwards), user info may be passed without user part (e.g., ``rediss://:pass@localhost``)
* ``stricturl``: method with the following keyword arguments:

    - ``strip_whitespace: bool = True``
    - ``min_length: int = 1``
    - ``max_length: int = 2 ** 16``
    - ``tld_required: bool = True``
    - ``host_required: bool = True``
    - ``allowed_schemes: Optional[Set[str]] = None``

The above types (which all inherit from ``AnyUrl``) will attempt to give descriptive errors when invalid URLs are
provided:

If you require a custom URI/URL type, it can be created in a similar way to the types defined above.


URL Properties
--------------
Assuming an input URL of ``http://samuel:pass@example.com:8000/the/path/?query=here#fragment=is;this=bit``,
the above types export the following properties:

* ``scheme``: always set - the url scheme (``http`` above)
* ``host``: always set - the url host (``example.com`` above)
* ``host_type``: always set - describes the type of host, either:

  * ``domain``: e.g. ``example.com``,
  * ``int_domain``: international domain, see `international-domains>`_, e.g. ``exampl£e.org``,
  * ``ipv4``: an IP V4 address, e.g. ``127.0.0.1``, or
  * ``ipv6``: an IP V6 address, e.g. ``2001:db8:ff00:42``

* ``user``: optional - the username if included (``samuel`` above)
* ``password``: optional - the password if included (``pass`` above)
* ``tld``: optional - the top level domain (``com`` above),
  **Note: this will be wrong for any two-level domain, e.g. "co.uk".** You'll need to implement your own list of TLDs
  if you require full TLD validation
* ``port``: optional - the port (``8000`` above)
* ``path``: optional - the path (``/the/path/`` above)
* ``query``: optional - the URL query (aka GET arguments or "search string") (``query=here`` above)
* ``fragment``: optional - the fragment (``fragment=is;this=bit`` above)

If further validation is required, these properties can be used by validators to enforce specific behaviour:

International Domains
---------------------
"International domains" (e.g. a URL where the host or TLD includes non-ascii characters) will be encoded via
`punycode <https://en.wikipedia.org/wiki/Punycode>`_ (see
`this article <https://www.xudongz.com/blog/2017/idn-phishing/>`_ for a good description of why this is important):

.. warning:: Underscores in Hostnames
             In *pydantic* underscores are allowed in all parts of a domain except the tld.
             Technically this might be wrong - in theory the hostname cannot have underscores, but subdomains can.

             To explain this; consider the following two cases:

             * ``exam_ple.co.uk``: the hostname is ``exam_ple``, which should not be allowed since it contains an underscore
             * ``foo_bar.example.com`` the hostname is ``example``, which should be allowed since the underscore is in the subdomain

             Without having an exhaustive list of TLDs, it would be impossible to differentiate between these two. Therefore
             underscores are allowed, but you can always do further validation in a validator if desired.

             Also, Chrome, Firefox, and Safari all currently accept ``http://exam_ple.com`` as a URL, so we're in good
             (or at least big) company.


Color Type
----------
You can use the ``Color`` data type for storing colors as per
`CSS3 specification <http://www.w3.org/TR/css3-color/#svg-color>`_. Colors can be defined via:

* `name <http://www.w3.org/TR/SVG11/types.html#ColorKeywords>`_ (e.g. ``"Black"``, ``"azure"``)
* `hexadecimal value <https://en.wikipedia.org/wiki/Web_colors#Hex_triplet>`_
  (e.g. ``"0x000"``, ``"#FFFFFF"``, ``"7fffd4"``)
* RGB/RGBA tuples (e.g. ``(255, 255, 255)``, ``(255, 255, 255, 0.5)``)
* `RGB/RGBA strings <https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#RGB_colors>`_
  (e.g. ``"rgb(255, 255, 255)"``, ``"rgba(255, 255, 255, 0.5)"``)
* `HSL strings <https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#HSL_colors>`_
  (e.g. ``"hsl(270, 60%, 70%)"``, ``"hsl(270, 60%, 70%, .5)"``)

``Color`` has the following methods:

``original``
    the original string or tuple passed to ``Color``

``as_named``
    returns a named CSS3 color; fails if the alpha channel is set or no such color exists unless
  ``fallback=True`` is supplied, in which case it falls back to ``as_hex``

``as_hex``
    returns a string in the format ``#fff`` or ``#ffffff``; will contain 4 (or 8) hex values if the alpha channel is set,
  e.g. ``#7f33cc26``

``as_rgb``
    returns a string in the format ``rgb(<red>, <green>, <blue>)``, or ``rgba(<red>, <green>, <blue>, <alpha>)``
  if the alpha channel is set

``as_rgb_tuple``
    returns a 3- or 4-tuple in RGB(a) format. The ``alpha`` keyword argument can be used to define whether
    the alpha channel should be included;
    options: ``True`` - always include, ``False`` - never include, ``None`` (default) - include if set

``as_hsl``
    string in the format ``hsl(<hue deg>, <saturation %>, <lightness %>)``
  or ``hsl(<hue deg>, <saturation %>, <lightness %>, <alpha>)`` if the alpha channel is set

``as_hsl_tuple``
    returns a 3- or 4-tuple in HSL(a) format. The ``alpha`` keyword argument can be used to define whether
    the alpha channel should be included;
    options: ``True`` - always include, ``False`` - never include, ``None`` (the default)  - include if set

The ``__str__`` method for ``Color`` returns ``self.as_named(fallback=True)``.

.. note:: the ``as_hsl*`` refer to hue, saturation, lightness "HSL" as used
          in html and most of the world, **not** "HLS" as used in python's
          ``colorsys``.

Secret Types
------------
You can use the ``SecretStr`` and the ``SecretBytes`` data types for storing sensitive information
that you do not want to be visible in logging or tracebacks.
``SecretStr`` and ``SecretBytes`` can be initialized idempotently or by using ``str`` or ``bytes`` literals respectively.
The ``SecretStr`` and ``SecretBytes`` will be formatted as either ``'**********'`` or ``''`` on conversion to json.


Json Type
---------
You can use ``Json`` data type to make *pydantic* first load a raw JSON string.
It can also optionally be used to parse the loaded object into another type base on
the type ``Json`` is parameterised with:


Payment Card Numbers
--------------------
The ``PaymentCardNumber`` type validates `payment cards <https://en.wikipedia.org/wiki/Payment_card>`_
(such as a debit or credit card).

``PaymentCardBrand`` can be one of the following based on the BIN:

* ``PaymentCardBrand.amex``
* ``PaymentCardBrand.mastercard``
* ``PaymentCardBrand.visa``
* ``PaymentCardBrand.other``

The actual validation verifies the card number is:

* a ``str`` of only digits
* `luhn <https://en.wikipedia.org/wiki/Luhn_algorithm>`_ valid
* the correct length based on the BIN, if Amex, Mastercard or Visa, and between
  12 and 19 digits for all other brands


Strict Types
------------
You can use the ``StrictStr``, ``StrictBytes``, ``StrictInt``,
``StrictFloat``, and ``StrictBool`` types to prevent coercion from
compatible types. These types will only pass validation when the
validated value is of the respective type or is a subtype of that type.
This behavior is also exposed via the ``strict`` field of the
``ConstrainedStr``, ``ConstrainedBytes``, ``ConstrainedFloat`` and
``ConstrainedInt`` classes and can be combined with a multitude of
complex validation rules.

The following caveats apply:

-  ``StrictBytes`` (and the ``strict`` option of ``ConstrainedBytes``)
   will accept both ``bytes``, and ``bytearray`` types.
-  ``StrictInt`` (and the ``strict`` option of ``ConstrainedInt``) will
   not accept ``bool`` types, even though ``bool`` is a subclass of
   ``int`` in Python. Other subclasses will work.
-  ``StrictFloat`` (and the ``strict`` option of ``ConstrainedFloat``)
   will not accept ``int``.


ByteSize
--------
You can use the ``ByteSize`` data type to convert byte string
representation to raw bytes and print out human readable versions of the
bytes as well.

Note that ``1b`` will be parsed as "1 byte" and not "1 bit".


Custom Data Types
-----------------
You can also define your own custom data types. There are several ways
to achieve it.


Classes with ``_get_validators__``
-------------------------------
You use a custom class with a classmethod ``_get_validators__``. It
will be called to get validators to parse and validate the input data.

These validators have the same semantics as in
`Validators`_, you can declare a parameter ``config``,
``field``, etc.

Similar validation could be achieved using
```constr(regex=...)`` <#constrained-types>`_ except the value won't be
formatted with a space, the schema would just include the full pattern
and the returned value would be a vanilla string.

See `schema`_ for more details on how the model's schema is
generated.


Arbitrary Types Allowed
-----------------------
You can allow arbitrary types using the ``arbitrary_types_allowed``
config in the `Model Config`_.
