from dataclasses import dataclass, field
from typing import List

FILE = r'/tmp/context-manager.txt'


@dataclass
class File:
    name: str
    content: List[str] = field(default_factory=[])

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return self.save_file()

    def append_line(self, line):
        self.content.append(line + '\n')

    def save_file(self):
        with open(self.name, mode='w', encoding='utf-8') as file:
            file.writelines(self.content)


with File(FILE) as file:
    file.append_line('first line')
    file.append_line('second line')
    file.append_line('third line')
