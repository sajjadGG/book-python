#!/usr/bin/env python
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

    # for line in iter(process.stdout.readline, b''):
    #     print(line.decode().strip())
    # process.wait()
    # return process.returncode


class Html(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        run('clear && printf "\e[3J"')  # noqa
        if chapter is None:
            src = BASE_DIR
            dst = Path('/tmp') / 'pybook'
        else:
            src = BASE_DIR / chapter
            dst = Path('/tmp') / chapter
        rmtree(dst, ignore_errors=True)
        run(f'sphinx-build -a -E -j auto --color -b html {src} {dst}')


class TestDoctest(Action):
    def is_ignored(self, file: Path):
        doctestignore = Path(file.parts[0]) / '.doctestignore'
        if doctestignore.exists():
            log.warning(f'IGNORED\t{file}')
            return True
        else:
            return False

    def is_skipped(self, file: Path):
        if '# doctest: +SKIP_FILE' in file.read_text():
            log.warning(f'SKIPPED\t{file}')
            return True
        else:
            return False

    def is_venv(self, file: Path):
        log.debug(f'VENV\t{file}')
        return str(file).startswith('.venv-py')

    def count_doctests(self, file: Path):
        return file.read_text().count('>>>')

    def get_files(self, directory: str):
        if directory is None:
            directory = ''
        yield from Path(directory).rglob('*.rst')
        yield from Path(directory).rglob('*.py')

    def run_test(self, file: Path):
        log.debug(f'RUN\t {file}')
        exitcode = run(f'python -m doctest {file}', timeout=20)
        if exitcode == 0:
            log.info(f'PASSED\t{file}')
        else:
            log.critical(f'FAILED\t{file}')
            exit(1)

    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        run('clear && printf "\e[3J"')  # noqa
        all_tests = 0
        for file in sorted(self.get_files(chapter)):
            if self.is_ignored(file): continue
            if self.is_venv(file): continue
            if self.is_skipped(file): continue
            if ntests := self.count_doctests(file):
                self.run_test(file)
                all_tests += ntests
            else:
                log.error(f'WITHOUT\t{file}')
        logging.warning(f'\nAll tests {all_tests}')


if __name__ == '__main__':
    parser = ArgumentParser(prog='Make')

    parser.add_argument('--html',
                        nargs='?', metavar='CHAPTER', action=Html,
                        help='Build documentation in html format')

    parser.add_argument('--doctest',
                        nargs='?', metavar='CHAPTER', action=TestDoctest,
                        help='Test ReST files')

    args = parser.parse_args()
