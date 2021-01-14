from dataclasses import dataclass, field


class Iterator:
    def has_next(self) -> bool:
        raise NotImplementedError

    def current(self) -> str:
        raise NotImplementedError

    def next(self) -> None:
        raise NotImplementedError


@dataclass
class BrowseHistory:
    _urls: list[str] = field(default_factory=list)

    def push(self, url: str) -> None:
        self._urls.append(url)

    def pop(self) -> str:
        self._urls.pop()

    def get_urls(self) -> list[str]:
        return self._urls

    def create_iterator(self) -> Iterator:
        return self.ListIterator(self)

    @dataclass
    class ListIterator(Iterator):
        __history: 'BrowseHistory'
        __index: int = 0

        def has_next(self) -> bool:
            return self.__index < len(history._urls)

        def current(self) -> str:
            return history._urls[self.__index]

        def next(self) -> None:
            self.__index += 1


if __name__ == '__main__':
    history = BrowseHistory()
    history.push(url='https://a.example.com')
    history.push(url='https://b.example.com')
    history.push(url='https://c.example.com')

    iterator = history.create_iterator()
    while iterator.has_next():
        url = iterator.current()
        print(url)
        iterator.next()
    # https://a.example.com
    # https://b.example.com
    # https://c.example.com
