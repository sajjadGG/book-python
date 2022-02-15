import re
from pathlib import Path
from shutil import rmtree
from _config import log, BOOKS, SRC_DIR, OUT_DIR
from _config import get_toc, get_chapters

# TODO(matt) highlights nie obsługuje wieloliniowych list (hard wrap)
# TODO(matt) stworzyć sekcję TL;DR
# TODO(matt) stworzyć sekcję Recap z rozdziału
# TODO(matt) wyciąganie glossary (make-glossary.py)
# TODO(matt) linki do materiałów, odnośnie każdego rozdziału


def get_headers(file: Path) -> list[str]:
    margin = '(?:\n{0,1})'
    title = r'^.{3,80}\n'
    underline = r'^[*=-]{3,80}\n{0,1}'
    highlights = r'(?:^\*\s.+\n)*'
    headers = re.findall(
        pattern=f'{margin}{title}{underline}{highlights}',
        string=file.read_text(),
        flags=re.MULTILINE)
    exclude = ('Use Case', 'Case Study', 'Example', 'SetUp', 'References')
    return [header.replace('Assignments\n-----------', 'Assignments\n-----------\n\n ')
            for header in headers
            if not header.startswith(exclude)]


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
                log.error(f'No chapter directory (flat structure): {book}/{file}')
                continue

            i = chapters.index(chapter)
            notes = outdir / f'{i:02}-{chapter}.rst'
            headers = get_headers(SRC_DIR / book / file)

            with notes.open(mode='a') as fp:
                fp.writelines(headers)
