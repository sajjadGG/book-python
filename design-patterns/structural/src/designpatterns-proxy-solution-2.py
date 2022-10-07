from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Proxy:
    pass


class Ebook(ABC):
    @abstractmethod
    def show(self) -> None:
        pass

    @abstractmethod
    def get_filename(self) -> None:
        pass


@dataclass
class RealEbook(Ebook):
    filename: str

    def __post_init__(self):
        self.load()

    def load(self) -> None:
        print(f'Loading the ebook {self.filename}')

    def show(self) -> None:
        print(f'Showing the ebook {self.filename}')

    def get_filename(self) -> None:
        return self.filename


@dataclass
class EbookProxy(Ebook):
    filename: str
    ebook: RealEbook | None = None

    def show(self) -> None:
        if self.ebook is None:
            self.ebook = RealEbook(self.filename)
        self.ebook.show()

    def get_filename(self) -> None:
        return self.filename


@dataclass()
class LoggingEbookProxy(Ebook):
    filename: str
    ebook: RealEbook | None = None

    def show(self) -> None:
        if self.ebook is None:
            self.ebook = RealEbook(self.filename)
        print('Logging')
        self.ebook.show()

    def get_filename(self) -> None:
        return self.filename


@dataclass
class Library:
    ebooks: dict[str, RealEbook] = field(default_factory=dict)

    def add(self, ebook: RealEbook) -> None:
        self.ebooks[ebook.get_filename()] = ebook

    def open(self, filename: str) -> None:
        self.ebooks.get(filename).show()


if __name__ == '__main__':
    library: Library = Library()
    filenames: list[str] = ['ebook-a.pdf', 'ebook-b.pdf', 'ebook-c.pdf']  # Read from database

    for filename in filenames:
        library.add(LoggingEbookProxy(filename))

    library.open('ebook-a.pdf')
    # Loading the ebook ebook-a.pdf
    # Logging
    # Showing the ebook ebook-a.pdf
