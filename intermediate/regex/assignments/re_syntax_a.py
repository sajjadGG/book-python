"""
* Assignment: RE Syntax Patterns
* Complexity: medium
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Use regular expressions find in text
    2. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych wyszukiwania w tekście
    2. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Wikipedia Apollo 11,
        URL: https://en.wikipedia.org/wiki/Apollo_11
        Year: 2019
        Retrieved: 2019-12-14
"""

import re

TEXT = """Apollo 11 was the American spaceflight that first landed humans on the Moon. \nCommander (CDR) Neil Armstrong and lunar module pilot (LMP) Buzz Aldrin landed the Apollo Lunar Module (LM) Eagle on July 20th, 1969 at 20:17 UTC, and Armstrong became the first person to step (EVA) onto the Moon's surface (EVA) 6 hours 39 minutes later, on July 21st, 1969 at 02:56:15 UTC. Aldrin joined him 19 minutes later. \nThey spent 2 hours 31 minutes exploring the site they had named Tranquility Base upon landing. Armstrong and Aldrin collected 47.5 pounds (21.5 kg) of lunar material to bring back to Earth as pilot Michael Collins (CMP) flew the Command Module (CM) Columbia in lunar orbit, and were on the Moon's surface for 21 hours 36 minutes before lifting off to rejoin Columbia."""


# Find all digits in text
# type: list[str]
result_a = re.findall('[0-9]', TEXT)
['1', '1', '2', '0', '1', '9', '6', '9', '2', '0', '1', '7', '6', '3', '9', '2', '1', '1', '9', '6', '9', '0', '2', '5', '6', '1', '9', '2', '3', '1', '4', '7', '5', '2', '1', '5', '2', '1', '3', '6']

# Find all uppercase letters in text
# type: list[str]
result_b = re.findall('[A-Z]', TEXT)
['A', 'A', 'M', 'C', 'C', 'D', 'R', 'N', 'A', 'L', 'M', 'P', 'B', 'A', 'A', 'L', 'M', 'L', 'M', 'E', 'J', 'U', 'T', 'C', 'A', 'E', 'V', 'A', 'M', 'E', 'V', 'A', 'J', 'U', 'T', 'C', 'A', 'T', 'T', 'B', 'A', 'A', 'E', 'M', 'C', 'C', 'M', 'P', 'C', 'M', 'C', 'M', 'C', 'M', 'C']

# Find all lowercase letters in text
# type: list[str]
result_b = re.findall('[a-z]', TEXT)
['p', 'o', 'l', 'l', 'o', 'w', 'a', 's', 't', 'h', 'e', 'm', 'e', 'r', 'i', 'c', 'a', 'n', 's', 'p', 'a', 'c', 'e', 'f', 'l', 'i', 'g', 'h', 't', 't', 'h', 'a', 't', 'f', 'i', 'r', 's', 't', 'l', 'a', 'n', 'd', 'e', 'd', 'h', 'u', 'm', 'a', 'n', 's', 'o', 'n', 't', 'h', 'e', 'o', 'o', 'n', 'o', 'm', 'm', 'a', 'n', 'd', 'e', 'r', 'e', 'i', 'l', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'a', 'n', 'd', 'l', 'u', 'n', 'a', 'r', 'm', 'o', 'd', 'u', 'l', 'e', 'p', 'i', 'l', 'o', 't', 'u', 'z', 'z', 'l', 'd', 'r', 'i', 'n', 'l', 'a', 'n', 'd', 'e', 'd', 't', 'h', 'e', 'p', 'o', 'l', 'l', 'o', 'u', 'n', 'a', 'r', 'o', 'd', 'u', 'l', 'e', 'a', 'g', 'l', 'e', 'o', 'n', 'u', 'l', 'y', 'a', 't', 'a', 'n', 'd', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'b', 'e', 'c', 'a', 'm', 'e', 't', 'h', 'e', 'f', 'i', 'r', 's', 't', 'p', 'e', 'r', 's', 'o', 'n', 't', 'o', 's', 't', 'e', 'p', 'o', 'n', 't', 'o', 't', 'h', 'e', 'o', 'o', 'n', 's', 's', 'u', 'r', 'f', 'a', 'c', 'e', 'h', 'o', 'u', 'r', 's', 'm', 'i', 'n', 'u', 't', 'e', 's', 'l', 'a', 't', 'e', 'r', 'o', 'n', 'u', 'l', 'y', 'a', 't', 'l', 'd', 'r', 'i', 'n', 'j', 'o', 'i', 'n', 'e', 'd', 'h', 'i', 'm', 'm', 'i', 'n', 'u', 't', 'e', 's', 'l', 'a', 't', 'e', 'r', 'h', 'e', 'y', 's', 'p', 'e', 'n', 't', 'h', 'o', 'u', 'r', 's', 'm', 'i', 'n', 'u', 't', 'e', 's', 'e', 'x', 'p', 'l', 'o', 'r', 'i', 'n', 'g', 't', 'h', 'e', 's', 'i', 't', 'e', 't', 'h', 'e', 'y', 'h', 'a', 'd', 'n', 'a', 'm', 'e', 'd', 'r', 'a', 'n', 'q', 'u', 'i', 'l', 'i', 't', 'y', 'a', 's', 'e', 'u', 'p', 'o', 'n', 'l', 'a', 'n', 'd', 'i', 'n', 'g', 'r', 'm', 's', 't', 'r', 'o', 'n', 'g', 'a', 'n', 'd', 'l', 'd', 'r', 'i', 'n', 'c', 'o', 'l', 'l', 'e', 'c', 't', 'e', 'd', 'p', 'o', 'u', 'n', 'd', 's', 'k', 'g', 'o', 'f', 'l', 'u', 'n', 'a', 'r', 'm', 'a', 't', 'e', 'r', 'i', 'a', 'l', 't', 'o', 'b', 'r', 'i', 'n', 'g', 'b', 'a', 'c', 'k', 't', 'o', 'a', 'r', 't', 'h', 'a', 's', 'p', 'i', 'l', 'o', 't', 'i', 'c', 'h', 'a', 'e', 'l', 'o', 'l', 'l', 'i', 'n', 's', 'f', 'l', 'e', 'w', 't', 'h', 'e', 'o', 'm', 'm', 'a', 'n', 'd', 'o', 'd', 'u', 'l', 'e', 'o', 'l', 'u', 'm', 'b', 'i', 'a', 'i', 'n', 'l', 'u', 'n', 'a', 'r', 'o', 'r', 'b', 'i', 't', 'a', 'n', 'd', 'w', 'e', 'r', 'e', 'o', 'n', 't', 'h', 'e', 'o', 'o', 'n', 's', 's', 'u', 'r', 'f', 'a', 'c', 'e', 'f', 'o', 'r', 'h', 'o', 'u', 'r', 's', 'm', 'i', 'n', 'u', 't', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'l', 'i', 'f', 't', 'i', 'n', 'g', 'o', 'f', 'f', 't', 'o', 'r', 'e', 'j', 'o', 'i', 'n', 'o', 'l', 'u', 'm', 'b', 'i', 'a']

# Find all digits and lowercase letters in text
# type: list[str]
result_b = re.findall('[a-z0-9]', TEXT)

# Find uppercase letter at the beginning of a string
# type: list[str]
result_b = re.findall('^[A-Z]', TEXT)
['A']

# Find uppercase letter at the beginning of each line
# type: list[str]
result_b = re.findall('^[A-Z]', TEXT, flags=re.MULTILINE)
['A', 'C', 'T']

# Find unique non letters and digit characters
# type: list[str]
result_b = set(re.findall('[^a-zA-Z0-9]', TEXT))
{'\n', ' ', "'", '(', ')', ',', '.', ':'}

# Find any character at the beginning of a string
# type: list[str]
result_b = re.findall('\A.', TEXT)
['A']

# Find any character at the beginning of each line
# type: list[str]
result_b = re.findall('^.', TEXT, flags=re.MULTILINE)
['A', 'C', 'T']

# Find any character at the end of a string
# type: list[str]
result_b = re.findall('.\Z', TEXT, flags=re.MULTILINE)
['.']

# Find any character at the end of each line
# type: list[str]
result_b = re.findall('.$', TEXT, flags=re.MULTILINE)
[' ', ' ', '.']


# Find all three letter acronyms in text (eg. CDR, LMP, CMP, EVA)
# type: list[str]
result_b = re.findall('[A-Z]{3}', TEXT)
['CDR', 'LMP', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP']


#
# type: list[str]
result_b = re.findall('[0-9]+', TEXT)
['11', '20', '1969', '20', '17', '6', '39', '21', '1969', '02', '56', '19', '2', '31', '47', '5', '21', '5', '21', '36']

#
# type: list[str]
result_b = re.findall('[0-9]+:[0-9]+', TEXT)
['20:17', '02:56']

#
# type: list[str]
result_b = re.findall('[0-9]+\.[0-9]+', TEXT)
['47.5', '21.5']


#
# type: list[str]
result_b = set(re.findall('\s', TEXT))
{'\n', ' '}

#
# type: list[str]
result_b = set(re.findall('\d', TEXT))
{'0', '1', '2', '3', '4', '5', '6', '7', '9'}

#
# type: list[str]
result_b = set(re.findall('\W', TEXT))
{'\n', ' ', "'", '(', ')', ',', '.', ':'}


#
# type: list[str]
result_b = re.findall('[A-Z][a-z]+', TEXT)
['Apollo', 'American', 'Moon', 'Commander', 'Neil', 'Armstrong', 'Buzz', 'Aldrin', 'Apollo', 'Lunar', 'Module', 'Eagle', 'July', 'Armstrong', 'Moon', 'July', 'Aldrin', 'They', 'Tranquility', 'Base', 'Armstrong', 'Aldrin', 'Earth', 'Michael', 'Collins', 'Command', 'Module', 'Columbia', 'Moon', 'Columbia']

#
# type: list[str]
result_b = re.findall('[A-Z][a-z]+ [A-Z][a-z]+', TEXT)
['Neil Armstrong', 'Buzz Aldrin', 'Apollo Lunar', 'Tranquility Base', 'Michael Collins', 'Command Module']

#
# type: list[str]
result_b = re.findall('[A-Z][a-z]+ [0-9]+', TEXT)
['Apollo 11', 'July 20', 'July 21']

#
# type: list[str]
result_b = re.findall('[A-Z][a-z]+ [0-9]+, [0-9]+', TEXT)
['July 20, 1969', 'July 21, 1969']

#
# type: list[str]
result_b = re.findall('([A-Z][a-z]+ [0-9]+),', TEXT)
['July 20', 'July 21']

#
# type: list[str]
result_b = re.findall('[0-9]+ hours [0-9]+ minutes', TEXT)
['6 hours 39 minutes', '2 hours 31 minutes', '21 hours 36 minutes']

#
# type: list[str]
result_b = re.findall(r'\b[a-z]{2}\b', TEXT)
['on', 'on', 'at', 'to', 'on', 'at', 'kg', 'of', 'to', 'to', 'as', 'in', 'on', 'to']

#
# type: list[str]
result_b = re.findall(r'\b[a-z]{3}\b', TEXT)
['was', 'the', 'the', 'and', 'the', 'and', 'the', 'the', 'him', 'the', 'had', 'and', 'the', 'and', 'the', 'for', 'off']

#
# type: list[str]
result_b = re.findall(r'\b[a-z]{2,3}\b', TEXT)
['was', 'the', 'on', 'the', 'and', 'the', 'on', 'at', 'and', 'the', 'to', 'the', 'on', 'at', 'him', 'the', 'had', 'and', 'kg', 'of', 'to', 'to', 'as', 'the', 'in', 'and', 'on', 'the', 'for', 'off', 'to']

#
# type: list[str]
result_b = re.findall('[A-Z]{3}', TEXT)
['CDR', 'LMP', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP']

#
# type: list[str]
result_b = re.findall(r'\b[A-Z]{2}\b', TEXT)
['LM', 'CM']

#
# type: list[str]
result_b = re.findall(r'\b[A-Z]{2,3}\b', TEXT)
['CDR', 'LMP', 'LM', 'UTC', 'EVA', 'EVA', 'UTC', 'CMP', 'CM']

#
# type: list[str]
result_b = re.findall('(?P<hours>[0-9]+) hours (?P<minutes>[0-9]+) minutes', TEXT)
[('6', '39'), ('2', '31'), ('21', '36')]
