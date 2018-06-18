import re


COMMIT_MESSAGE = """Fixed #27533 -- Fixed inspectdb crash if a unique constraint uses an … #31337
 …unsupported type."""

re.findall(r'#[0-9]+', COMMIT_MESSAGE, flags=re.MULTILINE)
# ['#23919', '#31337']

issues = re.compile(r'#[0-9]+', flags=re.MULTILINE)
issues.findall(COMMIT_MESSAGE)
# ['#23919', '#31337']
