Microservice Database
=====================
* Polyglot Persistence
* Database per Service
* Shared database
* Database triggers


Polyglot Persistence
--------------------
* overhead związany z wielością usług
* nowe technologie
* różne działające równoległe wersje np. baz danych
* Deprecation policy
* Problem z backupem danych


Database per Service
--------------------
* Keep each microservice's persistent data private to that service and accessible only via its API.
* Wiele baz danych w jednej usłudze
* Mieszane, usługi mają jedną bazę danych

.. figure:: img/microservices-database-per-service.png

    Database per Service


Shared database
---------------
* Use a (single) database that is shared by multiple services. Each service freely accesses data owned by other services using local ACID transactions

.. figure:: img/microservices-database-shared.png

    Shared database


Database triggers
-----------------
* Reliably publish events whenever state changes by using database triggers. Each trigger inserts an event into an EVENTS table, which is polled by a separate process that publishes the events.
* Czy są ok?
* Czym się różni struct od Class
