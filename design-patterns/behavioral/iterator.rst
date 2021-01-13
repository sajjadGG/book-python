Iterator
========


Rationale
---------
* EN: Iterator
* PL: Iterator
* Type: object


Use Cases
---------
* History (like browser history)


Problem
-------
.. code-block:: python

    from dataclasses import dataclass, field


    @dataclass
    class BrowseHistory:
        _urls: list[str] = field(default_factory=list)

        def push(self, url: str) -> None:
            self._urls.append(url)

        def pop(self) -> str:
            self._urls.pop()

        def get_urls(self) -> list[str]:
            return self._urls


    if __name__ == '__main__':
        history = BrowseHistory()
        history.push(url='https://a.example.com')
        history.push(url='https://b.example.com')
        history.push(url='https://c.example.com')

        for i in range(len(history.get_urls())):
            url = history.get_urls()[i]
            print(i)


Design
------
.. figure:: ../_img/designpatterns-iterator-usecase.png


Implementation
--------------
.. literalinclude:: ../_src/designpatterns-iterator.py
    :language: python


Assignments
-----------
.. todo:: Create assignments
