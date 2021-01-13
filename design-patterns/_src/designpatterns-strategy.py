from abc import ABCMeta, abstractmethod


class Compressor(metaclass=ABCMeta):
    @abstractmethod
    def compress(self, filename: str) -> None:
        pass

class JPEGCompressor(Compressor):
    def compress(self, filename: str) -> None:
        print('Compressing using JPEG')

class PNGCompressor(Compressor):
    def compress(self, filename: str) -> None:
        print('Compressing using PNG')


class Filter(metaclass=ABCMeta):
    @abstractmethod
    def apply(self, filename) -> None:
        pass

class BlackAndWhiteFilter(Filter):
    def apply(self, filename) -> None:
        print('Applying Black and White filter')

class HighContrastFilter(Filter):
    def apply(self, filename) -> None:
        print('Applying high contrast filter')


class ImageStorage:
    def store(self, filename: str, compressor: Compressor, filter: Filter) -> None:
        compressor.compress(filename)
        filter.apply(filename)


if __name__ == '__main__':
    image_storage = ImageStorage()

    image_storage.store('myfile.jpg', JPEGCompressor(), BlackAndWhiteFilter())
    # Compressing using JPEG
    # Applying Black and White filter

    image_storage.store('myfile.png', PNGCompressor(), BlackAndWhiteFilter())
    # Compressing using PNG
    # Applying Black and White filter
