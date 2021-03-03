Introduction
============


Rationale
---------
* Automatic documentation (Swagger, Redoc)
* Uses Python type annotation
* IDE autocomplete (through type annotation)
* Fast
* Based on open standards: JSON Schema, Open API
* Security and authentication

    * HTTP Basic
    * OAuth2 (also with JWT tokens)
    * API keys in Headers, Query parameters, Cookies, etc.

* Dependency Injection
* Unlimited "plugins"
* Testing
* Starlette features:

    * Websocket support
    * GrafQL support
    * In-process background tasks
    * Startup and shutdown events
    * Test client built on requests
    * CORS, GZip, Static Files, Streaming responses
    * Sessions and Cookies support

* Suport for databases:

    * SQL Database
    * NoSQL Database
    * GraphQL

Source: [#fastapicourse]_


Key Features
------------
* Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
* Fast to code: Increase the speed to develop features by about 200% to 300%. *
* Fewer bugs: Reduce about 40% of human (developer) induced errors. *
* Intuitive: Great editor support. Completion everywhere. Less time debugging.
* Easy: Designed to be easy to use and learn. Less time reading docs.
* Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* Robust: Get production-ready code. With automatic interactive documentation.
* Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

Source: [#fastapidoc]_


Used by
-------
* Microsoft in Windows and Office
* Netflix in Dispatch (crisis management)


Table of Contents
-----------------
* Source: [#fastapicourse]_

1. Getting Started

    * Install and Setup
    * Break it down, how it structured

2. Basic concepts

    * Path parameters
    * API Doc - swagger / redoc
    * Query parameters
    * Request body

3. Intermediate concepts

    * Debugging FastAPI
    * Pydantic schemas
    * SQLAlchemy database connections
    * Models and tables

4. Database tasks

    * Insert data to database
    * Select data from database
    * Delete
    * Update
    * Relationships: fk, m2m

5. Responses

    * Handling exceptions
    * Return response
    * Define response model

6. User and Password

    * Create user
    * Hash user password
    * Show single user
    * Define docs tags

7. API Router

    * API Router
    * API Router with parameters

8. Authentication using JWT

    * Create Login route
    * Login and verify password
    * Return JSON Web Token (JWT) access token
    * Routes behind authentication

9. Deploy

    * Deployment


Further Reading
---------------
* https://github.com/tiangolo/fastapi
* https://fastapi.tiangolo.com
* https://pydantic-docs.helpmanual.io
* https://swagger.io
* https://petstore.swagger.io
* https://www.uvicorn.org
* https://www.starlette.io


References
----------
.. [#fastapidoc] Sebastián Ramírez. FastAPI official documentation. Accessed Date: 2021-02-21. URL: https://fastapi.tiangolo.com
.. [#fastapigithub] Sebastián Ramírez. FastAPI Github repository. Accessed Date: 2021-02-21. URL: https://github.com/tiangolo/fastapi
.. [#fastapicourse] Bitfumes. FastAPI - A python framework full course. Accessed Date: 2021-02-21. URL: https://www.youtube.com/watch?v=7t2alSnE2-I
