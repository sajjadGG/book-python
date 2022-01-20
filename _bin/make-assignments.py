import logging
import sys
from doctest import TestResults, testmod
from pathlib import Path
from subprocess import run


logging.basicConfig(
    level='ERROR',
    datefmt='%Y-%m-%d %H:%M:%S',
    format='{levelname:<7} {message}',
    style='{'
)

log = logging.getLogger('assignment')

VERBOSE = False
SOURCE = Path('/Users/matt/Developer/book-python')
DESTINATION = Path('/Users/matt/Developer/_template')

# Paths should not have directory 'assignments' in them
EXCLUDE = (
    'django/',
    'data-science/',
    'machine-learning/',
    'dragon/dragon_beta.py',
    # ModuleNotFoundError: No module named 'dragon_alpha_adv'
    'dragon/dragon_api_adr.py',  # NameError: name 'Dragon' is not defined

    'advanced/decorator/decorator_func_c.py',
    'advanced/concurrency/threading_timer_a.py',
    'advanced/concurrency/threading_timer_b.py',
    'advanced/concurrency/threading_timer_c.py',
    'advanced/concurrency/multiprocessing_client.py',
    'advanced/concurrency/multiprocessing_server.py',

    'advanced/performance/hello-ctypes.py',
    'advanced/performance/setup.py',
    'advanced/performance/optimization_memoize.py',

    'network/transport/socket_backdoor.py',
    'network/transport/botnet_attacker.py',
    'network/transport/socket_heartbeat_client.py',
    'network/transport/socket_heartbeat_server.py',
    'network/transport/botnet_victim.py',
    'network/transport/botnet_heartbeat_receiver.py',
    'network/protocols/imap4.py',
    'network/protocols/ftp_upload.py',
    'network/protocols/ftp_download.py',
    'network/protocols/smtp_ssl.py',  # name 'USERNAME' is not defined
    'network/protocols/pop3.py',
)


# Failing Tests:
# basics/loop/loop_dict_d.py
# basics/loop/loop_while_about_c.py
# decorator/decorator_functools_c.py
# fastapi/web/http_gateway_old.py
# matplotlib/matplotlib_random_points.py
# intermediate/database/sqlite3_join_b.py
# intermediate/modules/venv.py
# design-patterns/structural/assignments/structural_composite_a.py
# fastapi/web/assignments/scrapping_eva.py
# fastapi/web/assignments/requests_github.py
# fastapi/web/assignments/scrapping_iris.py
# fastapi/web/assignments/http_github.py
# fastapi/web/assignments/http_gateway.py
# fastapi/web/assignments/scrapping_temperature.py
# fastapi/web/assignments/http_gateway_old.py
# fastapi/api/assignments/fastapi_schema_a.py
# dragon/assignments/dragon_alpha_basic.py
# dragon/assignments/dragon_alpha_advanced.py
# dragon/assignments/dragon_rc.py
# intermediate/operating-system/system_walk.py
# intermediate/operating-system/argparse_avg.py
# intermediate/operating-system/system_tree.py
# intermediate/builtin/print_formatting.py
# intermediate/builtin/print_lines.py

def run_doctest(file: Path) -> TestResults:
    dirname = str(file.parent)
    module = file.stem
    sys.path.insert(0, dirname)
    m = __import__(module)
    del sys.path[0]
    result = testmod(m, verbose=VERBOSE, raise_on_error=False)
    if result.failed:
        log.error(f'Doctest: error in {file}')
    else:
        log.debug(f'Doctest: success in {file}')
        return result


def get_solutions(file: Path) -> tuple[str, str]:
    content = file.read_text()
    try:
        content, solutions = content.split('# Solution', maxsplit=1)
    except (ValueError, TypeError):
        log.error(f'Solution: error in {file}')
        return '', ''
    else:
        log.debug(f'Solution: success in {file}')
        return content, solutions


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


log.warning(f'Current: {Path.cwd()}')
log.warning(f'Source: {SOURCE}')
log.warning(f'Destination: {DESTINATION}')
log.warning(f'Excluded: {EXCLUDE}')

for file in SOURCE.rglob('assignments/*.py'):
    path = str(file.relative_to(SOURCE)).replace('assignments/', '')
    log.info(f'Processing: {file}')

    if path.startswith(EXCLUDE):
        log.warning('Skipping - path is excluded')
        continue

    tests = run_doctest(file)
    assignment, solutions = get_solutions(file)

    write_file(
        path=Path(DESTINATION / '_assignments' / path),
        content=assignment)

    write_file(
        path=Path(DESTINATION / '_solutions' / path),
        content=solutions)


result = run('git commit -am "Assignments" && git pull --rebase && git push',
             shell=True,
             cwd=DESTINATION,
             capture_output=True,
             encoding='utf-8')

log.critical(result.stdout)
