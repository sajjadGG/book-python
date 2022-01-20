from pathlib import Path
import shutil
import logging
import re


SRC_DIR = Path('/Users/matt/Developer/book-python')
OUT_DIR = Path('/Users/matt/Developer/_template/_notes/')

BOOKS = [
    'advanced',
    'basics',
    'data-science',
    'design-patterns',
    'devops',
    'django',
    'fastapi',
    'intermediate',
    'machine-learning',
    'matplotlib',
    'network',
    'numpy',
    'OOP',
    'pandas',
]

EXCLUDE_HEADERS = (
    'Assignments',
    'Use Case',
    'Case Study',
    'Example',
)


HEADINGS = re.compile('^.{3,80}$\n^[*=-]{3,80}$', flags=re.MULTILINE)
FILES = re.compile('^\s+([-\w/]*\.rst)$', re.MULTILINE)


def find(file, regex):
    if not file.exists():
        return []
    with open(file) as f:
        return regex.findall(f.read())


def get_headers(file):
    headers = ''
    for header in find(file, HEADINGS):
        if not header.startswith(EXCLUDE_HEADERS):
            headers += '\n\n' + header
    return headers + '\n\n\n'


for book in BOOKS:
    mastertoc = SRC_DIR / book / Path('_index.rst')
    chapters = []
    outdir = OUT_DIR / book
    shutil.rmtree(outdir)
    outdir.mkdir(exist_ok=True)

    for file in find(mastertoc, FILES):
        try:
            chapter, topic = file.split('/')
            topic = topic.removesuffix('.rst')
        except ValueError:
            logging.error(file)
            continue

        if chapter not in chapters:
            chapters.append(chapter)

        i = chapters.index(chapter)
        filename = Path(f'{i:02}-{chapter}.md')
        headers = get_headers(SRC_DIR/book/file)

        with open(outdir/filename, mode='a') as file:
            file.write(headers)
