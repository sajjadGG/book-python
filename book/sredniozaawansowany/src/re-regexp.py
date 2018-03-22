import re


COMMIT_MESSAGE = "Refs #23919, #31337 -- Removed obsolete comments about u'' prefixes."


re.findall(r'#[0-9]+', COMMIT_MESSAGE)
# ['#23919', '#31337']

re.search(r'#[0-9]+', COMMIT_MESSAGE).group()
# '#23919'

re.match(r'#[0-9]+', COMMIT_MESSAGE)
# None


issues = re.compile(r'#[0-9]+')
issues.findall(COMMIT_MESSAGE)
# ['#23919', '#31337']

re.findall(issues, COMMIT_MESSAGE)
# ['#23919', '#31337']



COMMIT_MESSAGE = """Fixed #27533 -- Fixed inspectdb crash if a unique constraint uses an … #31337
 …unsupported type."""

issues = re.compile(r'#[0-9]+', flags=re.MULTILINE)

issues.findall(COMMIT_MESSAGE)
# ['#23919', '#31337']
