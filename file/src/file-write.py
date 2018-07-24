with open(r'C:\Users\desktop.ini', mode='w') as file:
    file.write('foobar')


with open(r'C:\Users\desktop.ini', mode='a') as file:
    file.write('foobar')


with open(r'C:\Users\desktop.ini', mode='w', encoding='utf-8') as file:
    file.write('foobar')
