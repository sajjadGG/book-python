from enum import Enum


class Slide:
    text: str

    def __init__(self, text: str) -> None:
        self.text = text

    def get_text(self) -> str:
        return self.text


class PresentationBuilder:
    def add_slide(self, slide: Slide) -> None:
        raise NotImplementedError


#%% Formats
class PresentationFormat(Enum):
    PDF = 1
    IMAGE = 2
    POWERPOINT = 3
    MOVIE = 4

class PDFDocument:
    def add_page(self, text: str) -> None:
        print('Adding a page to PDF')

class Movie:
    def add_frame(self, text: str, duration: int) -> None:
        print('Adding a frame to a movie')

class PDFDocumentBuilder(PresentationBuilder):
    document: PDFDocument

    def __init__(self):
        self.document = PDFDocument()

    def add_slide(self, slide: Slide) -> None:
        self.document.add_page(slide.get_text())

    def get_pdf_document(self) -> PDFDocument:
        return self.document


class MovieBuilder(PresentationBuilder):
    movie: Movie

    def __init__(self):
        self.movie = Movie()

    def add_slide(self, slide: Slide) -> None:
        self.movie.add_frame(slide.get_text(), duration=3)

    def get_movie(self) -> Movie:
        return self.movie


#%% Main
class Presentation:
    slides: list[Slide]

    def __init__(self) -> None:
        self.slides = []

    def add_slide(self, slide: Slide) -> None:
        self.slides.append(slide)

    def export(self, builder: PresentationBuilder) -> None:
        builder.add_slide(Slide('Copyright'))
        for slide in self.slides:
            builder.add_slide(slide)


if __name__ == '__main__':
    presentation = Presentation()
    presentation.add_slide(Slide('Slide 1'))
    presentation.add_slide(Slide('Slide 2'))

    builder = PDFDocumentBuilder()
    presentation.export(builder)
    movie = builder.get_pdf_document()

    builder = MovieBuilder()
    presentation.export(builder)
    movie = builder.get_movie()
