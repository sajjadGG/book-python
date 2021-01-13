from dataclasses import dataclass, field
from typing import Final


@dataclass
class EditorState:
    _content: Final[str]

    def get_content(self):
        return self._content


@dataclass
class History:
    _states: list[EditorState] = field(default_factory=list)

    def push(self, state: EditorState) -> None:
        self._states.append(state)

    def pop(self) -> EditorState:
        return self._states.pop()


class Editor:
    _content: str

    def set_content(self, content: str) -> None:
        self._content = content

    def get_content(self) -> str:
        return self._content

    def create_state(self):
        return EditorState(self._content)

    def restore_state(self, state: EditorState):
        self._content = state.get_content()


if __name__ == '__main__':
    editor = Editor()
    history = History()

    editor.set_content('a')
    history.push(editor.create_state())

    editor.set_content('b')
    history.push(editor.create_state())

    editor.set_content('c')
    editor.restore_state(history.pop())

    print(editor.get_content())
