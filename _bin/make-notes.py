import re
from pathlib import Path
from shutil import rmtree
from _config import log, BOOKS, SRC_DIR, OUT_DIR
from _config import get_toc, get_chapters

# TODO: highlights nie obsługuje wieloliniowych list (hard wrap)
# TODO: stworzyć sekcję TL;DR (albo wykorzysta
# TODO: stworzyć sekcję Recap z rozdziału
# TODO: wyciąganie glossary (make-glossary.py)
# TODO: linki do materiałów, odnośnie każdego rozdziału
# TODO: generowanie notatek i zadań powinno odbywać się na zasadzie podrozdziałów, tzn. w katalogu z podrozdziałem są notatki, zadania, rozwiązania, dane do zadań i pliki tymczasowe

def get_headers(file: Path) -> list[str]:
    margin = '(?:\n{0,1})'
    title = r'^.{3,80}\n'
    underline = r'^[*=-]{3,80}\n{0,1}'
    highlights = r'(?:^\*\s.+\n)*'
    headers = re.findall(
        pattern=f'{margin}{title}{underline}{highlights}',
        string=file.read_text(),
        flags=re.MULTILINE)
    exclude = ('Use Case', 'Case Study', 'Example',
               'SetUp', 'References', 'Assignments')
    return [header
            for header in headers
            if not header.lstrip().startswith(exclude)]


if __name__ == '__main__':
    for book in BOOKS:
        outdir = OUT_DIR / book / '_notes'
        rmtree(outdir)
        outdir.mkdir(exist_ok=True, parents=True)
        chapters = get_chapters(book)

        for file in get_toc(book):
            file = Path(file)
            topic = file.stem
            chapter = file.parent.name

            if not chapter:
                log.error(f'No chapter directory: {book}/{file}')
                continue

            i = chapters.index(chapter)
            notes = outdir / f'{i:02}-{chapter}.rst'
            headers = get_headers(SRC_DIR / book / file)

            with notes.open(mode='a') as fp:
                fp.writelines(headers)
