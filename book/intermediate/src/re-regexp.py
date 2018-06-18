import re

PATTERN = r'[A-Z]{2,10}-[0-9]+'  # used for JIRA issue id
PATTERN = r'#[0-9]+'  # used for redmine and track issue id


COMMIT_MESSAGE = "Refs #23919, #31337 -- Removed obsolete comments about u'' prefixes."


re.findall(PATTERN, COMMIT_MESSAGE)
# ['#23919', '#31337']

re.search(PATTERN, COMMIT_MESSAGE).group()
# '#23919'

re.match(PATTERN, COMMIT_MESSAGE)
# None


issues = re.compile(PATTERN)
issues.findall(COMMIT_MESSAGE)
# ['#23919', '#31337']

re.findall(issues, COMMIT_MESSAGE)
# ['#23919', '#31337']
