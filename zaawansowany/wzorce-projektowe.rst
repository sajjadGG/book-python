*****************
Wzorce projektowe
*****************

Creational Design Patterns
==========================

* Abstract Factory Pattern

    * A Classic Abstract Factory
    * A More Pythonic Abstract Factory

* Builder Pattern
* Factory Method Pattern
* Prototype Pattern
* Singleton Pattern


Structural Design Patterns
==========================

* Adapter Pattern
* Bridge Pattern
* Composite Pattern

    * A Classic Composite/Noncomposite Hierarchy
    * A Single Class for (Non)Composites

* Decorator Pattern

    * Function and Method Decorators
    * Class Decorators

* Facade Pattern
* Flyweight Pattern
* Proxy Pattern

Behavioral Design Patterns
==========================

* Chain of Responsibility Pattern

    * A Conventional Chain
    * A Coroutine-based Chain

* Command Pattern
* Interpreter Pattern

    * Expression Evaluation with eval()
    * Code Evaluation with exec()
    * Code Evaluation using a Subprocess

* Iterator Pattern

    * Sequence Protocol Iterators
    * Two-argument iter() Function Iterators
    * Iterator Protocol Iterators

* Mediator Pattern

    * A Conventional Mediator
    * A Coroutine-based Mediator

* Memento Pattern
* Observer Pattern
* State Pattern

    * Using State-Sensitive Methods
    * Using State-Specific Methods

* Strategy Pattern
* Template Method Pattern
* Visitor Pattern


Przykłady praktyczne
====================

Gateway, Singleton, Factory
---------------------------

.. code-block:: python

    class HttpClientInterface:
        def GET(self):
            raise NotImplementedError

        def POST(self):
            raise NotImplementedError


    class GatewayLive(HttpClientInterface):
        def GET(self):
            # zaciagnij informacje o userze
            return ...

        def POST(self):
            # zapytaj po sieci
            pass


    class GatewayStub(HttpClientInterface):
        def GET(self):
            return {'imie': 'nazwisko'}


    class HttpClientFactory:
        instance = None

        def __init__(self):

            if HttpClientFactory.instance:
                HttpClientFactory.instance = GatewayStub

            return HttpClientFactory.instance


    client = HttpClientFactory()
    client.GET()


    client2 = HttpClientFactory()
    client2.GET()
    client2.POST()
