Architecture
============


Stack
-----
* Starlette
* Pydantic
* Uvicorn


Starlette
---------
* ``Starlette`` is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.
* It is production-ready, and gives you the following:

    * Seriously impressive performance.
    * WebSocket support.
    * GraphQL support.
    * In-process background tasks.
    * Startup and shutdown events.
    * Test client built on requests.
    * CORS, GZip, Static Files, Streaming responses.
    * Session and Cookie support.
    * 100% test coverage.
    * 100% type annotated codebase.
    * Zero hard dependencies.

* Source: https://www.starlette.io


Uvicorn
-------
* ``Uvicorn`` is a lightning-fast ASGI server implementation, using ``uvloop`` and ``httptools``.
* Until recently Python has lacked a minimal low-level server/application interface for asyncio frameworks. The ASGI specification fills this gap, and means we're now able to start building a common set of tooling usable across all asyncio frameworks.
* ASGI should help enable an ecosystem of Python web frameworks that are highly competitive against Node and Go in terms of achieving high throughput in IO-bound contexts. It also provides support for HTTP/2 and WebSockets, which cannot be handled by WSGI.
* Uvicorn currently supports HTTP/1.1 and WebSockets. Support for HTTP/2 is planned.
* Source: https://www.uvicorn.org


Pydantic
--------
* Data validation and settings management using python type annotations.
* ``pydantic`` enforces type hints at runtime, and provides user friendly errors when data is invalid.
* Define how data should be in pure, canonical python; validate it with pydantic.
* So pydantic uses some cool new language features, but why should I actually go and use it?

    * There's no new schema definition micro-language to learn.
    * ``pydantic``'s BaseSettings class allows pydantic to be used in both a "validate this request data" context and in a "load my system settings" context
    * In benchmarks pydantic is faster than all other tested libraries
    * validate complex structures
    * ``pydantic`` allows custom data types to be defined or you can extend validation with methods on a model decorated with the validator decorator.
    * ``dataclasses`` integration

* Source: https://pydantic-docs.helpmanual.io


