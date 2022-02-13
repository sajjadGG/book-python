from subprocess import run
from _config import log, BOOKS, OUT_DIR


def exec(cmd, cwd=None):
    result = run(cmd,
                 shell=True,
                 cwd=cwd,
                 capture_output=True,
                 encoding='utf-8')
    log.warning(result.stdout)

for book in BOOKS:
    exec('git commit -am "Assignments"', cwd=OUT_DIR/book)
    exec('git pull --rebase', cwd=OUT_DIR/book)
    exec('git push', cwd=OUT_DIR/book)
