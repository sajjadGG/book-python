#!/usr/bin/env python
import logging
import sys
from doctest import DocTestFailure, testfile
from pathlib import Path
from argparse import ArgumentParser, Action
from shutil import rmtree
from subprocess import Popen, PIPE, TimeoutExpired

sys.tracebacklimit = 0
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


class TestRST(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        run('clear && printf "\e[3J"')  # noqa
        if chapter is None:
            src = BASE_DIR
        else:
            src = BASE_DIR / chapter
        all_tests = 0
        for file in sorted(src.rglob('*.rst')):
            if 'venv' in str(file):
                log.debug(f'File inside venv: {file}')
                continue
            all_tests += file.read_text().count('>>>')
            log.warning(f'Testing: {file}')
            exitcode = run(f'python -m doctest {file}', timeout=5)
            if exitcode == 1:
                log.error(f'Error: {file}')
                exit(1)
        logging.warning(f'\nAll tests {all_tests}')


class TestPython(Action):
    def __call__(self, parser, namespace, chapter, *args, **kwargs):
        run('clear && printf "\e[3J"')  # noqa
        if chapter is None:
            src = BASE_DIR
        else:
            src = BASE_DIR / chapter
        all_tests = 0
        for file in sorted(src.rglob('*.py')):
            if 'venv' in str(file):
                log.debug(f'File inside venv: {file}')
                continue
            ntests = file.read_text().count('>>>')
            if ntests == 0:
                log.info(f'Tests not found: {file}')
                continue
            all_tests += ntests
            log.warning(f'Testing: {file}')
            exitcode = run(f'python -m doctest {file}', timeout=20)
            if exitcode == 1:
                log.error(f'Error: {file}')
                exit(1)
        logging.warning(f'\nAll tests {all_tests}')


if __name__ == '__main__':
    parser = ArgumentParser(prog='Make')

    parser.add_argument('--html',
                        nargs='?', metavar='CHAPTER', action=Html,
                        help='Build documentation in html format')

    parser.add_argument('--test-rst',
                        nargs='?', metavar='CHAPTER', action=TestRST,
                        help='Test ReST files')

    parser.add_argument('--test-py',
                        nargs='?', metavar='CHAPTER', action=TestPython,
                        help='Test Python files (Assignments)')

    args = parser.parse_args()
