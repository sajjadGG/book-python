from dataclasses import dataclass, field


@dataclass
class Browser:
    history: list[str] = field(default_factory=list)

    def open(self, url: str) -> None:
        ...
        self.history.append(url)

    def __iter__(self) -> 'Browser':
        self._current = 0
        return self

    def __next__(self) -> str:
        if self._current >= len(self.history):
            raise StopIteration
        result = self.history[self._current]
        self._current += 1
        return result


if __name__ == '__main__':
    browser = Browser()
    browser.open('https://python.astrotech.io')
    browser.open('https://numpy.astrotech.io')
    browser.open('https://pandas.astrotech.io')
    browser.open('https://design-patterns.astrotech.io')

    for url in browser:
        print(url)

# https://python.astrotech.io
# https://numpy.astrotech.io
# https://pandas.astrotech.io
# https://design-patterns.astrotech.io
