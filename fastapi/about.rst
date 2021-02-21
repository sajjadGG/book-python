About
=====


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

Source: [fastapicourse]_


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

Source: [fastapidoc]_


Further Reading
---------------
* https://github.com/tiangolo/fastapi
* https://fastapi.tiangolo.com
* https://pydantic-docs.helpmanual.io
* https://swagger.io
* https://petstore.swagger.io


Getting Started
---------------
* Install and Setup
* Break it down, how it structured


Basic concepts
--------------
* Path parameters
* API Doc - swagger / redoc
* Query parameters
* Request body


Intermediate concepts
---------------------
* Debugging FastAPI
* Pydantic schemas
* SQLAlchemy database connections
* Models and tables


Database tasks
--------------
* Insert data to database
* Select data from database
* Delete
* Update
* Relationships: fk, m2m


Responses
---------
* Handling exceptions
* Return response
* Define response model


User and Password
-----------------
* Create user
* Hash user password
* Show single user
* Define docs tags


API Router
----------
* API Router
* API Router with parameters


Authentication using JWT
------------------------
* Create Login route
* Login and verify password
* Return JSON Web Token (JWT) access token
* Routes behind authentication


Deploy
------
* Deployment


References
----------
.. [fastapidoc] Sebastián Ramírez. FastAPI. Accessed Date: 2021-02-21. URL: https://fastapi.tiangolo.com
.. [fastapigithub] Sebastián Ramírez. FastAPI. Accessed Date: 2021-02-21. URL: https://github.com/tiangolo/fastapi
.. [fastapicourse] Bitfumes. FastAPI - A python framework | Full Course. Accessed Date: 2021-02-21. URL: https://www.youtube.com/watch?v=7t2alSnE2-I
