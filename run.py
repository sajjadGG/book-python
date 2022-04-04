#!/usr/bin/env python
"""
usage: run.py [-h] [-b [CHAPTER]] [-t [CHAPTER]] [-i [CHAPTER]] [-g]

options:
  -h, --help            show this help message and exit
  -b [CHAPTER], --build [CHAPTER]
                        build documentation in html format
  -t [CHAPTER], --doctest [CHAPTER]
                        test ReST files
  -i [CHAPTER], --install [CHAPTER]
                        install requirements
  -g, --gather          gather chapter requirements to main requirements

example:
    run.py --install
    run.py --install basics
    run.py --doctest
    run.py --doctest basics
    run.py --doctest basics/types
"""

import logging
import sys
from pathlib import Path
from argparse import ArgumentParser, Action
from shutil import rmtree
from subprocess import Popen, PIPE, TimeoutExpired

sys.tracebacklimit = 8
logging.basicConfig(level='INFO', format='%(message)s')
log = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent


def run(cmd, timeout=None):
    process = Popen(cmd, stdout=PIPE, shell=True)
    while process.poll() is None:
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except TimeoutExpired:
            process.kill()
            raise TimeoutError from None
        if stdout:
            print(stdout.decode())
    return process.returncode


class Gather(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        run('clear && printf "\e[3J"')  # noqa
        run(f'cat */requirements.txt |sort |uniq > requirements.txt')
        log.info('Requirements Gathered in requirements.txt')


class Install(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        if chapter is None:
            chapter = '.'
        run('clear && printf "\e[3J"')  # noqa
        run(f'pip install -r {chapter}/requirements.txt')
        log.info('Requirements installed')


class Build(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        if chapter is None:
            src = BASE_DIR
            dst = Path('/tmp') / 'pybook'
        else:
            src = BASE_DIR / chapter
            dst = Path('/tmp') / chapter
        rmtree(dst, ignore_errors=True)
        run('clear && printf "\e[3J"')  # noqa
        run(f'sphinx-build -a -E -j auto --color -b html {src} {dst}')


class Doctest(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        run('clear && printf "\e[3J"')  # noqa
        all_tests = 0
        for file in sorted(self.get_files(chapter)):
            if self.is_ignored(file): continue
            if self.is_venv(file): continue
            if self.is_skipped(file): continue
            if count := self.count_doctests(file):
                self.run_doctest(file)
                all_tests += count
            else:
                log.error(f'NOTESTS\t{file}')
        logging.warning(f'\nAll tests {all_tests}')

    @staticmethod
    def is_ignored(file: Path):
        doctestignore = Path(file.parts[0]) / '.doctestignore'
        if doctestignore.exists():
            log.warning(f'IGNORED\t{file}')
            return True
        else:
            return False

    @staticmethod
    def is_skipped(file: Path):
        if '# doctest: +SKIP_FILE' in file.read_text():
            log.warning(f'SKIPPED\t{file}')
            return True
        else:
            return False

    @staticmethod
    def is_venv(file: Path):
        log.debug(f'VENV\t{file}')
        return str(file).startswith('.venv-py')

    @staticmethod
    def count_doctests(file: Path):
        return file.read_text().count('>>> ')

    @staticmethod
    def get_files(directory: str):
        if directory is None:
            directory = ''
        yield from Path(directory).rglob('*.rst')
        yield from Path(directory).rglob('*.py')

    @staticmethod
    def run_doctest(file: Path):
        log.debug(f'RUN\t {file}')
        exitcode = run(f'python -m doctest {file}', timeout=20)
        if exitcode == 0:
            log.info(f'PASSED\t{file}')
        else:
            log.critical(f'FAILED\t{file}')
            exit(1)


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-b', '--build',
                        nargs='?', metavar='CHAPTER', action=Build,
                        help='build documentation in html format')

    parser.add_argument('-d', '--doctest',
                        nargs='?', metavar='CHAPTER', action=Doctest,
                        help='doctest *.rst and *.py files')

    parser.add_argument('-i', '--install',
                        nargs='?', metavar='CHAPTER', action=Install,
                        help='install requirements')

    parser.add_argument('-g', '--gather',
                        nargs=0, action=Gather,
                        help='gather chapter requirements to one file')

    parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        exit(1)
