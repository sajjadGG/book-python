from datetime import datetime


armstrong = '"June 21, 1969 2:56:15 AM UTC"'
armstrong = datetime.strptime(armstrong, '"%B %d, %Y %I:%M:%S %p UTC"')

# 04/12/61 06:07 AM
out = armstrong.strftime('%m/%d/%y %I:%M %p')
print(out)
