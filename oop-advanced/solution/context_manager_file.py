from dataclasses import dataclass
from typing import Union


FILE = r'/tmp/context-manager.txt'


@dataclass
class File:
    name: str
    content: Union[list, tuple] = ()

    def __post_init__(self):
        self.content = list(self.content)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        with open(self.name, mode='w', encoding='utf-8') as file:
            for line in self.content:
                file.write(f'{line}\n')

    def append_line(self, line):
        self.content.append(line)


with File(FILE) as file:
    file.append_line('first line')
    file.append_line('second line')
    file.append_line('third line')
