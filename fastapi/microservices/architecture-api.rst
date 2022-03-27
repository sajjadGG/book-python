Microservice API
================
* Wersjonowane
* Stabilne
* Deprecation policy
* HTTP, REST, JSON
* BFF, API Gateway
* GraphQL


API gateway
-----------
* Implement an API gateway that is the single entry point for all clients. The API gateway handles requests in one of two ways. Some requests are simply proxied/routed to the appropriate service. It handles other requests by fanning out to multiple services.
* Rather than provide a one-size-fits-all style API, the API gateway can expose a different API for each client. For example, the Netflix API gateway runs client-specific adapter code that provides each client with an API that's best suited to it's requirements.
* The API gateway might also implement security, e.g. verify that the client is authorized to perform the request
* Netflix API gateway, Zuur

Microservices API gateway:

.. figure:: img/microservices-api-gateway.jpg


BFF Model
---------


BFF + API Gateway
-----------------


GraphQL
-------


Historie
--------
* przykład stabilności webapi i mobilnych stron
* wersjonowanie w nagłówkach HTTP i q=...
* POST, PUT, PATCH, GET, DELETE


Further Reading
---------------
* http://allegro.tech/2015/01/Content-headers-or-how-to-version-api.html
