from typing import Any


class ConfigManager:
    settings: dict[str, Any]

    def __init__(self) -> None:
        self.settings = {}

    def set(self, key: str, value: Any) -> None:
        self.settings[key] = value

    def get(self, key: str) -> Any:
        return self.settings.pop(key)


if __name__ == '__main__':
    manager = ConfigManager()
    manager.set('name', 'Mark')

    other = ConfigManager()
    print(other.get('name'))
    # Traceback (most recent call last):
    # KeyError: 'name'
