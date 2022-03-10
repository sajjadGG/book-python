AsyncIO Future
==============



Rationale
---------
* Low-level awaitable object
* Represents an eventual result of an asynchronous operation
* When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place
* Future objects in asyncio are needed to allow callback-based code to be used with async/await.
* Normally there is *no need* to create Future objects at the application level code.
