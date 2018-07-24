with open(r'C:\Users\desktop.ini') as file:
    content = file.read()


with open(r'C:\Users\desktop.ini') as file:
    content = file.readlines()


with open(r'C:\Users\desktop.ini') as file:
    selected_lines = file.readlines()[1:30]


with open(r'C:\Users\desktop.ini') as file:
    for line in file:
        print(line)


with open(r'C:\Users\desktop.ini', encoding='utf-8') as file:
    content = file.read()
