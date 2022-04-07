import re
from pathlib import Path
from typing import Iterator
from _config import BOOKS, SRC_DIR, OUT_DIR, log


def get_files(book: str) -> Iterator[Path]:  # noqa
    yield from SRC_DIR.rglob(f'{book}/assignments/*.py')
    yield from SRC_DIR.rglob(f'{book}/*/assignments/*.py')


def split_assignment_solutions(file: Path) -> tuple[str, str]:  # noqa
    content = re.sub(
        pattern='^TODO: .+$',
        repl='',
        string=file.read_text(),
        flags=re.MULTILINE)

    if '"""' not in content:
        log.error(f'Docstring not found: {file}')
        return content, ''

    if '# Solution' not in content:
        log.error(f'Solution not found in: {file}')
        return content, ''

    assignment, solutions = content.split('# Solution', maxsplit=1)
    log.debug(f'Split ok: {file}')
    return assignment, solutions


def write_file(path: Path, content: str) -> None:
    log.debug(f'Writing file: {path}')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def process_file(book, file):  # noqa
    assignment, solutions = split_assignment_solutions(file)

    filename = (str(file.relative_to(SRC_DIR))
                .replace('assignments/', '')
                .replace(book, '', 1)
                .removeprefix('/'))

    path = Path(OUT_DIR / book / '_assignments' / filename)
    write_file(path, content=assignment)

    path = Path(OUT_DIR / book / '_solutions' / filename)
    write_file(path, content=solutions)


if __name__ == '__main__':
    for book in BOOKS:
        log.info(f'Processing book: {book}')

        for file in get_files(book):
            log.info(f'Processing file: {file}')
            process_file(book, file)
