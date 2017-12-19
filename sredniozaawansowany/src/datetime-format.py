import datetime

now = datetime.datetime.now()
print(f'Now is {now:%Y-%m-%d %H:%M}!')
# Now is 2017-12-19 17:40!

out = now.strftime('%A, %B %d, %I:%M %p')
print(out)
# Tuesday, December 19, 05:40 PM