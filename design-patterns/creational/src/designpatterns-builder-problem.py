from enum import Enum


class Slide:
    text: str

    def __init__(self, text: str) -> None:
        self.text = text

    def get_text(self) -> str:
        return self.text


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


#%% Main
class Presentation:
    slides: list[Slide]

    def __init__(self) -> None:
        self.slides = []

    def add_slide(self, slide: Slide) -> None:
        self.slides.append(slide)

    def export(self, format: PresentationFormat) -> None:
        if format == PresentationFormat.PDF:
            pdf = PDFDocument()
            pdf.add_page('Copyright')
            for slide in self.slides:
                pdf.add_page(slide.get_text())
        elif format == PresentationFormat.MOVIE:
            movie = Movie()
            movie.add_frame('Copyright', duration=3)
            for slide in self.slides:
                movie.add_frame(slide.get_text(), duration=3)
