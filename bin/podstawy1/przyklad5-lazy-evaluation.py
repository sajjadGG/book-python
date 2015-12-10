import datetime

now = datetime.datetime.now

print(now())

for i in range(0, 9999999):
    pow(i, 10)

print(now())