FILENAME = r'C:\Temp\bootfilure.txt'


# Read whole file as a text to ``content`` variable
with open(FILENAME, encoding='utf-8') as file:
    content = file.read()


# Convert file to list by line
with open(FILENAME, encoding='utf-8') as file:
    lines_in_file = file.readlines()


# Convert file to list by line, select 1-30 lines
with open(FILENAME, encoding='utf-8') as file:
    selected_lines = file.readlines()[1:30]


# Convert file to list by line
# file by default iterate by line like ``file.readlines()``
with open(FILENAME, encoding='utf-8') as file:
    for line in file:
        if not line.startswith('#'):
            print(line)
