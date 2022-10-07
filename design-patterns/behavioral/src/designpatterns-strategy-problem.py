from dataclasses import dataclass


@dataclass
class ImageStorage:
    compressor: str
    filter: str

    def store(self, filename) -> None:
        if self.compressor == 'jpeg':
            print('Compressing using JPEG')
        elif self.compressor == 'png':
            print('Compressing using PNG')

        if self.filter == 'black&white':
            print('Applying Black&White filter')
        elif self.filter == 'high-contrast':
            print('Applying high contrast filter')
