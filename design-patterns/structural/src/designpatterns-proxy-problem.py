from dataclasses import dataclass, field


@dataclass
class Ebook:
    filename: str

    def __post_init__(self):
        self._load()

    def _load(self) -> None:
        print(f'Loading the ebook {self.filename}')

    def show(self) -> None:
        print(f'Showing the ebook {self.filename}')

    def get_filename(self) -> None:
        return self.filename


@dataclass
class Library:
    ebooks: dict[str, Ebook] = field(default_factory=dict)

    def add(self, ebook: Ebook) -> None:
        self.ebooks[ebook.get_filename()] = ebook

    def open(self, filename: str) -> None:
        self.ebooks.get(filename).show()


if __name__ == '__main__':
    library: Library = Library()
    filenames: list[str] = ['ebook-a.pdf', 'ebook-b.pdf', 'ebook-c.pdf']  # Read from database

    for filename in filenames:
        library.add(Ebook(filename))

    library.open('ebook-a.pdf')
    # Loading the ebook ebook-a.pdf
    # Loading the ebook ebook-b.pdf
    # Loading the ebook ebook-c.pdf
    # Showing the ebook ebook-a.pdf
