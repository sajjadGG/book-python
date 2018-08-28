FILENAME = r'C:\Users\desktop.ini'


with open(FILENAME, encoding='utf-8') as file:
    content = file.read()


with open(FILENAME, encoding='utf-8') as file:
    content = file.readlines()


with open(FILENAME, encoding='utf-8') as file:
    selected_lines = file.readlines()[1:30]


with open(FILENAME, encoding='utf-8') as file:
    for line in file:
        print(line)
