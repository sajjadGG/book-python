import logging
import sys
from doctest import TestResults, testmod
from pathlib import Path
from _config import VERBOSE, SRC_DIR, log



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


if __name__ == '__main__':
    log.warning(f'Excluded: {EXCLUDE}')

    for file in SRC_DIR.rglob('assignments/*.py'):
        path = str(file.relative_to(SRC_DIR)).replace('assignments/', '')
        log.info(f'Processing: {file}')

        if path.startswith(EXCLUDE):
            log.warning('Skipping - path is excluded')
            continue

        run_doctest(file)
