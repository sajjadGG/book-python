from pathlib import Path
from typing import Iterator
from _config import BOOKS, SRC_DIR, OUT_DIR, log


def get_files(book: str) -> Iterator[Path]:
    yield from SRC_DIR.rglob(f'{book}/assignments/*.py')
    yield from SRC_DIR.rglob(f'{book}/*/assignments/*.py')


def split_assignment_solutions(file: Path) -> tuple[str, str]:
    content = file.read_text()

    if '"""' not in content:
        log.error(f'Todo not found: {file}')
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


for book in BOOKS:
    log.info(f'Processing book: {book}')

    for file in get_files(book):
        log.info(f'Processing file: {file}')
        assignment, solutions = split_assignment_solutions(file)

        filename = (str(file.relative_to(SRC_DIR))
                    .replace('assignments/', '')
                    .replace(book, '')
                    .removeprefix('/'))

        write_file(
            path=Path(OUT_DIR / book / '_assignments' / filename),
            content=assignment)

        write_file(
            path=Path(OUT_DIR / book / '_solutions' / filename),
            content=solutions)
