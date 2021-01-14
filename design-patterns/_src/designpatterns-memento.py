from dataclasses import dataclass, field
from typing import Final


@dataclass
class EditorState:
    __content: Final[str]

    def get_content(self):
        return self.__content


@dataclass
class History:
    __states: list[EditorState] = field(default_factory=list)

    def push(self, state: EditorState) -> None:
        self.__states.append(state)

    def pop(self) -> EditorState:
        return self.__states.pop()


class Editor:
    __content: str

    def set_content(self, content: str) -> None:
        self.__content = content

    def get_content(self) -> str:
        return self.__content

    def create_state(self):
        return EditorState(self.__content)

    def restore_state(self, state: EditorState):
        self.__content = state.get_content()


if __name__ == '__main__':
    editor = Editor()
    history = History()

    editor.set_content('a')
    history.push(editor.create_state())
    print(editor.get_content())
    # a

    editor.set_content('b')
    history.push(editor.create_state())
    print(editor.get_content())
    # b

    editor.set_content('c')
    print(editor.get_content())
    # c

    editor.restore_state(history.pop())
    print(editor.get_content())
    # b
