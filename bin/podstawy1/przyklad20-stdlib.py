import datetime

today = datetime.date.today()
now = datetime.datetime.now()

d = now - datetime.timedelta(days=30)
d = d.replace(tzinfo=datetime.timezone.utc)

wyswietl = '{:%Y-%m-%d %H:%M}'.format(d)
#print(wyswietl)


data = input('Podaj datę: ')

try:
    wyswietl = datetime.datetime.strptime(data, '%Y-%m-%d')
except ValueError:
    wyswietl = datetime.datetime.strptime(data, '%m/%d/%y')

print(wyswietl)







