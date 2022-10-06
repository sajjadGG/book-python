from dataclasses import dataclass


@dataclass
class ImageStorage:
    _compressor: str
    _filter: str

    def store(self, filename) -> None:
        if self._compressor == 'jpeg':
            print('Compressing using JPEG')
        elif self._compressor == 'png':
            print('Compressing using PNG')

        if self._filter == 'black&white':
            print('Applying Black&White filter')
        elif self._filter == 'high-contrast':
            print('Applying high contrast filter')
