from dataclasses import dataclass, field
from typing import Final


@dataclass
class EditorState:
    content: Final[str]

    def get_content(self):
        return self.content


@dataclass
class History:
    states: list[EditorState] = field(default_factory=list)

    def push(self, state: EditorState) -> None:
        self.states.append(state)

    def pop(self) -> EditorState:
        return self.states.pop()


class Editor:
    content: str

    def set_content(self, content: str) -> None:
        self.content = content

    def get_content(self) -> str:
        return self.content

    def create_state(self):
        return EditorState(self.content)

    def restore_state(self, state: EditorState):
        self.content = state.get_content()


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
