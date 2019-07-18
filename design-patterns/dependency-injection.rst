********************
Dependency injection
********************


- http://python-dependency-injector.ets-labs.org/introduction/di_in_python.html

Dependency injection, as a software design pattern, has number of advantages that are common for each language (including Python):

    - Dependency Injection decreases coupling between a class and its dependency.
    - Because dependency injection doesn’t require any change in code behavior it can be applied to legacy code as a refactoring. The result is clients that are more independent and that are easier to unit test in isolation using stubs or mock objects that simulate other objects not under test. This ease of testing is often the first benefit noticed when using dependency injection.
    - Dependency injection can be used to externalize a system’s configuration details into configuration files allowing the system to be reconfigured without recompilation (rebuilding). Separate configurations can be written for different situations that require different implementations of components. This includes, but is not limited to, testing.
    - Reduction of boilerplate code in the application objects since all work to initialize or set up dependencies is handled by a provider component.
    - Dependency injection allows a client to remove all knowledge of a concrete implementation that it needs to use. This helps isolate the client from the impact of design changes and defects. It promotes reusability, testability and maintainability.
    - Dependency injection allows a client the flexibility of being configurable. Only the client’s behavior is fixed. The client may act on anything that supports the intrinsic interface the client expects.

.. code-block:: python
    :caption: Dependency injection

    from dataclasses import dataclass
    from datetime import timedelta
    from typing import Optional, Any


    @dataclass
    class CacheInterface:
        expiration: timedelta = timedelta(days=30)
        location: Optional[str] = None

        def get(self, key: str) -> Any:
            raise NotImplementedError

        def set(self, key: str, value: Any) -> None:
            raise NotImplementedError

        def is_valid(self, key) -> bool:
            raise NotImplementedError


    class CacheFilesystem(CacheInterface):
        """Cache using files"""


    class CacheMemory(CacheInterface):
        """Cache using memory"""


    class CacheDatabase(CacheInterface):
        """Cache using database"""


    @dataclass
    class HTTP:
        _cache: CacheInterface

        def _fetch(self, url):
            return ...

        def get(self, url):
            if self._cache.is_valid(url):
                # Use cached data
                self._cache.get(url)
            else:
                data = self._fetch(url)
                self._cache.set(url, data)


    if __name__ == '__main__':
        database = CacheDatabase(location='sqlite3:///tmp/http-cache.sqlite3')
        filesystem = CacheFilesystem(location='/tmp/')
        memory = CacheMemory(expiration=timedelta(hours=2))

        http1 = HTTP(_cache=database)
        http1.get('http://python.astrotech.io')

        http2 = HTTP(_cache=filesystem)
        http2.get('http://python.astrotech.io')

        http3 = HTTP(_cache=memory)
        http3.get('http://python.astrotech.io')
